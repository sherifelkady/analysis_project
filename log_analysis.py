#!/usr/bin/env python3


import psycopg2

DBNAME = "news"

# What are the most popular three articles of all time


def top_articles():
    try:
        conn = psycopg2.connect(database=DBNAME)
    except psycopg2.Error as e:
        print ("No Connection")
        print (e.pgerror)
    else:
        c = conn.cursor()
        c.execute("""select title ,count(*) AS view
        FROM articles join log on articles.slug = substring(log.path,10)
        GROUP BY title ORDER BY view desc limit 3
        """)
        results = c.fetchall()
    finally:
        conn.close()
    return results

# Who are the most popular article authors of all time


def top_author():
    try:
        conn = psycopg2.connect(database=DBNAME)
    except psycopg2.Error as e:
        print("No Connection")
        print(e.pgerror)
    else:
        c = conn.cursor()
        c.execute("""SELECT name , count(*) AS view
        FROM authors join articles on authors.id = articles.author
        join log on articles.slug = substring(log.path,10)
        GROUP BY authors.name ORDER BY view desc
        """)
        results = c.fetchall()
    finally:
        conn.close()
    return results

# On which days did more than 1% of requests lead to errors


def get_errors():
    try:
        conn = psycopg2.connect(database=DBNAME)
    except psycopg2.Error as e:
        print("No Connection")
        print(e.pgerror)
    else:
        c = conn.cursor()
        c.execute("""SELECT * FROM error_per
        WHERE error_per.percentage > 1 ORDER BY
        ROUND(error_per.percentage,-4) DESC
        """)
        results = c.fetchall()
    finally:
        conn.close()
    return results

question_1 = top_articles()
question_2 = top_author()
question_3 = get_errors()


# Print Results


def print_res(res):
    for record in res:
        title = record[0]
        view = record[1]
        print("\t" + "%s - %d" % (title, view) + " views")
    print(" ################################################ ")

print (" What are the most popular three articles of all time ")
print_res(question_1)

print (" Who are the most popular article authors of all time ")
print_res(question_2)

print (" On which days did more than 1 percentage of requests lead to errors ")
for record in question_3:
    print("\t" + str(record[0]) + " : " + str(record[1]) + " %")
