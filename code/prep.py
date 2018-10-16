#!/usr/bin/env python3

# load modules
import psycopg2
from config import Config
import sys

# postgres access
cfg = Config(open(sys.path[0] + '/.credentials'))
#cfg = Config(open(sys.path[0] + '/.credentials-onhost'))

# establish connection
conn = psycopg2.connect(**cfg)

# open cursors
cur = conn.cursor()

# create extensions, schema, tables
cur.execute("CREATE EXTENSION IF NOT EXISTS hstore;")

cur.execute("CREATE SCHEMA IF NOT EXISTS myschema;")

sql3 = """
CREATE TABLE IF NOT EXISTS myschema.mytable (
    id    BIGSERIAL PRIMARY KEY,
    lali  VARCHAR(123) NOT NULL,
    hiha  NUMERIC(5,2),
    nono  hstore  
);"""
cur.execute(sql3)


# insert demo data
sql4 = ("""
    INSERT INTO myschema.mytable (lali) VALUES 
    ('cool stuff');
    """,
    """
    INSERT INTO myschema.mytable (lali, hiha) VALUES
    ('with a number (check the rounding)', 123.456);
    """,
    """
    INSERT INTO myschema.mytable (lali, nono) VALUES
    ('some unstructured nosql-ish hstore', '
        "thisis" => "key-value item", 
        "beaware" => "hstore does not allow sub-arrays like json",
        "mymoney" => "987.65" 
    ');
    """)

# insert if the table is empty
cur.execute("select count(id) from myschema.mytable;")
rows = cur.fetchall()

if rows[0][0] == 0:
    for s in sql4:
        cur.execute(s)

# close cursor
cur.close()
# commit changes and close connection
conn.commit()
conn.close()
