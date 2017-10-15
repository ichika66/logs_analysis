# logs_analysis.py
#
import re
import psycopg2
""" Connect to the PostgreSQL database. Returns a database connection. """

title1 = "1. What are the most popular three articles of all time?"
title2 = "2. Who are the most popular article authors of all time? "
title3 = "3. On which days did more than 1% of requests lead to errors?"

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

def PrintViews(title, result):
	result = list(result)
	print title
	for r in result:
		print (str(r[0]) + ' - ' + str(r[1]) + ' views')

#print GetResult(query1)
#print GetResult(query2)
#print GetResult(query3)
PopArt3 = GetResult(query1)
PopAut = GetResult(query2)

PrintViews(title1, PopArt3)
PrintViews(title2, PopAut)
