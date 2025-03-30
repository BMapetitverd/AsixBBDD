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

# Insert customers
customers = [
    (497,"Ana García", 20),
    (498,"Javier Martínez", 22),
    (499,"Marta López", 19),
    (500,"Carlos Ruiz", 21),
    (501,"Sofía Pérez", 20)
]

# Insert the data
sql = "INSERT INTO Customers (customerNumber, customerName, creditLimit) VALUES (%s, %s, %s)"
cursor.executemany(sql, customers)

# It's mandatory to commit every time a DML operation is performed
connection.commit()

connection.close()