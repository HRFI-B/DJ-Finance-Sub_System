import pyodbc
from konversi_bulan import convert_bln
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Database\sk_dj.accdb;')
cursor = conn.cursor()

def update_tagihan_sd():
    cursor.execute(f'SELECT NIS FROM siswa_sd')
    NIS = cursor.fetchall()
    for x in NIS:
        cursor.execute(f'SELECT * FROM pembayaran_sd where nis = \'{x.NIS}\'')
        pembayaran_siswa = cursor.fetchall()
        for y in pembayaran_siswa:
            Tahun_Pembayaran = convert_bln(y.Tahun_)
            if Tahun_Pembayaran >= 7:
                pass

    

update_tagihan_sd()