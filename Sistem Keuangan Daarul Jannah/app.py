from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import *
from flask_mysqldb import MySQL
import MySQLdb.cursors
from threading import Thread
from math import floor

#Koneksi, inisialisasi DB
def connect_db():
    # IP host database
    app.config['MYSQL_HOST'] = 'localhost'

    # Nama user database
    app.config['MYSQL_USER'] = 'root'

    # Password user database
    app.config['MYSQL_PASSWORD'] = ''

    # Nama database
    app.config['MYSQL_DB'] = 'sistem_pembayaran'

    mysql = MySQL(app)
    return mysql

# inisiasi variabel aplikasi
app = Flask(__name__)
mysql = connect_db()

# pembaruan data tagihan
# def update_tagihan():
#     with mysql.connection.cursor() as cursor:
#         cursor.execute('SELECT nis FROM siswa_sd')
#         nis_siswa = cursor.fetchall()
#         update_tagihan_spp_sd(nis_siswa)
        # update_tagihan_tabungan_wajib_sd(siswa)
        # penghapusan_data_pembayaran_sd()

# # update tagihan spp sd
# def update_tagihan_spp_sd(siswa):
#     # pembaruan tagihan spp sd secara bergantian dalam perulangan
#     for nis_siswa in nis_siswa:
#         paid_month=[]
#         unpaid_month=[]
#         #Pengambilan data dari database (siswa_sd)
#         with mysql.connection.cursor() as cursor:
#             cursor.execute('SELECT * FROM siswa_sd where NIS = %s', (nis_siswa['nis'],))
#             siswa = cursor.fetchone()
        
#         # Jika data siswa ditemukan
#         if siswa:
#             katagori_siswa = siswa['status']
#             # Pemanggilan data pembayaran spp siswa
#             with mysql.connection.cursor() as cursor:
#                 cursor.execute('SELECT * FROM pembayaran_sd where NIS = %s and jenis_pembayaran = %s', (siswa['NIS'], 'SPP'))
#                 data_pembayaran_spp = cursor.fetchall()
                            
#             for data_pembayaran_spp in data_pembayaran_spp:
#                 if data_pembayaran_spp['status'] == "Lunas": 
#                     paid_month.append(data_pembayaran_spp['untuk_bulan'])

#                 elif data_pembayaran_spp['status'] == "Overpaid":
#                     with mysql.connection.cursor() as cursor:
#                         cursor.execute('SELECT biaya FROM biaya_spp_sd where status = %s', (katagori_siswa,))
#                         biaya_spp = cursor.fetchone()
#                         biaya_spp = biaya_spp['biaya']
#                     overpaid_month = floor(data_pembayaran_spp['jumlah_pembayran']/biaya_spp)
#                     for bulan in range (data_pembayaran_spp['untuk_bulan'],data_pembayaran_spp['untuk_bulan']+overpaid_month):
#                         paid_month.append(bulan)
                
#             #Pengambilan harga tagihan spp
#             cursor.execute(f'SELECT biaya FROM biaya_spp_sd where status = \'{katagori_siswa}\'')
#             biaya_spp = cursor.fetchone()
#             biaya_spp = biaya_spp['biaya']
            
#             cursor.execute(f'SELECT * FROM tagihan_sd where nis = \'{x.NIS}\'')
#             temp2 = cursor.fetchall()
#             for y in temp2:
#                 bulan_x_bayar.append(y.Tagihan_bulan)

#             for i in range(12):
#             #12 -> datem.month
#                 if not i+1 in bulan_sdh_dibayar:
#                     if not i+1 in bulan_x_bayar:
#                         cursor.execute(f'INSERT INTO tagihan_sd (NIS, Tagihan_bulan, Jenis_tagihan, Jumlah_tagihan, Tagihan_tahun) VALUES (\'{x.NIS}\', \'{i+1}\', \'SPP\', \'{biaya_spp}\', {datem.year -1})')#datem.year -1 -> datem.year
#                         conn.commit()
#                 elif i+1 in bulan_sdh_dibayar:   
#                     cursor.execute(f'DELETE FROM tagihan_sd Where NIS = \'{x.NIS}\' AND Tagihan_bulan = {i+1} AND Jenis_tagihan =\'SPP\'')
#                     conn.commit()

# eksekusi pembaruan data tagihan
# thread = Thread(target=update_tagihan(), args=())
# thread.daemon = Tru
# thread.start()

@app.route('/', methods=['GET', 'POST'])
def function():
    if not 'loggedin' in session:
        return redirect(url_for('login'))
    return redirect(url_for('home'))

@app.route('/login', methods=['POST', 'GET'])
def login():    
    msg = ''
    #Pengambilan data dari Form Login.html (username, Password)
    if not 'loggedin' in session:
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            # inisiasi variabel kredensial dari form login
            # username
            username = request.form['username']
            # password
            password = request.form['password']
            
            # Pengambilan data user dari database
            with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                cursor.execute('SELECT * FROM user where username = %s AND password = %s', (username, password))
                user = cursor.fetchone()
            
            # jika user ditemukan
            if user:
                # inisiasi data session

                # menyatakan bahwa user telah login
                session['loggedin'] = True

                # menyimpan data nip user
                session['nip'] = user['nip']

                # menyimpan data username user
                session['username'] = user['username']

                # menyimpan data otoritas user
                session['otoritas'] = user['otoritas']
                
                # pengambilan data nama pegawai dari database
                with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                    cursor.execute('SELECT nama_pegawai FROM pegawai where nip = %s', ([user['nip']]))
                    pegawai = cursor.fetchone()

                # menyimpan data nama pegawai user
                session['nama'] = pegawai['nama_pegawai']
                
                # Redirect to home page
                return redirect(url_for('home'))
            
            # jika username atau password salah
            else:
                msg = 'Incorrect username/password!'
    
    # redirect user ke halaman home jika sudah login 
    elif 'loggedin' in session:
        return redirect(url_for('home'))
    
    #Render login.html jika ada request dari client
    return render_template('login-page.html',msg=msg)

@app.route('/logout')
def logout():
    # ketika fungsi logout dijalankan, semua cookie pada browser akan dihapus
    # hal ini menyebabkan user tidak dapat mengakses aplikasi sebelum melakukan login

    # menghapus semua data session
    session.clear()

    # redirect user ke halaman login
    return redirect(url_for('login'))

@app.route('/home', methods=['POST', 'GET'])
def home():
    # halaman utama aplikasi atau dashboard

    # jika user sudah login, maka user tidak akan diredirect ke halaman login
    if 'loggedin' in session:

        # instruksi yang dijalankan ketika akun memiliki otoritas staff
        if session['otoritas'] =='Staff':
            return render_template('dashboard.html')

        # instruksi yang dijalankan ketika akun memiliki otoritas admin
        elif session['otoritas']=='Admin':
            return render_template('dashboard.html')
    
    # jika user belum login, maka user akan diredirect ke halaman login
    return redirect('/login')

@app.route('/manajemen_siswa', methods=['GET'])
def manajemen_siswa():
    # halaman manajemen siswa
    # jika user sudah login, maka user tidak akan diredirect ke halaman login
    if 'loggedin' in session:

        # instruksi yang dijalankan ketika akun memiliki otoritas staff
        if session['otoritas'] == 'Staff':

            # pengambilan semua data siswa dari database
            with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:

                # pengambilan data siswa tk
                cursor.execute('SELECT * FROM siswa_tk')
                siswa_tk = cursor.fetchall()

                # pengambilan data siswa sd
                cursor.execute('SELECT * FROM siswa_sd')
                siswa_sd = cursor.fetchall()

                # pengambilan data siswa smp
                cursor.execite('SELECT * FROM siswa_smp')
                siswa_smp = cursor.fetchall()
            
            # render template manajemen_siswa.html dengan data siswa
            return render_template('tabelsiswa.html',siswa_tk=siswa_tk, siswa_sd=siswa_sd, siswa_smp=siswa_smp)

        # instruksi yang dijalankan ketika akun memiliki otoritas admin
        elif session['otoritas'] == 'Admin':

            # pengambilan semua data siswa dari database
            with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:

                # pengambilan data siswa tk
                cursor.execute('SELECT * FROM siswa_tk')
                siswa_tk = cursor.fetchall()

                # pengambilan data siswa sd
                cursor.execute('SELECT * FROM siswa_sd')
                siswa_sd = cursor.fetchall()

                # pengambilan data siswa smp
                cursor.execute('SELECT * FROM siswa_smp')
                siswa_smp = cursor.fetchall()

            # render template manajemen_siswa.html dengan data siswa
            return render_template('tabelsiswa.html',siswa_tk=siswa_tk, siswa_sd=siswa_sd, siswa_smp=siswa_smp)
    
    # jika user belum login, maka user akan diredirect ke halaman login
    return redirect('/login')

@app.route('/detail_siswa/<nis>', methods=['GET'])
def detail_siswa(nis):
    if 'loggedin' in session:

        # instruksi yang dijalankan ketika akun memiliki otoritas staff
        if session['otoritas'] == 'Staff':
            with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                cursor.execute('SELECT * FROM siswa_sd WHERE nis = %s', ([nis]))
                siswa = cursor.fetchone()
                if not siswa:
                    cursor.execute('SELECT * FROM siswa_smp WHERE nis = %s', ([nis]))
                    siswa = cursor.fetchone()
                    if not siswa:
                        cursor.execute('SELECT * FROM siswa_tk WHERE nis = %s', ([nis]))
                        siswa = cursor.fetchone()
            return render_template('datasiswa.html',siswa=siswa)

        # instruksi yang dijalankan ketika akun memiliki otoritas admin
        elif session['otoritas'] == 'Admin':
            with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                cursor.execute('SELECT * FROM siswa_sd WHERE nis = %s', ([nis]))
                siswa = cursor.fetchone()
                if not siswa:
                    cursor.execute('SELECT * FROM siswa_smp WHERE nis = %s', ([nis]))
                    siswa = cursor.fetchone()
                    if not siswa:
                        cursor.execute('SELECT * FROM siswa_tk WHERE nis = %s', ([nis]))
                        siswa = cursor.fetchone()
            return render_template('datasiswa.html',siswa=siswa)

    # jika user belum login, maka user akan diredirect ke halaman login
    return redirect('/login')

@app.route('/ubah_siswa/<nis>')
def ubah_siswa():
    pass

@app.route('/hapus_siswa/<nis>')
def hapus_siswa():
    pass

@app.route('/riwayat_pembayaran/<nis>', methods=['GET'])
def riwayat_pembayaran(nis):
    if request.method == 'GET':
        # update_tagihan_sd()
        #Pengambilan data siswa sd dari database
        with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute('SELECT * FROM siswa_sd where nis = %s', ([nis]))
            data_siswa = cursor.fetchone()
            
            if data_siswa:
                cursor.execute('SELECT * FROM pembayaran_sd where nis = %s ORDER by waktu_pembayaran DESC', ([nis]))
                data_pembayaran = cursor.fetchall()
                cursor.execute('SELECT * FROM tagihan_sd where nis = %s ORDER by tagihan_bulan ASC', ([nis]))
                tagihan_siswa = cursor.fetchall()      
            
        # jika data siswa tidak ditemukan ditemukan
        if not data_siswa:
            with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                cursor.execute('SELECT * FROM siswa_smp where nis = %s', ([nis]))
                data_siswa = cursor.fetchone()
            
                if data_siswa:
                    cursor.execute('SELECT * FROM pembayaran_smp where nis = %s', ([nis]))
                    data_pembayaran = cursor.fetchall()
                    cursor.execute('SELECT * FROM tagihan_smp where nis = %s', ([nis]))
                    tagihan_siswa = cursor.fetchall()    
                        
            #jika tidak ditemukan nis yang dicari di tabel siswa_smp, pencarian dilanjutkan ke tabel siswa_tk    
            if not data_siswa:
                with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                    cursor.execute('SELECT * FROM siswa_tk where nis = %s', ([nis]))
                    data_siswa = cursor.fetchone()
                
                    if data_siswa:
                        cursor.execute('SELECT * FROM pembayaran_tk where nis = %s', ([nis]))
                        data_pembayaran = cursor.fetchall()
                        cursor.execute('SELECT * FROM tagihan_tk where nis = %s', ([nis]))
                        tagihan_siswa = cursor.fetchall()  
        
        #Render tabel-pembayaran.html jika ada request dari client
        return render_template('riwayat_pembayaran.html', siswa=data_siswa, spp=data_pembayaran, tagihan=tagihan_siswa)

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host='0.0.0.0',port=2431 ,debug=True)