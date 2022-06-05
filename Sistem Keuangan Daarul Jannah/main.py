# library import
from email import message
from flask import Flask,render_template,url_for, request,jsonify,session,flash
from matplotlib.style import use
from werkzeug.utils import redirect
import pyodbc
from datetime import *
from db_update_tagihan import update_tagihan_sd
import os
# from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

#get date
current_date = date.today()
datem = datetime.strptime(str(current_date), "%Y-%m-%d")

#inisialisasi variabel app
# login_manager = LoginManager()
app = Flask(__name__)
# login_manager.init_app(app)

#Koneksi ke basis data
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Database\sk_dj.accdb;')
cursor = conn.cursor()

@app.route('/login', methods=['POST', 'GET'])
def login():    
    msg = ''
    #Pengambilan data dari Form Login.html (NIP, Password)
    if not 'loggedin' in session:
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            # session.pop('id', None)
            username = request.form['username']
            password = request.form['password']
            cursor.execute(f'SELECT * FROM app_user_account where Username = \'{username}\' AND Password = \'{password}\'')
            # Fetch one record and return result
            account = cursor.fetchone()
            if account:
                cursor.execute(f'SELECT * FROM pegawai where NIP = \'{account.NIP}\'')
                # Fetch one record and return result
                account_data = cursor.fetchone()
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['username'] = account.Username
                session['otoritas'] = account.Otoritas
                session['nama'] = account_data.Nama_Pegawai
                # Redirect to home page
                return redirect(url_for('home'))
            else:
                msg = 'Incorrect username/password!'
    elif 'loggedin' in session:
        return redirect(url_for('home'))
    #Render login.html jika ada request dari client
    return render_template('Login.html',msg=msg)

#Direct to /login
@app.route('/', methods=['POST', 'GET'])
def function():
    if not 'username' in session:
        return redirect('/login')
    return redirect(url_for('home'))

#Backend laman ubah data
@app.route('/ubah_data', methods=['POST', 'GET'])
def ubah_data():
    if 'loggedin' in session:
        if request.method == 'POST':
            print("\n")
        else:
            #Render home.html jika ada request dari client
            return render_template('ubahdata.html')
    else:
        return redirect('/login')
#Backend laman pengecekan pembayaran siswa
@app.route('/pengecekan_pembayaran_siswa', methods=['POST', 'GET'])
def pengecekan_pembayaran_siswa():
    if 'loggedin' in session:
        #Jika ada aksi metode post dari front end
        if request.method == 'POST':
            #Penarikan variabel nis dari form ke variabel python
            nis = request.form['nis']
            #Pengambilan data dari database (siswa_sd)
            cursor.execute(f'SELECT Nama FROM siswa_sd where nis = \'{nis}\'')
            result = cursor.fetchone()
            #jika tidak ditemukan nis yang dicari di tabel siswa_sd, pencarian dilanjutkan ke tabel siswa_smp
            if not result:
                cursor.execute(f'SELECT Nama FROM siswa_smp where nis = \'{nis}\'')
                result = cursor.fetchone()
            #jika tidak ditemukan nis yang dicari di tabel siswa_smp, pencarian dilanjutkan ke tabel siswa_tk    
            if not result:
                cursor.execute(f'SELECT Nama FROM siswa_tk where nis = \'{nis}\'')
                result = cursor.fetchone()
            if not result:
                return render_template('cek_pembayaran.html')
            elif result.Nama:
                nis = int(nis)
                return redirect (url_for('.detail_pembayaran', nis=nis))
        else:
            return render_template('cek_pembayaran.html')
    return redirect('/login')

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
            cursor.execute(f'SELECT * FROM pembayaran_sd where nis = \'{nis}\' ORDER by Waktu_Pembayaran DESC')
            data_pembayaran = cursor.fetchall()
            cursor.execute(f'SELECT * FROM tagihan_sd where nis = \'{nis}\' ORDER by Tagihan_bulan ASC')
            tagihan_siswa = cursor.fetchall()      
            
        #jika tidak ditemukan nis yang dicari di tabel siswa_sd, pencarian dilanjutkan ke tabel siswa_smp
        if len(data_siswa) == 0:
            cursor.execute(f'SELECT * FROM pembayaran_smp where nis = \'{nis}\'')
            data_pembayaran = cursor.fetchall()
            cursor.execute(f'SELECT * FROM tagihan_smp where nis = \'{nis}\'')
            tagihan_siswa = cursor.fetchall()     
                        
        #jika tidak ditemukan nis yang dicari di tabel siswa_smp, pencarian dilanjutkan ke tabel siswa_tk    
        if len(data_siswa) == 0:
            cursor.execute(f'SELECT * FROM pembayaran_tk where nis = \'{nis}\'')
            data_pembayaran = cursor.fetchall()
            cursor.execute(f'SELECT * FROM tagihan_tk where nis = \'{nis}\'')
            tagihan_siswa = cursor.fetchall()  
        
        #Render tabel-pembayaran.html jika ada request dari client
        return render_template('tabel-pembayaran.html', siswa=data_siswa, spp=data_pembayaran, tagihan=tagihan_siswa)

# Backend laman home
@app.route('/home', methods=['POST', 'GET'])
def home():
    if 'loggedin' in session and session['otoritas'] =='Staff':
        return render_template('home.html')
    elif session['otoritas']=='Admin':
        return render_template('maintenance.html')
    else:
        return redirect('/login')

#run program
if __name__ == "__main__": 
    os.system('title SK Server')
    app.secret_key = 'super secret key'
    app.config["SESSION_PERMANENT"] = False
    # app.config["SESSION_TYPE"] = "filesystem"
    app.run(host='0.0.0.0', port=5001, debug=True)