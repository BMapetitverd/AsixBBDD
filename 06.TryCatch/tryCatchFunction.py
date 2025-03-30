#Use pip install mysql-connector-python if you don't have this package installed
import mysql.connector

def insert_customer(cNumber, cName, creditLimit):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="admin",      # MySQL user
            password="Curs202425",      # user's password
            database="classicmodels"
        )
        
        cursor = connection.cursor()
        sql = "INSERT INTO Customers (customerNumber, customerName, creditLimit) VALUES (%s, %s, %s)"
        cursor.execute(sql, (cNumber, cName, creditLimit))
        connection.commit()
        print("Customer created")
    except mysql.connector.IntegrityError:
        print("Error: The customer number already exists or there is an integrity issue")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        connection.close()

# Ejemplo de uso:
insert_customer(506, "Pep Gonella", 230000)