#! /usr/bin/python -v
import psycopg2


def logs_analysis():
    global c
    print('Welcome to my first project \"Logs Analysis\"')
    try:
        db = psycopg2.connect("dbname=news")
        c = db.cursor()
        #
        # Most viewed articles query
        #
        query1 = '''select articles.title, count(log.path) as views
        from log join articles on substring(log.path,10) = articles.slug
        group by articles.title, log.status
        having log.status='200 OK'
        order by views desc limit 3;'''
        c.execute(query1)
        pop_art = c.fetchall()
        print
        print "A.1"
        print "Most popular three articles of all time are:"
        for x in pop_art:
            print "  ", x[0], '__', x[1], 'views'
        #
        # Top 3 famous authors query
        #
        query2 = '''select authors.name, count(log.path) as views
        from log join (articles join authors on articles.author = authors.id)
        on substring(log.path,10) = articles.slug
        group by substring(log.path,10), authors.name, log.status
        having log.status='200 OK'
        order by views desc limit 3;'''
        c.execute(query2)
        pop_auth = c.fetchall()
        print
        print "A.2"
        print "Most popular authors are:"
        for x in pop_auth:
            print "  ", x[0], '__', x[1], 'views'
        #
        # 404 status percentage query
        #
        query3 = '''select days, round(bad_percent,1)
        from (select to_char((log.time)::date, 'Month dd, yyyy') as days,
        (sum(case when status = '404 NOT FOUND' then 1 else 0 end) * 100)
        ::numeric / count(status) as bad_percent
        from log
        group by days
        order by bad_percent desc) as final
        where bad_percent > 1;'''
        c.execute(query3)
        num_error = c.fetchall()
        print
        print "A.3"
        print "Days that more than '1%' of requests lead to errors:"
        for x in num_error:
            print "  ", x[0], '__', x[1], '%', 'errors'
    finally:
        c.close()


logs_analysis()
