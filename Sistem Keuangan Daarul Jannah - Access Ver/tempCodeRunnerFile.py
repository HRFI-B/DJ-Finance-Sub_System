# library import
from flask import Flask,render_template,url_for, request,jsonify,session,flash
from werkzeug.utils import redirect
import pyodbc
from datetime import *
from konversi_bulan import convert_bln
import time
from db_update_tagihan import update_tagihan_sd

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
    return redirect('/pengecekan_pembayaran_siswa')


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
        update_tagihan_sd()
        #Pengambilan data dari database (siswa_sd)
        cursor.execute(f'SELECT * FROM siswa_sd where nis = \'{nis}\'')
        data_siswa = cursor.fetchall()
        if not len(data_siswa) == 0:
            cursor.execute(f'SELECT * FROM pembayaran_spp_sd where nis = \'{nis}\'')
            data_pembayaran_spp = cursor.fetchall()
            cursor.execute(f'SELECT * FROM tagihan_sd where nis = \'{nis}\'')
            tagihan_siswa = cursor.fetchall()           
            
        #jika tidak ditemukan nis yang dicari di tabel siswa_sd, pencarian dilanjutkan ke tabel siswa_smp
        if len(data_siswa) == 0:
            cursor.execute(f'SELECT * FROM pembayaran_spp_smp where nis = \'{nis}\'')
            data_pembayaran_spp = cursor.fetchall()
            cursor.execute(f'SELECT * FROM tagihan_smp where nis = \'{nis}\'')
            tagihan_siswa = cursor.fetchall()     
                        
        #jika tidak ditemukan nis yang dicari di tabel siswa_smp, pencarian dilanjutkan ke tabel siswa_tk    
        if len(data_siswa) == 0:
            cursor.execute(f'SELECT * FROM pembayaran_spp_sd where nis = \'{nis}\'')
            data_pembayaran_spp = cursor.fetchall()
            cursor.execute(f'SELECT * FROM tagihan_sd where nis = \'{nis}\'')
            tagihan_siswa = cursor.fetchall()                   
            #Render tabel-pembayaran.html jika ada request dari client
        return render_template('tabel-pembayaran.html', siswa=data_siswa, spp=data_pembayaran_spp, tagihan=tagihan_siswa)
    # except:
        print("error")


#Backend laman home
# @app.route('/home', methods=['POST', 'GET'])
# def home():
#     if request.method == 'POST':
#         print("\n")
#     else:
#         #Render home.html jika ada request dari client
#         return render_template('home.html')

#run program
if __name__ == "__main__": 
    # app.secret_key = 'super secret key'
    # app.config["SESSION_PERMANENT"] = False
    # app.config["SESSION_TYPE"] = "filesystem"
    app.run(host='127.0.0.1', port=8080, debug=True)