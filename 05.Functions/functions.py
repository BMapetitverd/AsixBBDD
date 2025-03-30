#Use pip install mysql-connector-python if you don't have this package installed
import mysql.connector

def insert_customer(cNumber, cName, creditLimit):
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
    connection.close()
    print("Customer created")

# Ejemplo de uso:
insert_customer(506, "Pep Gonella", 230000)