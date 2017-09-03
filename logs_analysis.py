# logs_analysis.py
#
import re
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
	cursor.execute("SELECT path, count(id) AS view FROM log WHERE path LIKE '/article/%' GROUP BY path ORDER BY view DESC LIMIT 3;")
	rows = cursor.fetchall()
	db.close();
	row = []
	string = ''
	for r in rows:
		string = str(r)
		string = re.sub('/article/', '', string)
		row.append(string)
	#		row.append(r)
	return row

	# select path, count(id) as view from log group by path order by view desc limit 10;
print PopularArticle()