
from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = "libranexus-secret-key"


# ==============================
# MySQL Database Connection
# ==============================

def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3307,
        user="root",
        password="WPAcs2001",
        database="libranexus"
    )


# ==============================
# Home
# ==============================

@app.route("/")
def home():
    return render_template("index.html")


# ==============================
# Login
# ==============================

@app.route("/login")
def login():
    return render_template("login.html")


# ==============================
# Register
# ==============================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        first_name = request.form["first_name"].strip()
        last_name = request.form["last_name"].strip()
        email = request.form["email"].strip()
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        # Check password match
        if password != confirm_password:
            flash("Passwords do not match.", "error")
            return redirect(url_for("register"))

        # Combine first name and last name
        full_name = f"{first_name} {last_name}"

        # Hash password before storing
        hashed_password = generate_password_hash(password)

        connection = get_db_connection()
        cursor = connection.cursor()

        try:
            query = """
                INSERT INTO users
                (full_name, email, password)
                VALUES (%s, %s, %s)
            """

            cursor.execute(
                query,
                (full_name, email, hashed_password)
            )

            connection.commit()

            flash(
                "Account created successfully! Please log in.",
                "success"
            )

            return redirect(url_for("login"))

        except mysql.connector.IntegrityError:

            flash(
                "This email is already registered.",
                "error"
            )

            return redirect(url_for("register"))

        finally:
            cursor.close()
            connection.close()

    return render_template("register.html")


# ==============================
# Books
# ==============================

@app.route("/books")
def books():
    return render_template("books.html")


# ==============================
# Dashboard
# ==============================

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ==============================
# Borrowed Books
# ==============================

@app.route("/borrowed-books")
def borrowed_books():
    return render_template("borrowed-books.html")


# ==============================
# Run Application
# ==============================

if __name__ == "__main__":
    app.run(debug=True)

