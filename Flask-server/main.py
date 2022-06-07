# library import
from flask import Flask,render_template,url_for, request,jsonify,session,flash
from werkzeug.utils import redirect
import pyodbc
from datetime import *
from konversi_bulan import convert_bln
import time

#get date
current_date = date.today()
datem = datetime.strptime(str(current_date), "%Y-%m-%d")

# from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

#inisialisasi variabel app
# login_manager = LoginManager()
app = Flask(__name__)
# login_manager.init_app(app)

#Koneksi ke basis data
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Database\sk_dj.accdb;')
cursor = conn.cursor()

#Direct to /login
@app.route('/', methods=['POST', 'GET'])
def function():
    return redirect('/login')

#Backend laman Login
@app.route('/login', methods=['POST', 'GET'])
def login():
    print("\n")       
    log_stat = None
    #Pengambilan data dari Form Login.html (NIP, Password)
    if request.method == 'POST':
        # session.pop('id', None)
        id = request.form['username']
        password = request.form['password']
        try:
            Verify_ID = None
            Verify_Pass = None

            #Pencocokan data NIP masukan dengan NIP di basis data
            cursor.execute(f'SELECT Username FROM app_user_account where Username = \'{id}\'')
            result = cursor.fetchall()
            for x in result:
                Verify_ID = x[0]

            #Pencocokan data password masukan dengan password pegawai di basis data
            cursor.execute(f'SELECT Password FROM app_user_account where Username = \'{id}\'')
            result = cursor.fetchall()
            for x in result:
                Verify_Pass = x[0]

            #Pengambilan data otoritas pegawai di basis data
            cursor.execute(f'SELECT Otoritas FROM app_user_account where Username = \'{id}\'')
            result = cursor.fetchall()
            for x in result:
                Otoritas = x[0]

            #Algoritma ketika NIP ditemukan di basis data dan password benar
            if not Verify_ID == None and Verify_Pass == password:
                print("\nLogin Success as ", end = '')
                print(Otoritas, end=' - ')
                print(request.remote_addr)
                # session['id']=Verify_ID
                #Pengalihan ke laman home
                return redirect(url_for('home'))

            #Algoritma ketika NIP tidak ditemukan
            elif Verify_ID == None:
                print("\nWrong ID!")
                return redirect(url_for('login'))
                
            #Algoritma ketika NIP tidak ditemukan
            elif not Verify_Pass == password:
                print("\nWrong Password!")
                return redirect(url_for('login'))
        
        #jika ada error dalam masukan data
        except ValueError:
            return 'There was an issue'

    else:
        #Render login.html jika ada request dari client
        return render_template('Login.html')

#Backend laman pengecekan pembayaran siswa
@app.route('/pengecekan_pembayaran_siswa', methods=['POST', 'GET'])
def pengecekan_pembayaran_siswa():
    print("\n")
    #Jika ada aksi metode post dari front end
    if request.method == 'POST':
        #Penarikan variabel nis dari form ke variabel python
        nis = request.form['nis']
        #Pengambilan data dari database (siswa_sd)
        cursor.execute(f'SELECT Nama FROM siswa_sd where nis = \'{nis}\'')
        result = cursor.fetchall()
        #jika tidak ditemukan nis yang dicari di tabel siswa_sd, pencarian dilanjutkan ke tabel siswa_smp
        if len(result) == 0:
            cursor.execute(f'SELECT Nama FROM siswa_smp where nis = \'{nis}\'')
            result = cursor.fetchall()
        #jika tidak ditemukan nis yang dicari di tabel siswa_smp, pencarian dilanjutkan ke tabel siswa_tk    
        if len(result) == 0:
            cursor.execute(f'SELECT Nama FROM siswa_tk where nis = \'{nis}\'')
            result = cursor.fetchall()
        #konversi bentuk array ke variabel string
        for x in result:
            nama = x[0] 
            if nama == "":
                nama = None
            
        try:
            if not nama == None:
                nis = int(nis)
                try:
                    return redirect (url_for('.detail_pembayaran', nis=nis))
                except:
                    print("error accured")
            else:
                print("Wrong ID")
                return render_template('cek_pembayaran.html')
        except:
            print("Wrong ID")
            return render_template('cek_pembayaran.html')
    else:
        return render_template('cek_pembayaran.html')

@app.route('/detail_pembayaran/<nis>', methods=['POST', 'GET'])
def detail_pembayaran(nis):
    # try:
    if request.method == 'POST':
        return None
    else:
        bulan_sdh_dibayar=[]
        bulan_x_bayar=[]
        #Pengambilan data dari database (siswa_sd)
        cursor.execute(f'SELECT * FROM siswa_sd where nis = \'{nis}\'')
        data_siswa = cursor.fetchall()
        if not len(data_siswa) == 0:
            cursor.execute(f'SELECT * FROM pembayaran_spp_sd where nis = \'{nis}\'')
            data_pembayaran_spp = cursor.fetchall()
            for z in data_siswa:
                temp3 = z.Status
            cursor.execute(f'SELECT Biaya FROM biaya_spp_sd where Katagori_siswa = \'{temp3}\'')
            biaya_spp = cursor.fetchall()
            for a in biaya_spp:
                biaya_spp = a[0]
            for x in data_pembayaran_spp:
                temp = convert_bln(x.Untuk_bulan)
                bulan_sdh_dibayar.append(temp)
            cursor.execute(f'SELECT * FROM tagihan_sd where nis = \'{nis}\'')
            temp2 = cursor.fetchall()
            for y in temp2:
                bulan_x_bayar.append(y.Tagihan_bulan)
            for i in range(datem.month):
                if not i+1 in bulan_sdh_dibayar:
                    if not i+1 in bulan_x_bayar:
                        cursor.execute(f'INSERT INTO tagihan_sd (NIS, Tagihan_bulan, Jenis_tagihan, Jumlah_tagihan) VALUES (\'{nis}\', \'{str(i+1)}\',\'SPP\',\'{biaya_spp}\')')
                        conn.commit()
                elif i+1 in bulan_sdh_dibayar:   
                    try:
                        cursor.execute(f'DELETE FROM tagihan_sd WHERE NIS =\'{nis}\' AND Tagihan_bulan =\'{str(i+1)}\'')
                        conn.commit()
                    except:
                        pass
            cursor.execute(f'SELECT * FROM tagihan_sd where nis = \'{nis}\'')
            temp2 = cursor.fetchall()            
        
        #jika tidak ditemukan nis yang dicari di tabel siswa_sd, pencarian dilanjutkan ke tabel siswa_smp
        if len(data_siswa) == 0:
            cursor.execute(f'SELECT * FROM siswa_smp where nis = \'{nis}\'')
            data_siswa = cursor.fetchall()
            if not len(data_siswa) == 0:
                cursor.execute(f'SELECT * FROM pembayaran_spp_smp where nis = \'{nis}\'')
                data_pembayaran_spp = cursor.fetchall()
                for z in data_siswa:
                    temp3 = z.Status
                cursor.execute(f'SELECT Biaya FROM biaya_spp_smp where Katagori_siswa = \'{temp3}\'')
                biaya_spp = cursor.fetchall()
                for a in biaya_spp:
                    biaya_spp = a[0]
                for x in data_pembayaran_spp:
                    temp = convert_bln(x.Untuk_bulan)
                    bulan_sdh_dibayar.append(temp)
                cursor.execute(f'SELECT * FROM tagihan_smp where nis = \'{nis}\'')
                temp2 = cursor.fetchall()
                for y in temp2:
                    bulan_x_bayar.append(y.Tagihan_bulan)
                for i in range(datem.month):
                    if not i+1 in bulan_sdh_dibayar:
                        if not i+1 in bulan_x_bayar:
                            cursor.execute(f'INSERT INTO tagihan_smp (NIS, Tagihan_bulan, Jenis_tagihan, Jumlah_tagihan) VALUES (\'{nis}\', \'{str(i+1)}\',\'SPP\',\'{biaya_spp}\')')
                            conn.commit()
                    elif i+1 in bulan_sdh_dibayar:   
                        try:
                            cursor.execute(f'DELETE FROM tagihan_smp WHERE NIS =\'{nis}\' AND Tagihan_bulan =\'{str(i+1)}\'')
                            conn.commit()
                        except:
                            pass
                cursor.execute(f'SELECT * FROM tagihan_smp where nis = \'{nis}\'')
                temp2 = cursor.fetchall()                  
        #jika tidak ditemukan nis yang dicari di tabel siswa_smp, pencarian dilanjutkan ke tabel siswa_tk    
        if len(data_siswa) == 0:
            cursor.execute(f'SELECT * FROM siswa_tk where nis = \'{nis}\'')
            data_siswa = cursor.fetchall()
            if not len(data_siswa) == 0:
                cursor.execute(f'SELECT * FROM pembayaran_spp_tk where nis = \'{nis}\'')
                data_pembayaran_spp = cursor.fetchall()
                for z in data_siswa:
                    temp3 = z.Status
                cursor.execute(f'SELECT Biaya FROM biaya_spp_tk where Katagori_siswa = \'{temp3}\'')
                biaya_spp = cursor.fetchall()
                for a in biaya_spp:
                    biaya_spp = a[0]
                for x in data_pembayaran_spp:
                    temp = convert_bln(x.Untuk_bulan)
                    bulan_sdh_dibayar.append(temp)
                cursor.execute(f'SELECT * FROM tagihan_tk where nis = \'{nis}\'')
                temp2 = cursor.fetchall()
                for y in temp2:
                    bulan_x_bayar.append(y.Tagihan_bulan)
                for i in range(datem.month):
                    if not i+1 in bulan_sdh_dibayar:
                        if not i+1 in bulan_x_bayar:
                            cursor.execute(f'INSERT INTO tagihan_tk (NIS, Tagihan_bulan, Jenis_tagihan, Jumlah_tagihan) VALUES (\'{nis}\', \'{str(i+1)}\',\'SPP\',\'{biaya_spp}\')')
                            conn.commit()
                    elif i+1 in bulan_sdh_dibayar:   
                        try:
                            cursor.execute(f'DELETE FROM tagihan_tk WHERE NIS =\'{nis}\' AND Tagihan_bulan =\'{str(i+1)}\'')
                            conn.commit()
                        except:
                            pass
                cursor.execute(f'SELECT * FROM tagihan_tk where nis = \'{nis}\'')
                temp2 = cursor.fetchall()                    
            #Render tabel-pembayaran.html jika ada request dari client
        return render_template('tabel-pembayaran.html', siswa=data_siswa, spp=data_pembayaran_spp, tagihan=temp2)
    # except:
        print("error")


#Backend laman home
@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        print("\n")
    else:
        #Render home.html jika ada request dari client
        return render_template('home.html')

#run program
if __name__ == "__main__": 
    # app.secret_key = 'super secret key'
    # app.config["SESSION_PERMANENT"] = False
    # app.config["SESSION_TYPE"] = "filesystem"
    app.run(host='127.0.0.1', port=8080, debug=True)