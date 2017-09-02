# logs_analysis.py
#

import psycopg2
""" Connect to the PostgreSQL database. Returns a database connection. """
def connect(database_name="newsdata"):
	try:
		db = psycopg2.connect("dbname={}".format(database_name))
		cursor = db.cursor
		return db, cursor
	except:
		print("Error establishing a database connection")
