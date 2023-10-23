import bcrypt
import sqlite3
import secrets

sample_license_key = secrets.token_hex(16)
sample_license_info = "This is the license information for the sample user."

def auth():
    # Connect to the SQLite database
    conn = sqlite3.connect("your_database.db")
    cur = conn.cursor()

    # Drop the Users table if it already exists
    cur.execute("DROP TABLE IF EXISTS Users")

    # Create the Users table with the necessary columns
    cur.execute("CREATE TABLE Users (username TEXT, password_hash TEXT, license_key TEXT, license_info TEXT)")

    # Check if the sample user already exists in the database
    cur.execute("SELECT username FROM Users WHERE username=?", ("sample_user",))
    result = cur.fetchone()

    if not result:
        # Generate a random license key and license info

        # Hash the sample password
        sample_password = "password123"
        password_hash = bcrypt.hashpw(sample_password.encode("utf-8"), bcrypt.gensalt())

        # Insert the sample username, password hash, license key, and license info into the Users table
        cur.execute("INSERT INTO Users (username, password_hash, license_key, license_info) VALUES (?, ?, ?, ?)", ("sample_user", password_hash, sample_license_key, sample_license_info))
        conn.commit()
        print("Sample user added to the database.")
        # print("License Key:", sample_license_key)
        print("Please remember to keep your password secure.")

    # Prompt the user to enter the username and password
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Retrieve the password hash and license info from the database based on the entered username
    cur.execute("SELECT password_hash, license_info FROM Users WHERE username=?", (username,))
    result = cur.fetchone()

    if result:
        stored_password_hash, license_info = result

        # Hash the entered password and compare it with the stored password hash
        entered_password_hash = bcrypt.hashpw(password.encode("utf-8"), stored_password_hash.encode("utf-8"))
        if entered_password_hash == stored_password_hash:
            print("Password is valid. User is authenticated.")
            print("License Information:")
            print(license_info)
        else:
            print("Invalid password")
    else:
        print("Invalid username")

    # Close the connection to the database
    conn.close()

auth()