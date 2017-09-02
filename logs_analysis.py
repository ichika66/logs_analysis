# logs_analysis.py
#

import psycopg2
""" Connect to the PostgreSQL database. Returns a database connection. """
def connect(database_name="news"):
	try:
		db = psycopg2.connect("dbname={}".format(database_name))
		cursor = db.cursor()
		return db, cursor
	except:
		print("Error establishing a database connection")

def PopularArticle():
	""" Print out the most popular article of all times. """
	db, cursor = connect()
	cursor.execute("SELECT path, COUNT(id) AS view FROM log GROUP BY path ORDER BY view DESC LIMIT 10;")
	rows = cursor.fetchall()
	db.close();
	return rows

	# select path, count(id) as view from log group by path order by view desc limit 10;
PopularArticle()