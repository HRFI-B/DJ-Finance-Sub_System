import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\ihzaf\OneDrive\Documents\Project\Sistem Keuangan Daarul Jannah - Access Ver\sk_dj.accdb;')
cursor = conn.cursor()
cursor.execute('select * from account')


for row in cursor.fetchall():
    print (row[row])