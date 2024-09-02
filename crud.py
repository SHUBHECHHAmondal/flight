import mysql.connector

try:
    # Establish connection to the database
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='shubhechha21',
        database='indigo'
    )
    mycursor = conn.cursor()
    print('Connection established')
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit(1)

try:
    # Uncomment these sections if needed to create the database and table
    # mycursor.execute("CREATE DATABASE indigo")
    # conn.commit()

    # Uncomment to create the table
    # mycursor.execute("""
    # CREATE TABLE airport(
    #     airport_id INTEGER PRIMARY KEY,
    #     code VARCHAR(10) NOT NULL,
    #     city VARCHAR(50) NOT NULL,
    #     name VARCHAR(255) NOT NULL
    # )
    # """)
    # conn.commit()

    # Uncomment to insert data into the table
    # mycursor.execute("""
    # INSERT INTO airport (airport_id, code, city, name) VALUES
    # (1, 'DEL', 'New Delhi', 'IGIA'),
    # (2, 'CCU', 'Kolkata', 'NSCA'),
    # (3, 'BOM', 'Mumbai', 'CSMA')
    # """)
    # conn.commit()

    # Retrieve data
    mycursor.execute("SELECT * FROM airport WHERE airport_id > 1")
    data = mycursor.fetchall()
    print("Retrieved data:", data)

    for i in data:
        print("Airport Name:", i[3])

    # Update data
    mycursor.execute("""
    UPDATE airport
    SET name = 'Bombay'
    WHERE airport_id = 3
    """)
    conn.commit()

    # Check updated data
    mycursor.execute("SELECT * FROM airport")
    data = mycursor.fetchall()
    print("Data after update:", data)

    # Delete data
    mycursor.execute("DELETE FROM airport WHERE airport_id = 3")
    conn.commit()

    # Check data after deletion
    mycursor.execute("SELECT * FROM airport")
    data = mycursor.fetchall()
    print("Data after deletion:", data)

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Clean up the connection and cursor
    if mycursor:
        mycursor.close()
    if conn.is_connected():
        conn.close()
        print('Connection closed')
