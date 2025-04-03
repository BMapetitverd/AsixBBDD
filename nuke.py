import mysql.connector
import random

connection = mysql.connector.connect(
    host="localhost",
    user="admin",      # MySQL user
    password="Curs202425",      # user's password
    database="classicmodels"
)

connectionBM = mysql.connector.connect(
    host="localhost",
    user="admin",      # MySQL user
    password="Curs202425",      # user's password
    database="borjaMoll"
)

cursor = connection.cursor()
cursorBM = connectionBM.cursor()

cursorBM.execute("USE borjaMoll")

cursor.execute("SELECT customerNumber, contactFirstName, contactLastName FROM Customers")

"""
for customer in cursor.fetchall():
    cursorBM.execute("INSERT INTO Students (Id, name, lastName) Values(%s,%s,%s)",(customer[0],customer[1],customer[2]))
"""
studentsToInsert = []
for customer in cursor.fetchall():
    studentsToInsert.append((customer[0], customer[1], customer[2], random.randrange(18, 41)))

cursorBM.executemany("INSERT INTO Students (Id, name, lastName, age) Values(%s,%s,%s,%s)",studentsToInsert)
#connectionBM.commit()
