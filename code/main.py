#!/usr/bin/env python3

# load modules
import psycopg2
from config import Config
import sys
from datetime import datetime 

# file settings
filepath = '/data/'
filename = datetime.now().strftime("%Y-%m-%d %H-%M") + ".csv"

# postgres access
cfg = Config(open(sys.path[0] + '/.credentials'))
#cfg = Config(open(sys.path[0] + '/.credentials-onhost'))

# establish connection
conn = psycopg2.connect(**cfg)

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
