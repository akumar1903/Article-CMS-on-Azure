import os

import pymssql
import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};server=udacityarticlecms.database.windows.net,1433;UID=udacityadmin;PWD=;database=udacityarticlecms");  
conn2 = pymssql.connect(server='udacityarticlecms.database.windows.net', user='udacityadmin', password='', database='udacityarticlecms',port=1433);  

cursor = conn.cursor()
cursor.execute('select 1 as a, 2 as b')
row = cursor.fetchone()
print(f"row={row}")

cursor = conn.cursor();  
cursor.execute("SELECT 1");
row = cursor.fetchall()

conn.close()

for i in row:
    print(i)

cursor2 = conn2.cursor();  
cursor2.execute("SELECT 1");
row2 = cursor2.fetchall()

conn2.close()

for i in row2:
    print(i)