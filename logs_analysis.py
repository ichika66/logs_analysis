# logs_analysis.py
#
import re
import psycopg2
""" Connect to the PostgreSQL database. Returns a database connection. """

query1 = (
	"select articles.title, count(*) as view "
	"from articles inner join log on log.path "
	"like concat ('%', articles.slug, '%') "
	"group by articles.title, log.path "
	"order by view desc limit 3;"
	)

def connect(database_name="news"):
	try:
		db = psycopg2.connect("dbname={}".format(database_name))
		cursor = db.cursor()
		return db, cursor
	except:
		print("Error establishing a database connection")

def GetResult(query):
	"""Get the query result from the DB"""
	db, cursor = connect()
	cursor.execute(query)
	titles = cursor.fetchall()
	db.close
	return titles


def Popular3Article():
	""" Print out the most popular article of all times. """
	db, cursor = connect()
	cursor.execute("SELECT path, count(id) AS view FROM log WHERE path LIKE '/article/%' GROUP BY path ORDER BY view DESC LIMIT 3;")
	rows = cursor.fetchall()
	row = []
	ls = []
	for r in rows:
		ls = r[0]
		ls = re.sub('/article/', '', ls)
		ls = "'" + ls + "'"
		query = ("SELECT title from articles where slug = " + str(ls))
		#get the title from articles table
		cursor.execute(query)
		title = cursor.fetchone()
		title = title + (r[1],)  # add a view count to title tuple
		row.append(title)
	# 	row.append(ls)
	# cursor.execute("SELECT articles.title, count(log.path) AS view FROM articles, log WHERE articles.slug = " + str(row[0]) + "OR articles.slug = " + str(row[1]) + "OR articles.slug = " + str(row[2]) + "GROUP BY articles.title ORDER BY view desc")
	# top3 = cursor.fetchall()
	db.close();
	return row


def PopularAuthor():
	db, cursor = connect()

	query = ("select path, count(path) as view from log where path like '/article/%'  group by path order by view desc limit 8;")
	#query = ("select articles.title, authors.name from articles, authors where articles.author = authors.id")
	cursor.execute(query)
	author = cursor.fetchall()
	db.close()
	return author

print Popular3Article()
print PopularAuthor()
print GetResult(query1)
