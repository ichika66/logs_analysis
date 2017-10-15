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

query3 = (
	"select * from load_error where error >= 1;"
	)

"""
create view error_count as select cast(time as date), count(*) as error from log where status not like '%200%' group by cast(time as date) order by cast (time as date) desc;
"""
"""
create view log_status as select cast(time as date), count(*) as error from log group by cast(time as date) order by cast(time as date) desc;
"""
#select log_status.time, round(((error_count.error * 100.) / log_status.error), 1) as error from log_status, error_count where log_status.time = error_count.time order by log_status.time asc;

"""
create view load_error as select log_status.time, round(((error_count.error * 100.) / log_status.error), 1) as error from log_status, error_count where log_status.time = error_count.time order by log_status.time asc;
"""


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

def PrintViews(result):
	for r in result:
		print r

#print GetResult(query1)
#print GetResult(query2)
#print GetResult(query3)
PopArt3 = GetResult(query1)
PrintViews(PopArt3)
