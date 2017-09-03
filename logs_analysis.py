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
	return GetTitle(row)

def GetTitle(row):
	""" get title from articles table which path is same as slug """
	title = []
	t = []
	db, cursor = connect()
	cursor.execute("SELECT slug, title FROM articles;")
	title = cursor.fetchall()
	db.close();

	title = dict(title)
	ti = []
	for r in row:
		if title[r]:
			ti.append(title[r])

	return ti

print PopularArticle()
#print GetTitle()

