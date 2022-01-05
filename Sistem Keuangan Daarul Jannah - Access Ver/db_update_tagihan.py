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
    update_tagihan_spp(NIS)
 
    # cursor.execute(f'SELECT * FROM pembayaran_sd where nis = \'{x.NIS}\'')
    # pembayaran_siswa = cursor.fetchall()
    
    # for y in pembayaran_siswa:
    #     Tahun_Pembayaran = y.Tahun_Pembayaran
    #     #Proses Pengecekan Tagihan SPP
    #     if y.Jenis_Pembayaran == "SPP":
    #         if Tahun_Pembayaran == datem.year - 1:
    #             if 8 < 7:
    #             #Current Month > 7
    #                 for i in range(1,7):
    #                     if convert_bln(y.Untuk_bulan) == i:
    #                         pass
    #                     else:
    #                         #Update Tagihan SPP
    #                         pass
    #             else:
    #                 month_start_s2 = 7
    #                 for i in range(month_start_s2,13):
    #                     if not convert_bln(y.Untuk_bulan) == i:
    #                         #Update Tagihan SPP
    #                         cursor.execute(f'SELECT Status FROM siswa_sd where nis = \'{y.NIS}\'')
    #                         Status_siswa = cursor.fetchall()
    #                         for z in Status_siswa:
    #                             Status_temp = z.Status
    #                         cursor.execute(f'SELECT Biaya FROM biaya_spp_sd where Katagori_siswa = \'{Status_temp}\'')
    #                         biaya_spp = cursor.fetchall()
    #                         for a in biaya_spp:
    #                             biaya_spp_temp = a[0]
                            
    #                         cursor.execute(f'SELECT Tagihan_bulan, Tagihan_tahun FROM tagihan_sd where NIS = \'{y.NIS}\' and Jenis_tagihan = \'SPP\'')
    #                         data_tagihan = cursor.fetchall()
                            
    #                         for temp in data_tagihan:
    #                             tahun_tagihan = temp.Tagihan_tahun
    #                             bulan_tagihan = temp.Tagihan_bulan
    #                             # print(bulan_tagihan, tahun_tagihan)
    #                         try:   
    #                             # print( bulan_tagihan, i)
    #                             # if not bulan_tagihan == i:
    #                             #     # update_tagihan_spp(y.NIS, i, biaya_spp_temp, Tahun_Pembayaran, tagihan_sekolah = "tagihan_sd")
    #                             #     print(bulan_tagihan)
    #                             #     count+=1
    #                             #     print(count)
    #                             pass
    #                         except:
    #                             update_tagihan_spp(y.NIS, i, biaya_spp_temp, Tahun_Pembayaran, tagihan_sekolah = "tagihan_sd")
    #                         update_tagihan_spp(y.NIS, i, biaya_spp_temp, Tahun_Pembayaran, tagihan_sekolah = "tagihan_sd")
    #                         month_start_s2+=1
                            
    #     elif y.Jenis_Pembayaran == "Tabungan Wajib":
    #         pass
            
                            

def update_tagihan_spp(NIS):
    for x in NIS:
        bulan_sdh_dibayar=[]
        bulan_x_bayar=[]
        #Pengambilan data dari database (siswa_sd)
        cursor.execute(f'SELECT * FROM siswa_sd where NIS = \'{x.NIS}\'')
        data_siswa = cursor.fetchall()
        if not len(data_siswa) == 0:
            cursor.execute(f'SELECT * FROM pembayaran_sd where NIS = \'{x.NIS}\' and Jenis_Pembayaran = \'SPP\'')
            data_pembayaran_spp = cursor.fetchall()
            for z in data_siswa:
                temp3 = z.Status

            for x in data_pembayaran_spp:
                temp = convert_bln(x.Untuk_bulan)
                bulan_sdh_dibayar.append(temp)
                
            #Pengambilan harga tagihan spp
            cursor.execute(f'SELECT Biaya FROM biaya_spp_sd where Katagori_siswa = \'{temp3}\'')
            biaya_spp = cursor.fetchall()
            for a in biaya_spp:
                biaya_spp = a.Biaya
            
            cursor.execute(f'SELECT * FROM tagihan_sd where nis = \'{x.NIS}\'')
            temp2 = cursor.fetchall()
            for y in temp2:
                bulan_x_bayar.append(y.Tagihan_bulan)

            for i in range(12):
            #12 -> datem.month
                if not i+1 in bulan_sdh_dibayar:
                    if not i+1 in bulan_x_bayar:
                        cursor.execute(f'INSERT INTO tagihan_sd (NIS, Tagihan_bulan, Jenis_tagihan, Jumlah_tagihan, Tagihan_tahun) VALUES (\'{x.NIS}\', \'{i+1}\', \'SPP\', \'{biaya_spp}\', {datem.year -1})')#datem.year -1 -> datem.year
                        conn.commit()
                elif i+1 in bulan_sdh_dibayar:   
                    # try:
                    cursor.execute(f'DELETE FROM tagihan_sd Where NIS = \'{x.NIS}\' AND Tagihan_bulan = {i+1} AND Jenis_tagihan =\'SPP\'')
                    conn.commit()
                    # except:
                    #     pass
            cursor.execute(f'SELECT * FROM tagihan_sd where nis = \'{x.NIS}\'')
            temp2 = cursor.fetchall()    

def update_tagihan_tabungan_wajib():
    # cursor.execute(f'INSERT INTO {tagihan_sekolah} (NIS, Tagihan_bulan, Jenis_tagihan, Jumlah_tagihan, Tagihan_tahun) VALUES (\'{nis}\', \'{str(i)}\',\'Tabungan Wajib\',\'{biaya_spp}\',\'{Tahun_Pembayaran}\')')
    # conn.commit()
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