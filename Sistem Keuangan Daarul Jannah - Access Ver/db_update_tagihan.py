import pyodbc
from konversi_bulan import convert_bln
from datetime import *
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Database\sk_dj.accdb;')
cursor = conn.cursor()


#get date
current_date = date.today()
datem = datetime.strptime(str(current_date), "%Y-%m-%d")

def update_tagihan_sd():
    cursor.execute(f'SELECT NIS FROM siswa_sd')
    NIS = cursor.fetchall()
    for x in NIS:
        cursor.execute(f'SELECT * FROM pembayaran_sd where nis = \'{x.NIS}\'')
        pembayaran_siswa = cursor.fetchall()
        for y in pembayaran_siswa:
            Tahun_Pembayaran = y.Tahun_Pembayaran
            if Tahun_Pembayaran == datem.year - 1:
                if 8 < 7:
                    for i in range(1,7):
                        if convert_bln(y.Untuk_bulan) == i:
                            pass
                        else:
                            #Update Tagihan SPP
                            cursor.execute(f'SELECT Status FROM siswa_sd where nis = \'{y.NIS}\'')
                            Status_siswa = cursor.fetchall()
                            for z in Status_siswa:
                                Status_temp = z.Status
                            cursor.execute(f'SELECT Biaya FROM biaya_spp_sd where Katagori_siswa = \'{Status_temp}\'')
                            biaya_spp = cursor.fetchall()
                            for a in biaya_spp:
                                biaya_spp_temp = a[0]
                            update_tagihan_spp(y.NIS, i, biaya_spp_temp, tagihan_sekolah = "tagihan_sd")
                else:
                    for i in range(7,13):
                        if convert_bln(y.Untuk_bulan) == i:
                            if y.Jenis_Pembayaran == "SPP":
                                pass
                            
                        else:
                            #Update Tagihan SPP
                            cursor.execute(f'SELECT Status FROM siswa_sd where nis = \'{y.NIS}\'')
                            Status_siswa = cursor.fetchall()
                            for z in Status_siswa:
                                Status_temp = z.Status
                            cursor.execute(f'SELECT Biaya FROM biaya_spp_sd where Katagori_siswa = \'{Status_temp}\'')
                            biaya_spp = cursor.fetchall()
                            for a in biaya_spp:
                                biaya_spp_temp = a[0]
                            update_tagihan_spp(y.NIS, i, biaya_spp_temp, tagihan_sekolah = "tagihan_sd")

def update_tagihan_spp(nis, i, biaya_spp,tagihan_sekolah):
    cursor.execute(f'INSERT INTO \'{tagihan_sekolah}\' (NIS, Tagihan_bulan, Jenis_tagihan, Jumlah_tagihan) VALUES (\'{nis}\', \'{str(i)}\',\'SPP\',\'{biaya_spp}\')')
    conn.commit()

def update_tagihan_tabungan_wajib():
    pass

def update_tagihan_ekskul():
    pass

def update_tagihan_zis():
    pass

def update_tagihan_tpq():
    pass

def update_tagihan_kb():
    pass


update_tagihan_sd()