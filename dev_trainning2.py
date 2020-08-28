import csv
import mysql.connector as mysql

db = mysql.connect(host='localhost', user='root', password='', database='lite')
cursor = db.cursor()

with open('customer.csv') as cvs_file:
	csv_reader = csv.reader(cvs_file)
	fields = next(csv_reader)
	try:
		query = 'CREATE TABLE Customers ({0})'
		cursor.execute(query.format(' VARCHAR(255),'.join(fields)+' VARCHAR(255)'))
	except:
		pass
	query = 'INSERT INTO customers ({0}) VALUES {1}'
	for data in csv_reader:
		cursor.execute(query.format(','.join(fields), tuple(data)))
		db.commit()

