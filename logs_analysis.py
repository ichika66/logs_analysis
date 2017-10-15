#!/usr/bin/env python
# logs_analysis.py
import psycopg2

# title strings
title1 = "\n1. What are the most popular three articles of all time?\n"
title2 = "\n2. Who are the most popular article authors of all time?\n "
title3 = "\n3. On which days did more than 1% of requests lead to errors?\n"

# Most poular three articles
query1 = (
    "select articles.title, count(*) as view "
    "from articles inner join log on log.path "
    "= concat('/article/', articles.slug) "
    "group by articles.title, log.path "
    "order by view desc limit 3;"
    )

# most popular authors
query2 = (
    "select authors.name, count(*) as view "
    "from authors inner join articles "
    "on articles.author = authors.id "
    "inner join log on log.path "
    "= concat('/article/', articles.slug) "
    "group by authors.name "
    "order by view desc; "
    )

# error logs more than 1% per day
query3 = (
    "select * from load_error where error >= 1;"
    )


def connect(database_name="news"):
    """ Connect to the PostgreSQL database. Returns a database connection. """
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except Exception:
        print("Error establishing a database connection")


def GetResult(query):
    """ Get the query result from the DB """
    db, cursor = connect()
    cursor.execute(query)
    result = cursor.fetchall()
    db.close
    return result


def PrintViews(title, result):
    """ Print the title and result of the query1 & 2 """
    result = list(result)
    print title
    for r in result:
        print('  ' + str(r[0]) + ' - ' + str(r[1]) + ' views')


def PrintErrors(title, result):
    """ Print the title and result of the query3 """
    result = list(result)
    print title
    for r in result:
        print('  ' + str(r[0]) + ' - ' + str(r[1]) + '% errors')


# Define result of each queries
Report1 = GetResult(query1)
Report2 = GetResult(query2)
Report3 = GetResult(query3)

# Print all reports
PrintViews(title1, Report1)
PrintViews(title2, Report2)
PrintErrors(title3, Report3)
