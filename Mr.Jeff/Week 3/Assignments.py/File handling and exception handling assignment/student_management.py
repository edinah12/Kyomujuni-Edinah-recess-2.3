"""Student Record Management System.

This program demonstrates file handling, data processing, exception handling,
logging, and debugging concepts using a menu-driven interface.
"""

from __future__ import annotations

import argparse
import csv
import json
import logging
import shutil
import tempfile
from pathlib import Path
from typing import Dict, List


BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "students.csv"
JSON_FILE = BASE_DIR / "students.json"
LOG_FILE = BASE_DIR / "student_system.log"

CSV_FIELDS = ["reg_no", "name", "age", "gender"]
JSON_FIELDS = ["address", "contact", "program", "email"]
DISPLAY_FIELDS = [
    ("reg_no", "Reg No"),
    ("name", "Name"),
    ("age", "Age"),
    ("gender", "Gender"),
    ("address", "Address"),
    ("contact", "Contact"),
    ("program", "Program"),
    ("email", "Email"),
]


class StudentManagementError(Exception):
    """Base class for custom student management exceptions."""


class StudentNotFoundError(StudentManagementError):
    """Raised when a requested student record does not exist."""


class DuplicateRegistrationError(StudentManagementError):
    """Raised when a registration number already exists."""


class InvalidStudentDataError(StudentManagementError):
    """Raised when user input fails validation."""


def configure_logging(log_path: Path, overwrite: bool = False) -> None:
    """Configure file logging for the application."""

    root_logger = logging.getLogger()
    for handler in list(root_logger.handlers):
        root_logger.removeHandler(handler)
        handler.close()

    root_logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(log_path, mode="w" if overwrite else "a", encoding="utf-8")
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )
    root_logger.addHandler(file_handler)


class StudentManagementSystem:
    """Manage student records stored in CSV and JSON files."""

    def __init__(self, csv_path: Path = CSV_FILE, json_path: Path = JSON_FILE, log_path: Path = LOG_FILE) -> None:
        self.csv_path = csv_path
        self.json_path = json_path
        self.log_path = log_path
        self.ensure_storage()

    def ensure_storage(self) -> None:
        """Create the storage files if they do not already exist."""

        if not self.csv_path.exists():
            with self.csv_path.open("w", newline="", encoding="utf-8") as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=CSV_FIELDS)
                writer.writeheader()

        if not self.json_path.exists():
            with self.json_path.open("w", encoding="utf-8") as json_file:
                json.dump([], json_file, indent=4)

    def _load_csv_records(self) -> List[Dict[str, str]]:
        """Load core student records from the CSV file."""

        file_handle = None
        records: List[Dict[str, str]] = []

        try:
            self.ensure_storage()
            file_handle = self.csv_path.open("r", newline="", encoding="utf-8")
            reader = csv.DictReader(file_handle)
            for row in reader:
                if row.get("reg_no"):
                    records.append(
                        {
                            "reg_no": normalize_reg_no(row.get("reg_no", "")),
                            "name": row.get("name", "").strip(),
                            "age": row.get("age", "").strip(),
                            "gender": row.get("gender", "").strip(),
                        }
                    )
        except Exception as exc:
            logging.exception("Failed to load CSV records.")
            raise StudentManagementError("Unable to read the CSV file.") from exc
        finally:
            if file_handle is not None:
                file_handle.close()

        return records

    def _load_json_details(self) -> Dict[str, Dict[str, str]]:
        """Load additional student details from the JSON file."""

        file_handle = None
        details: Dict[str, Dict[str, str]] = {}

        try:
            self.ensure_storage()
            file_handle = self.json_path.open("r", encoding="utf-8")
            payload = json.load(file_handle)

            if not isinstance(payload, list):
                raise StudentManagementError("JSON file must contain a list of student details.")

            for item in payload:
                if isinstance(item, dict) and item.get("reg_no"):
                    reg_no = normalize_reg_no(str(item.get("reg_no", "")))
                    details[reg_no] = {
                        "reg_no": reg_no,
                        "address": str(item.get("address", "")).strip(),
                        "contact": str(item.get("contact", "")).strip(),
                        "program": str(item.get("program", "")).strip(),
                        "email": str(item.get("email", "")).strip(),
                    }
        except json.JSONDecodeError as exc:
            logging.exception("The JSON file could not be decoded.")
            raise StudentManagementError("Unable to read the JSON file.") from exc
        except Exception as exc:
            logging.exception("Failed to load JSON details.")
            raise StudentManagementError("Unable to read the JSON file.") from exc
        finally:
            if file_handle is not None:
                file_handle.close()

        return details

    def _save_csv_records(self, records: List[Dict[str, str]]) -> None:
        """Save core student records back to the CSV file."""

        file_handle = None

        try:
            file_handle = self.csv_path.open("w", newline="", encoding="utf-8")
            writer = csv.DictWriter(file_handle, fieldnames=CSV_FIELDS)
            writer.writeheader()
            for record in records:
                writer.writerow(
                    {
                        "reg_no": normalize_reg_no(record.get("reg_no", "")),
                        "name": record.get("name", "").strip(),
                        "age": str(record.get("age", "")).strip(),
                        "gender": record.get("gender", "").strip(),
                    }
                )
        except Exception as exc:
            logging.exception("Failed to save CSV records.")
            raise StudentManagementError("Unable to write to the CSV file.") from exc
        finally:
            if file_handle is not None:
                file_handle.close()

    def _save_json_details(self, details: Dict[str, Dict[str, str]]) -> None:
        """Save additional student details back to the JSON file."""

        file_handle = None

        try:
            payload = [details[reg_no] for reg_no in sorted(details)]
            file_handle = self.json_path.open("w", encoding="utf-8")
            json.dump(payload, file_handle, indent=4)
        except Exception as exc:
            logging.exception("Failed to save JSON details.")
            raise StudentManagementError("Unable to write to the JSON file.") from exc
        finally:
            if file_handle is not None:
                file_handle.close()

    def _combined_records(self) -> List[Dict[str, str]]:
        """Return merged CSV and JSON records for display or search."""

        csv_records = {record["reg_no"]: record for record in self._load_csv_records()}
        json_details = self._load_json_details()
        combined: List[Dict[str, str]] = []

        for reg_no in sorted(csv_records):
            merged = {**csv_records[reg_no], **json_details.get(reg_no, {})}
            for field in JSON_FIELDS:
                merged.setdefault(field, "")
            combined.append(merged)

        return combined

    def get_student(self, reg_no: str) -> Dict[str, str]:
        """Find a student by registration number."""

        reg_no = normalize_reg_no(reg_no)
        for record in self._combined_records():
            if record["reg_no"] == reg_no:
                logging.info("Searched for student %s.", reg_no)
                return record

        logging.warning("Student %s was not found.", reg_no)
        raise StudentNotFoundError(f"No student record found for {reg_no}.")

    def add_student(self, student_data: Dict[str, str]) -> Dict[str, str]:
        """Add a new student record to both storage files."""

        reg_no = normalize_reg_no(student_data["reg_no"])
        records = self._load_csv_records()
        details = self._load_json_details()

        if any(record["reg_no"] == reg_no for record in records):
            raise DuplicateRegistrationError(f"Registration number {reg_no} already exists.")

        core_record = {
            "reg_no": reg_no,
            "name": student_data["name"].strip(),
            "age": str(student_data["age"]).strip(),
            "gender": student_data["gender"].strip(),
        }
        detail_record = {
            "reg_no": reg_no,
            "address": student_data["address"].strip(),
            "contact": student_data["contact"].strip(),
            "program": student_data["program"].strip(),
            "email": student_data["email"].strip(),
        }

        records.append(core_record)
        details[reg_no] = detail_record
        self._save_csv_records(records)
        self._save_json_details(details)

        logging.info("Added student %s.", reg_no)
        return {**core_record, **detail_record}

    def update_student(self, reg_no: str, updated_data: Dict[str, str]) -> Dict[str, str]:
        """Update an existing student record."""

        reg_no = normalize_reg_no(reg_no)
        records = self._load_csv_records()
        details = self._load_json_details()

        record = next((item for item in records if item["reg_no"] == reg_no), None)
        if record is None:
            raise StudentNotFoundError(f"No student record found for {reg_no}.")

        detail_record = details.get(
            reg_no,
            {"reg_no": reg_no, "address": "", "contact": "", "program": "", "email": ""},
        )

        record.update(
            {
                "name": updated_data["name"].strip(),
                "age": str(updated_data["age"]).strip(),
                "gender": updated_data["gender"].strip(),
            }
        )
        detail_record.update(
            {
                "address": updated_data["address"].strip(),
                "contact": updated_data["contact"].strip(),
                "program": updated_data["program"].strip(),
                "email": updated_data["email"].strip(),
            }
        )

        details[reg_no] = detail_record
        self._save_csv_records(records)
        self._save_json_details(details)

        logging.info("Updated student %s.", reg_no)
        return {**record, **detail_record}

    def delete_student(self, reg_no: str) -> None:
        """Delete a student from both files."""

        reg_no = normalize_reg_no(reg_no)
        records = self._load_csv_records()
        details = self._load_json_details()

        if not any(record["reg_no"] == reg_no for record in records):
            raise StudentNotFoundError(f"No student record found for {reg_no}.")

        records = [record for record in records if record["reg_no"] != reg_no]
        details.pop(reg_no, None)
        self._save_csv_records(records)
        self._save_json_details(details)

        logging.info("Deleted student %s.", reg_no)

    def view_students(self) -> List[Dict[str, str]]:
        """Display all students in a readable table."""

        records = self._combined_records()
        logging.info("Viewed all student records.")
        return records

    def run_demo(self) -> None:
        """Run a non-interactive demonstration that generates log entries."""

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_dir_path = Path(temp_dir)
            temp_csv = temp_dir_path / "students.csv"
            temp_json = temp_dir_path / "students.json"
            shutil.copy2(self.csv_path, temp_csv)
            shutil.copy2(self.json_path, temp_json)

            demo_system = StudentManagementSystem(temp_csv, temp_json, self.log_path)
            demo_system.view_students()
            demo_system.get_student("S002")
            demo_system.add_student(
                {
                    "reg_no": "S900",
                    "name": "Demo Student",
                    "age": "22",
                    "gender": "Female",
                    "address": "Demo Street",
                    "contact": "+256700009900",
                    "program": "Information Technology",
                    "email": "demo.student@example.com",
                }
            )
            demo_system.update_student(
                "S900",
                {
                    "name": "Demo Student Updated",
                    "age": "23",
                    "gender": "Female",
                    "address": "Demo Avenue",
                    "contact": "+256700009901",
                    "program": "Software Engineering",
                    "email": "demo.updated@example.com",
                },
            )
            demo_system.delete_student("S900")

            try:
                demo_system.get_student("S999")
            except StudentNotFoundError:
                logging.info("Demo handled a missing student lookup correctly.")

    def run(self) -> None:
        """Run the interactive menu-driven program."""

        try:
            while True:
                print("\nStudent Record Management System")
                print("1. Add a new student")
                print("2. View all students")
                print("3. Search for a student by registration number")
                print("4. Update student details")
                print("5. Delete a student record")
                print("0. Exit")

                choice = input("Choose an option: ").strip()

                try:
                    if choice == "1":
                        self._interactive_add_student()
                    elif choice == "2":
                        self._interactive_view_students()
                    elif choice == "3":
                        self._interactive_search_student()
                    elif choice == "4":
                        self._interactive_update_student()
                    elif choice == "5":
                        self._interactive_delete_student()
                    elif choice == "0":
                        print("Goodbye.")
                        break
                    else:
                        print("Please choose a valid menu option.")
                except StudentManagementError as exc:
                    print(f"Error: {exc}")
                    logging.warning("User-facing error: %s", exc)
                except ValueError as exc:
                    print(f"Error: {exc}")
                    logging.warning("Validation error: %s", exc)
                except Exception as exc:
                    print("An unexpected error occurred. Check the log file.")
                    logging.exception("Unexpected application error.")
                    logging.error("Unhandled exception: %s", exc)
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
            logging.info("Program interrupted by user.")
        finally:
            logging.info("Application closed.")

    def _interactive_add_student(self) -> None:
        """Collect input for adding a student."""

        student_data = {
            "reg_no": prompt_required_text("Enter registration number: "),
            "name": prompt_required_text("Enter full name: "),
            "age": prompt_age("Enter age: "),
            "gender": prompt_choice("Enter gender (Male/Female/Other): ", ["male", "female", "other"]),
            "address": prompt_required_text("Enter address: "),
            "contact": prompt_contact("Enter contact number: "),
            "program": prompt_required_text("Enter program: "),
            "email": prompt_email("Enter email address: "),
        }
        added_student = self.add_student(student_data)
        print("Student added successfully.")
        print_student_details(added_student)

    def _interactive_view_students(self) -> None:
        """Display all students from the stored files."""

        records = self.view_students()
        if not records:
            print("No student records found.")
            return

        print_student_table(records)

    def _interactive_search_student(self) -> None:
        """Search for a student and display the merged record."""

        reg_no = prompt_required_text("Enter registration number to search: ")
        student = self.get_student(reg_no)
        print_student_details(student)

    def _interactive_update_student(self) -> None:
        """Update an existing student record."""

        reg_no = prompt_required_text("Enter registration number to update: ")
        existing = self.get_student(reg_no)

        updated_data = {
            "name": prompt_optional_text("Enter full name", existing.get("name", "")),
            "age": prompt_optional_age("Enter age", existing.get("age", "")),
            "gender": prompt_choice(
                "Enter gender (Male/Female/Other)",
                ["male", "female", "other"],
                existing.get("gender", ""),
            ),
            "address": prompt_optional_text("Enter address", existing.get("address", "")),
            "contact": prompt_optional_contact("Enter contact number", existing.get("contact", "")),
            "program": prompt_optional_text("Enter program", existing.get("program", "")),
            "email": prompt_optional_email("Enter email address", existing.get("email", "")),
        }

        updated_student = self.update_student(reg_no, updated_data)
        print("Student updated successfully.")
        print_student_details(updated_student)

    def _interactive_delete_student(self) -> None:
        """Delete a student after user confirmation."""

        reg_no = prompt_required_text("Enter registration number to delete: ")
        student = self.get_student(reg_no)
        print_student_details(student)
        confirm = input("Type YES to delete this student: ").strip().lower()
        if confirm != "yes":
            print("Delete cancelled.")
            logging.info("Delete cancelled for %s.", normalize_reg_no(reg_no))
            return

        self.delete_student(reg_no)
        print("Student deleted successfully.")


def normalize_reg_no(reg_no: str) -> str:
    """Standardize registration numbers for reliable searching."""

    return reg_no.strip().upper()


def prompt_required_text(message: str) -> str:
    """Prompt for a non-empty string."""

    value = input(message).strip()
    if not value:
        raise InvalidStudentDataError("This field cannot be empty.")
    return value


def prompt_optional_text(message: str, current_value: str) -> str:
    """Prompt for text and keep the current value if the input is blank."""

    value = input(f"{message} [{current_value}]: ").strip()
    return value or current_value


def prompt_age(message: str) -> str:
    """Prompt for a valid age."""

    value = input(message).strip()
    if not value.isdigit():
        raise InvalidStudentDataError("Age must be a whole number.")

    age = int(value)
    if age < 1 or age > 120:
        raise InvalidStudentDataError("Age must be between 1 and 120.")

    return str(age)


def prompt_optional_age(message: str, current_value: str) -> str:
    """Prompt for age while allowing the user to keep the current value."""

    value = input(f"{message} [{current_value}]: ").strip()
    if not value:
        return current_value
    if not value.isdigit():
        raise InvalidStudentDataError("Age must be a whole number.")

    age = int(value)
    if age < 1 or age > 120:
        raise InvalidStudentDataError("Age must be between 1 and 120.")

    return str(age)


def prompt_choice(message: str, allowed_values: List[str], current_value: str = "") -> str:
    """Prompt for a value from a fixed list of options."""

    allowed_lookup = {item.lower(): item for item in allowed_values}
    if current_value:
        prompt_message = f"{message} [{current_value}]: "
    else:
        prompt_message = f"{message} "

    value = input(prompt_message).strip()
    if not value and current_value:
        return current_value

    value_lower = value.lower()
    if value_lower not in allowed_lookup:
        raise InvalidStudentDataError(f"Please choose one of: {', '.join(allowed_values)}.")

    return allowed_lookup[value_lower].title()


def prompt_contact(message: str) -> str:
    """Prompt for a phone number or contact value."""

    value = input(message).strip()
    if not value:
        raise InvalidStudentDataError("Contact number cannot be empty.")

    allowed_chars = set("0123456789+ -")
    if any(character not in allowed_chars for character in value):
        raise InvalidStudentDataError("Contact number contains invalid characters.")

    return value


def prompt_optional_contact(message: str, current_value: str) -> str:
    """Prompt for contact information while allowing the current value."""

    value = input(f"{message} [{current_value}]: ").strip()
    if not value:
        return current_value
    allowed_chars = set("0123456789+ -")
    if any(character not in allowed_chars for character in value):
        raise InvalidStudentDataError("Contact number contains invalid characters.")
    return value


def prompt_email(message: str) -> str:
    """Prompt for a simple email address."""

    value = input(message).strip()
    if "@" not in value or "." not in value.split("@")[-1]:
        raise InvalidStudentDataError("Enter a valid email address.")
    return value


def prompt_optional_email(message: str, current_value: str) -> str:
    """Prompt for email while keeping the current value if blank."""

    value = input(f"{message} [{current_value}]: ").strip()
    if not value:
        return current_value
    if "@" not in value or "." not in value.split("@")[-1]:
        raise InvalidStudentDataError("Enter a valid email address.")
    return value


def print_student_details(student: Dict[str, str]) -> None:
    """Print a single student record in a friendly format."""

    print("\nStudent Details")
    print("-" * 40)
    for key, label in DISPLAY_FIELDS:
        print(f"{label:<12}: {student.get(key, '')}")


def print_student_table(records: List[Dict[str, str]]) -> None:
    """Print all student records as a simple table."""

    widths = {field: len(label) for field, label in DISPLAY_FIELDS}
    for record in records:
        for field, label in DISPLAY_FIELDS:
            widths[field] = max(widths[field], len(str(record.get(field, ""))))

    header = " | ".join(label.ljust(widths[field]) for field, label in DISPLAY_FIELDS)
    separator = "-+-".join("-" * widths[field] for field, _ in DISPLAY_FIELDS)
    print("\n" + header)
    print(separator)
    for record in records:
        row = " | ".join(str(record.get(field, "")).ljust(widths[field]) for field, _ in DISPLAY_FIELDS)
        print(row)


def main() -> None:
    """Program entry point."""

    parser = argparse.ArgumentParser(description="Student Record Management System")
    parser.add_argument("--demo", action="store_true", help="Run an automated demonstration")
    args = parser.parse_args()

    configure_logging(LOG_FILE, overwrite=args.demo)
    system = StudentManagementSystem()

    if args.demo:
        system.run_demo()
        print("Demo completed. Check student_system.log for the generated log entries.")
        return

    system.run()


if __name__ == "__main__":
    main()