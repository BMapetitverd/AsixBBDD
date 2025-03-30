#Use pip install mysql-connector-python if you don't have this package installed
import mysql.connector

# Conexión a MySQL (ajusta user, password y host según tu configuración)
conexion = mysql.connector.connect(
    host="localhost",
    user="admin",      # Usuario de MySQL
    password="Curs202425",      # Contraseña (vacía por defecto en XAMPP/WAMP)
    database="classicmodels"
)

cursor = conexion.cursor()

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
    print(customer[1])

conexion.close()