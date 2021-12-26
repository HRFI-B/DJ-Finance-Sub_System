import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Database\sk_dj.accdb;')
cursor = conn.cursor()


