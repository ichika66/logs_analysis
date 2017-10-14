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

query2 = (
	"select authors.name, count(*) as view "
	"from authors inner join articles "
	"on articles.author = authors.id "
	"inner join log on log.path "
	"like concat ('%', articles.slug, '%') "
	"group by authors.name "
	"order by view desc; "
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

print GetResult(query1)
print GetResult(query2)
