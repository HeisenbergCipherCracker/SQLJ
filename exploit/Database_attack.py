import mysql.connector


def Host_ip_address(Ip,UserN,PasswordN,DB,AUTH):

    # Connect to the database
    conn = mysql.connector.connect(
        host="localhost",
        user="username",
        password="password",
        database="dbname",
        auth_plugin='mysql_native_password'
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Prepare the SQL statement with placeholders
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    values = ("john", "password123")

    # Execute the query with the provided values
    cursor.execute(query, values)

    # Commit the changes to the database
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()