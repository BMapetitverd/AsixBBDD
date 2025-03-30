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

# Select and show all the customers
cursor.execute("SELECT * FROM Customers")
print("All the customers:")
for customer in cursor.fetchall():
    print(customer)

# Select and show all the customers with a creditLimit greater than 100.000
cursor.execute("SELECT customerNumber, customerName, creditLimit FROM Customers WHERE creditLimit > 100000")
print("\nCustomers with more than 100000:")
for customer in cursor.fetchall():
    print(customer)
    # Print the customer name
    print(customer[1])

connection.close()