#write a python script that performs file organisation of your download folder
#code logic for file automation

from pathlib import Path
import shutil


# Get the Downloads folder using pathlib
download_folder = Path.home() / "Downloads"


# File categories
file_types = {

    "Images": [".jpg", ".jpeg", ".png", ".gif"],

    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],

    "Videos": [".mp4", ".mkv", ".avi"],

    "Music": [".mp3", ".wav"],

    "Programs": [".exe", ".msi"]

}


# Function to identify file category
def get_category(extension):

    for folder, extensions in file_types.items():

        if extension.lower() in extensions:
            return folder

    return "Others"



# Loop through files in Downloads
for file in download_folder.iterdir():

    # Ignore folders
    if file.is_dir():
        continue


    # Get file extension
    extension = file.suffix


    # Find correct category
    category = get_category(extension)


    # Create destination folder
    destination_folder = download_folder / category


    # Create folder if it does not exist
    destination_folder.mkdir(exist_ok=True)


    # Move file
    shutil.move(
        str(file),
        str(destination_folder / file.name)
    )


print("Downloads folder organized successfully!")