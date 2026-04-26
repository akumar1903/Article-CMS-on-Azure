import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=tcp:udacityarticlecms.database.windows.net,1433;"
    "DATABASE=udacityarticlecms;"
    "UID=udacityadmin;"
    "PWD=<>;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

cursor = conn.cursor()
cursor.execute("SELECT 1")
print(cursor.fetchall())

conn.close()