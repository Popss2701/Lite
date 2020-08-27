import csv
import mysql.connector as mysql

try:
	db = mysql.connect(host='localhost', user='root', password='', database='lite')
except:
	db = mysql.connect(host='localhost', user='root', password='')
	cursor = db.cursor()
	cursor.execute('CREATE DATABASE lite')

db = mysql.connect(host='localhost', user='root', password='', database='lite')
cursor = db.cursor()
try:
	cursor.execute('CREATE TABLE Customers (id  INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY)')
except:
	pass
with open('customer.csv') as cvs_file:
	csv_reader = csv.reader(cvs_file)
	fields = next(csv_reader)
	try:
		for item in fields:
			cursor.execute('ALTER TABLE Customers ADD %s VARCHAR(255)' % (item))
	except:
		pass
	query = 'INSERT INTO customers ({0}) VALUES {1}'
	for data in csv_reader:
		data = tuple(data)
		cursor.execute(query.format(','.join(fields), tuple(data)))
		db.commit()

cursor.execute("ALTER TABLE customers DROP id")
