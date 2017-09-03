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
	ls = []
	for r in rows:
		ls = r[0]  # get one element from tuple
		ls = re.sub('/article/', '', ls)  # delete article from path
		row.append(ls)  # append the row list
	#return row
	#GetTitle(row)

def GetTitle():
	""" get title from articles table which path is same as slug """
	title = []
	t = []
	db, cursor = connect()
	#for r in row:
	#query = "SELECT title FROM articles WHERE slug = %s;" % row[0]
	#query = "SELECT title FROM articles WHERE slug = 'candidate-is-jerk';"
	cursor.execute("SELECT title FROM articles WHERE slug = 'candidate-is-jerk';")
	title = cursor.fetchall()
	db.close();
	#title.append(t)

	return title

print PopularArticle()
print GetTitle()

