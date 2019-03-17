#!/usr/bin/env python2.7

import psycopg2
import datetime as dt
import collections


def return_query(query):
    '''
    Takes a query string, queries the news database, and returns the results.
    '''
    connection = psycopg2.connect('dbname=news')

    cursor = connection.cursor()

    cursor.execute(query)

    result = cursor.fetchall()

    connection.close

    return result


def Q1_response():
    '''
    Q1: What are the three most popular articles of all time
    => Prints DB/Log analysis based response on console
    '''

    print("Q1: What are the three most popular articles of all time?\n")

    query = "SELECT articles.title, count(articles.title) 						\
            FROM articles, log 												\
            WHERE log.path like CONCAT('%',articles.slug,'%')					\
                AND log.status not like '%404%' 									\
            GROUP BY articles.title												\
            ORDER BY count desc 												\
            LIMIT 3;"

    results = return_query(query)

    for title, hits in results:
        print('"{}" -- {:,} views'.format(title, hits))

    print("\n")


def Q2_response():
    '''
    Q2: Who are the most popular article authors of all time?
    => Prints DB/Log analysis based response on console
    '''
    print("Q2: Who are the most popular article authors of all time?\n")

    query = "SELECT authors.name, count(authors.name) 							\
            FROM articles, log, authors 										\
            WHERE log.path like CONCAT('%',articles.slug,'%') 					\
                AND log.status not like '%404%' 								\
                AND articles.author = authors.id 								\
            GROUP BY authors.name 												\
            ORDER BY count desc;"

    results = return_query(query)

    index = 1
    for author, hits in results:
        print('{}. {} -- {:,} views'.format(index, author, hits))
        index += 1

    print("\n")


def Q3_response():
    '''
    Q3. On which days did more than 1% of requests lead to errors?
    => Prints DB/Log Analysis based response on console
    '''
    print("Q3: On which days did more than 1% of requests lead to errors?\n")

    query = "SELECT to_char(log.time,'mm/dd/yyyy') as day, 								\
                log.status, count(log.status)\
            FROM log 																	\
            GROUP BY day, status 														\
            ORDER BY day;"

    results = return_query(query)

    ok_status_by_date = {}
    err_status_by_date = {}
    err_rate_by_date = {}

    for day, status, count in results:
        if day not in err_rate_by_date:
            err_rate_by_date[day] = 0

        if status.startswith('200'):
            ok_status_by_date[day] = float(count)
        if status.startswith('404'):
            err_status_by_date[day] = float(count)

    ordered_err_rate = collections.OrderedDict(
                            sorted(err_rate_by_date.items()))

    for day in ordered_err_rate:
        total = ok_status_by_date[day] + err_status_by_date[day]
        ordered_err_rate[day] = (err_status_by_date[day] / total) * 100
        if ordered_err_rate[day] > 1:
            formatted_date = dt.datetime.strptime(day, "%m/%d/%Y")
            print("{:%B %d, %Y} -- {:.2f}% errors".format(
                        formatted_date, ordered_err_rate[day]))


# Q1: What are the three most popular articles of all time
Q1_response()

# Q2: Who are the most popular article authors of all time?
Q2_response()

# Q3: On which days did more than 1% of requests lead to errors?
Q3_response()
