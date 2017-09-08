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
	#db.close();
	row = []
	ls = []
	title = ''
	dictionary = dict(rows)
	#for r in rows:
	for r in rows:
		#ls = r[0]  # get one element from tuple
		ls = r[0]
		ls = re.sub('/article/', '', ls)
		#newls = re.sub('/article/', '', ls)  # delete article from path
		#dictionary[newls] = dictionary.pop(ls)
		#row.append(ls)  # append the row list
		ls = "'" + ls + "'"
		#print ls
		query = ("SELECT title from articles where slug = " + str(ls))
		# get the title from articles table
		cursor.execute(query)
		title = cursor.fetchone()
		#print title
		title = title + (r[1],)  # add a view count to title tuple
		#print r[1]
		#title = title + r[1]
		row.append(title)
		#r[0] = title
		#row.append(row)
	#dictionary = dict(rows)
	#print dictionary
	db.close();
	return row
	#return GetTitle(row)

# def GetTitle(row):
# 	""" get title from articles table which path is same as slug """
# 	title = []  # list to store titles
# 	db, cursor = connect()
# 	cursor.execute("SELECT slug, title FROM articles;")
# 	title = cursor.fetchall()
# 	db.close();

# 	dictionary = dict(title)  # change tuple to dictionary
# 	top3 = []  # list of top three titles
# 	for r in row:
# 		if dictionary[r]:
# 			top3.append(dictionary[r])

# 	return top3

# def Top3Articles():
# 	""" returns the top 3 popular articl from the database """


print PopularArticle()

