import pandas as pd
import pymysql
cx = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='',
                     db='northwind')

cur = cx.cursor()
cur.execute("SELECT orderID, customerID FROM orders")
print(cur.description)
print()
for row in cur:
    print(row)

pd.read_sql("SELECT orderID, customerID FROM orders","db_connection")

cur.close()
cx.close()
