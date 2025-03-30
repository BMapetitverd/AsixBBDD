#Use pip install mysql-connector-python if you don't have this package installed
import mysql.connector

search_name = input("Write the customer name: ")

# Connection to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="admin",      # MySQL user
    password="Curs202425",      # user's password
    database="classicmodels"
)
cursor = connection.cursor()

cursor.execute("SELECT * FROM Customers WHERE customerName = %s", (search_name,))
# We only want the first customer
result = cursor.fetchone()

if result:
    print("Data found:", result)
else:
    print("Customer not found.")

connection.close()