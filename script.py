#!/usr/bin/env python3

# load modules
import psycopg2
from datetime import datetime 

# file settings
filepath = '/data/'
filename = datetime.now().strftime("%Y-%m-%d") + ".csv"

# postgres access
hostname = '172.64.0.5'
username = 'postgres'
password = 'postgres'
database = 'postgres'

# establish connection
conn = psycopg2.connect( 
    host=hostname, 
    user=username, 
    password=password, 
    dbname=database )

# open cursor an run query
sqlquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(
    "SELECT id, lali, hiha, nono -> 'mymoney' as mycol FROM myschema.mytable")

with open(filepath + filename, "w") as fptr:
    cur = conn.cursor()
    cur.copy_expert(sqlquery, fptr)
    conn.commit()
    cur.close()

# process query result
#cur = conn.cursor()
#sqlquery = "SELECT id, lali, hiha, nono -> 'mymoney' as mycol FROM myschema.mytable"
#cur.execute(sqlquery)
#for row in cur.fetchall():
#    print(row)
#cur.close()

# close connection
conn.close()
