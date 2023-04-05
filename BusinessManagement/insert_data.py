import pymysql
import csv
from sql.db import DB


cursor = DB.getDB().cursor()
csv_data = csv.reader(open('data.csv'))
next(csv_data)
cursor.execute('SET FOREIGN_KEY_CHECKS = 0;')
cursor.execute('TRUNCATE TABLE IS601_MP3_Companies;')
cursor.execute('SET FOREIGN_KEY_CHECKS = 1;')
for row in csv_data:
    try:
        append_rows = [row[2],row[3],row[4],row[5],row[7],row[8],row[12]]
        DB.insertOne('INSERT INTO IS601_MP3_Companies(name,address,city,country,state,zip,website) VALUES(%s, %s,%s, %s,%s, %s,%s)',*append_rows)
    except Exception as e:
        print(f"Exception occured for {append_rows}: {e}")

cursor.close()