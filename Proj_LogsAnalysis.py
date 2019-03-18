#!/usr/bin/env python3

'''
Assignment: Logs Analysis for news
'''

import psycopg2
import datetime


try:
    db = psycopg2.connect("dbname=news")
except psycopg2.Error as e:
    print("Unable to connect to the database")
    print(e.pgerror)
    print(e.diag.message_detail)
    sys.exit(1)

task = db.cursor()

# statis views of article
task.execute("create view mostreads as\
                select split_part(path, '/', 3) as article,\
                 count(*) as n from log\
                 group by article\
                 order by n desc;")
# statis report for connection
task.execute("create view errorReport as\
                select date(time) as date,\
                count(*) as errors from log where not status='200 OK'\
                group by date;")
task.execute("create view connReport as\
                select date(time) as date,\
                count(*) as conn from log\
                group by date;")

# Task 1
task.execute("create view mostreadarticle as\
                select title, n, author from articles, mostreads\
                where slug=article order by n desc;")
print('1. What are the most popular three articles of all time?')
task.execute("select * from mostreadarticle limit 3;")
t1 = task.fetchall()
for i in t1:
    print('\"{}\" - {} views'.format(i[0], i[1]))

# Task 2
task.execute("select name, m from authors, \
                (select author, sum(n) as m \
                    from mostreadarticle group by author) \
                    as totalviews\
                where author=authors.id\
                order by m desc;")
print('\n2. Who are the most popular article authors of all time?')
t2 = task.fetchall()
for i in t2:
    print('{} - {} views'.format(i[0], i[1]))

# Task 3
task.execute("create view errrate as\
                select errorReport.date, (1.0*errors/conn) as ratio\
                from errorReport join connReport \
                on errorReport.date=connReport.date;")
'''
I have a little trouble here, I tried to use "having" to filter the data
but it said ratio is not here, so I have to do it again.
'''
task.execute("select * from errrate where ratio>0.01;")
print('\n3. On which days did more than 1% of requests lead to errors?')
t3 = task.fetchall()
for i in t3:
    print('{} - {:.1f}%errors'.format(i[0].strftime("%b %d, %Y"), i[1]*100))

db.close()
