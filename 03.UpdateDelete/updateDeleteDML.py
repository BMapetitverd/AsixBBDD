#Use pip install mysql-connector-python if you don't have this package installed
import mysql.connector

# Connection to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="admin",      # MySQL user
    password="Curs202425",      # user's password
    database="classicmodels"
)

cursor = connection.cursor()

cursor.executemany("UPDATE Customers (customerName, creditLimit) VALUES ('Adrian Petit', 2000000) WHERE customerNumber = 500")

cursor.executemany("DELETE FROM Customers WHERE customerNumber = 500")

# It's mandatory to commit every time a DML operation is performed
connection.commit()
connection.close()