import mysql.connector
from mysql.connector import Error

def crear_base_datos():
    # 1. Connect to your MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="admin",      # MySQL user
        password="Curs202425",
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # 2. Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS borjaMoll")
        print("Database created")

        # 3. Select database
        cursor.execute("USE borjaMoll")

        # 4. Crear a table
        cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
                            id INT PRIMARY KEY,
                            name VARCHAR(50),
                            lastName VARCHAR(50),
                            age INT)''')
        print("Table created")

        cursor.close()
        connection.close()

# Call the function
crear_base_datos()