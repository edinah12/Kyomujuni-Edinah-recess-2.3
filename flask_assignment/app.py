from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = "assignment-secret-key"

# Demo credentials for assignment purposes.
VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not username or not password:
            flash("Please enter both username and password.", "error")
            return render_template("login.html")

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            session["username"] = username
            return redirect(url_for("dashboard"))

        flash("Invalid username or password.", "error")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    username = session.get("username")
    if not username:
        flash("Please log in first.", "error")
        return redirect(url_for("login"))
    return render_template("dashboard.html", username=username)


@app.route("/logout")
def logout():
    session.pop("username", None)
    flash("You have been logged out.", "success")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
