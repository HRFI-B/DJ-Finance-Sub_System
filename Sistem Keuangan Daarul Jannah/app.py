from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import *
from flask_mysqldb import MySQL
import MySQLdb.cursors
from threading import Thread
import os

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

app.config['UPLOAD_FOLDER'] = 'static/foto_siswa'

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
    
    session['year'] = date.today().year
    
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
    # halaman detail siswa
    # jika user sudah login, maka user tidak akan diredirect ke halaman login
    if 'loggedin' in session:

        # instruksi yang dijalankan ketika akun memiliki otoritas staff atau admin
        if session['otoritas'] == 'Staff' or session['otoritas'] == 'Admin':
            
            # pengambilan data siswa dari database
            with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:

                # pengambilan data siswa sd
                cursor.execute('SELECT * FROM siswa_sd WHERE nis = %s', ([nis]))
                siswa = cursor.fetchone()

                tingkat = 'SD'

                # instruksi jika siswa sd tidak ditemukan
                if not siswa:
                    # pengambilan data siswa smp
                    cursor.execute('SELECT * FROM siswa_smp WHERE nis = %s', ([nis]))
                    siswa = cursor.fetchone()

                    tingkat = 'SMP'

                    # instruksi jika siswa smp tidak ditemukan
                    if not siswa:
                        # pengambilan data siswa tk
                        cursor.execute('SELECT * FROM siswa_tk WHERE nis = %s', ([nis]))
                        siswa = cursor.fetchone()

                        tingkat = 'TK'
            
            # render template detail_siswa.html dengan data siswa
            return render_template('datasiswa.html',siswa=siswa, tingkat=tingkat)

    # jika user belum login, maka user akan diredirect ke halaman login
    return redirect('/login')

@app.route('/tambah_siswa', methods=['POST', 'GET'])
def tambah_siswa():
    # halaman tambah siswa
    # jika user sudah login, maka user tidak akan diredirect ke halaman login
    if 'loggedin' in session:

        # instruksi yang dijalankan ketika akun memiliki otoritas staff atau admin
            if session['otoritas'] == 'Staff' or session['otoritas'] == 'Admin':
                # instruksi yang dijalankan ketika request method POST
                if request.method == 'POST':
                        # pengambilan data siswa baru dari form

                        # nis siswa
                        nis = request.form['nis']

                        # nisn siswa
                        nisn = request.form['nisn']

                        # nama siswa
                        nama_siswa = request.form['nama_siswa']

                        # jenis kelamin siswa
                        jenis_kelamin = request.form['jenis_kelamin']

                        # kelas siswa
                        kelas = request.form['kelas']

                        # status siswa
                        status = request.form['status']

                        # tingkat siswa
                        tingkat = request.form['tingkat']

                        # foto siswa
                        foto_profil = request.files['foto_siswa']
                        nama_foto = str(foto_profil.filename)
                        if foto_profil:
                            foto_profil.save(os.path.join(app.config['UPLOAD_FOLDER'], nama_foto))
                        else:
                            nama_foto = 'default.jpg'

                        # pemasukan data siswa baru ke database
                        with mysql.connection.cursor() as cursor:
                            # pemasukan data siswa baru ke dalam database siswa_tk jika tingkat siswa adalah tk
                            if tingkat == "TK":
                                cursor.execute('INSERT IGNORE INTO siswa_tk (nis, nisn, nama_siswa, jenis_kelamin, kelas, status, foto_path) VALUES (%s, %s, %s, %s, %s, %s, %s)', (nis, nisn, nama_siswa, jenis_kelamin, kelas, status, nama_foto))
                                mysql.connection.commit()

                            # pemasukan data siswa baru ke dalam database siswa_sd jika tingkat siswa adalah sd
                            elif tingkat == "SD":
                                cursor.execute('INSERT IGNORE INTO siswa_sd (nis, nisn, nama_siswa, jenis_kelamin, kelas, status, foto_path) VALUES (%s, %s, %s, %s, %s, %s, %s)', (nis, nisn, nama_siswa, jenis_kelamin, kelas, status, nama_foto))
                                mysql.connection.commit()

                            # pemasukan data siswa baru ke dalam database siswa_smp jika tingkat siswa adalah smp
                            elif tingkat == "SMP":
                                cursor.execute('INSERT IGNORE INTO siswa_smp (nis, nisn, nama_siswa, jenis_kelamin, kelas, status, foto_path) VALUES (%s, %s, %s, %s, %s, %s, %s)', (nis, nisn, nama_siswa, jenis_kelamin, kelas, status, nama_foto))
                                mysql.connection.commit()
                        return redirect('/manajemen_siswa')

                # instruksi yang dijalankan ketika request method GET
                elif request.method == 'GET':

                    # render template tambah_siswa.html
                    return render_template('tambahdatasiswa.html')

    # jika user belum login, maka user akan diredirect ke halaman login
    return redirect('/login')

@app.route('/ubah_siswa/<nis>', methods=['GET', 'POST'])
def ubah_siswa(nis):
    # halaman ubah siswa
    # jika user sudah login, maka user tidak akan diredirect ke halaman login
    if 'loggedin' in session:

        # instruksi yang dijalankan ketika akun memiliki otoritas staff atau admin
        if session['otoritas'] == 'Staff' or session['otoritas'] == 'Admin':
            # instruksi yang dijalankan ketika request method POST
            if request.method == 'POST':
                # pengambilan data siswa dari form

                # nis siswa
                nis = request.form['nis']
                
                # nisn siswa
                nisn = request.form['nisn']

                # nama siswa
                nama_siswa = request.form['nama_siswa']

                # jenis kelamin siswa
                jenis_kelamin = request.form['jenis_kelamin']

                # kelas siswa
                kelas = request.form['kelas']

                # status siswa
                status = request.form['status']
                
                # pembaruan data siswa ke database
                with mysql.connection.cursor() as cursor:
                    
                    # pengecekan jika tingkat siswa adalah tk
                    cursor.execute('SELECT nis FROM siswa_tk WHERE nis = %s', ([nis]))
                    siswa = cursor.fetchone()
                    if siswa:
                        cursor.execute('UPDATE IGNORE siswa_tk SET nama_siswa = %s, jenis_kelamin = %s, kelas = %s, status = %s, nisn = %s WHERE nis = %s', (nama_siswa, jenis_kelamin, kelas, status, nisn, nis))
                        mysql.connection.commit()
                    
                    elif not siswa:
                        # pengecekan jika tingkat siswa adalah sd
                        cursor.execute('SELECT nis FROM siswa_sd WHERE nis = %s', ([nis]))
                        siswa = cursor.fetchone()
                        if siswa:
                            cursor.execute('UPDATE IGNORE siswa_sd SET nama_siswa = %s, jenis_kelamin = %s, kelas = %s, status = %s, nisn = %s WHERE nis = %s', (nama_siswa, jenis_kelamin, kelas, status, nisn, nis))
                            mysql.connection.commit()

                        elif not siswa:
                            # pengecekan jika tingkat siswa adalah smp
                            cursor.execute('SELECT nis FROM siswa_smp WHERE nis = %s', ([nis]))
                            siswa = cursor.fetchone()
                            if siswa:
                                cursor.execute('UPDATE IGNORE siswa_smp SET nama_siswa = %s, jenis_kelamin = %s, kelas = %s, status = %s, nisn = %s WHERE nis = %s', (nama_siswa, jenis_kelamin, kelas, status, nisn, nis))
                                mysql.connection.commit()

                # redirect ke halaman manajemen siswa
                return redirect('/manajemen_siswa')
            
            # instruksi yang dijalankan ketika request method GET
            elif request.method == 'GET':

                # inisialisasi tingkat siswa
                tingkat = ""

                # pengambilan data siswa dari database
                with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                    # pengambilan data siswa berdasarkan nis
                    
                    # pengecekan apakah nis siswa ada di database siswa_tk
                    cursor.execute('SELECT * FROM siswa_tk WHERE nis = %s', ([nis]))
                    siswa = cursor.fetchone()
                    tingkat = "TK"

                    # instruksi yang dilakukan jika siswa tidak ditemukan di database siswa_tk
                    if not siswa:
                        # pengecekan apakah nis siswa ada di database siswa_sd
                        cursor.execute('SELECT * FROM siswa_sd WHERE nis = %s', ([nis]))
                        siswa = cursor.fetchone()
                        tingkat = "SD"

                        # instruksi yang dilakukan jika siswa tidak ditemukan di database siswa_sd
                        if not siswa:
                            # pengecekan apakah nis siswa ada di database siswa_smp
                            cursor.execute('SELECT * FROM siswa_smp WHERE nis = %s', ([nis]))
                            siswa = cursor.fetchone()
                            tingkat = "SMP"

                # render template ubahdatasiswa.html dengan data siswa
                return render_template('ubahdatasiswa.html',siswa=siswa, tingkat=tingkat)

    # jika user belum login, maka user akan diredirect ke halaman login
    return redirect('/login')

@app.route('/hapus_siswa/<nis>', methods=['GET', 'POST'])
def hapus_siswa(nis):
    # halaman hapus siswa
    # jika user sudah login, maka user tidak akan diredirect ke halaman login
    if 'loggedin' in session:

        # instruksi yang dijalankan ketika akun memiliki otoritas staff atau admin
        if session['otoritas'] == 'Staff' or session['otoritas'] == 'Admin':
            
            #  penghapusan data siswa dari database
            with mysql.connection.cursor() as cursor:
                # penghapusan data siswa berdasarkan nis

                # pengecekan apakah nis siswa ada di database siswa_tk
                cursor.execute('DELETE IGNORE FROM siswa_tk WHERE nis = %s', ([nis]))
                mysql.connection.commit()

                # pengecekan apakah nis siswa ada di database siswa_sd
                cursor.execute('DELETE IGNORE FROM siswa_sd WHERE nis = %s', ([nis]))
                mysql.connection.commit()

                # pengecekan apakah nis siswa ada di database siswa_smp
                cursor.execute('DELETE IGNORE FROM siswa_smp WHERE nis = %s', ([nis]))
                mysql.connection.commit()

            # redirect ke halaman manajemen siswa
            return redirect('/manajemen_siswa')
    
    # jika user belum login, maka user akan diredirect ke halaman login
    return redirect('/login')

@app.route('/riwayat_pembayaran/<nis>', methods=['GET'])
def riwayat_pembayaran(nis):
    # halaman riwayat pembayaran
    # jika user sudah login, maka user tidak akan diredirect ke halaman login
    if 'loggedin' in session:

        # instruksi yang dijalankan ketika akun memiliki otoritas staff atau admin
        if session['otoritas'] == 'Staff' or session['otoritas'] == 'Admin':

            # instruksi yang dijalankan ketika request method GET
            if request.method == 'GET':

                # Pengecekan dan pengambilan data siswa dari database jika nis siswa ada di database siswa_tk
                with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                    cursor.execute('SELECT * FROM siswa_sd where nis = %s', ([nis]))
                    data_siswa = cursor.fetchone()
                    
                # jika data siswa ditemukan di database siswa_sd
                if data_siswa:
                    
                    # pengambilan data pembayaran siswa sd dari database pembayaran_sd
                    with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                        cursor.execute('SELECT * FROM pembayaran_sd where nis = %s ORDER by waktu_pembayaran DESC', ([nis]))
                        data_pembayaran = cursor.fetchall()

                        # pengambilan data tagihan siswa sd dari database tagihan_sd
                        cursor.execute('SELECT * FROM tagihan_sd where nis = %s ORDER by tagihan_bulan ASC', ([nis]))
                        tagihan_siswa = cursor.fetchall()      
                
                # jika data siswa tidak ditemukan di database siswa_sd 
                elif not data_siswa:

                    # pengecekan dan pengambilan data siswa dari database jika nis siswa ada di database siswa_smp
                    with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                        cursor.execute('SELECT * FROM siswa_smp where nis = %s', ([nis]))
                        data_siswa = cursor.fetchone()
                    
                    # jika data siswa ditemukan di database siswa_smp
                    if data_siswa:

                        with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                            # pengambilan data pembayaran siswa smp dari database pembayaran_smp
                            cursor.execute('SELECT * FROM pembayaran_smp where nis = %s', ([nis]))
                            data_pembayaran = cursor.fetchall()

                            # pengambilan data tagihan siswa smp dari database tagihan_smp
                            cursor.execute('SELECT * FROM tagihan_smp where nis = %s', ([nis]))
                            tagihan_siswa = cursor.fetchall()    
                                    
                    # jika data siswa tidak ditemukan di database siswa_smp
                    elif not data_siswa:

                        # pengecekan dan pengambilan data siswa dari database jika nis siswa ada di database siswa_tk
                        with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                            cursor.execute('SELECT * FROM siswa_tk where nis = %s', ([nis]))
                            data_siswa = cursor.fetchone()
                        
                        # jika data siswa ditemukan di database siswa_tk
                        if data_siswa:

                            # pengambilan data pembayaran siswa tk dari database pembayaran_tk
                            with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                                cursor.execute('SELECT * FROM pembayaran_tk where nis = %s', ([nis]))
                                data_pembayaran = cursor.fetchall()

                                # pengambilan data tagihan siswa tk dari database tagihan_tk
                                cursor.execute('SELECT * FROM tagihan_tk where nis = %s', ([nis]))
                                tagihan_siswa = cursor.fetchall()  
                
                #Render tabel-pembayaran.html jika ada request dari client
                return render_template('riwayat_pembayaran.html', siswa=data_siswa, spp=data_pembayaran, tagihan=tagihan_siswa)

    # jika user belum login, maka user akan diredirect ke halaman login
    return redirect('/login')

@app.route('/pembayaran_spp/<nis>', methods=['GET','POST'])
def pembayaran_spp(nis):
    # halaman pembayaran spp
    # jika user sudah login, maka user tidak akan diredirect ke halaman login
    if 'loggedin' in session:
        # instruksi yang dijalankan ketika akun memiliki otoritas staff atau admin
        if session['otoritas'] == 'Staff' or session['otoritas'] == 'Admin':
                
                # instruksi yang dijalankan ketika request method GET
                if request.method == 'GET':
    
                    # Pengecekan dan pengambilan data siswa dari database jika nis siswa ada di database siswa_sd
                    with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                        cursor.execute('SELECT * FROM siswa_sd where nis = %s', ([nis]))
                        data_siswa = cursor.fetchone()
                        
                    # jika data siswa ditemukan di database siswa_sd
                    if data_siswa:
                        
                        # pengambilan data tagihan siswa sd dari database tagihan_sd
                        with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                            cursor.execute('SELECT * FROM tagihan_sd where nis = %s', ([nis]))
                            data_tagihan = cursor.fetchall()

                    # jika data siswa tidak ditemukan di database siswa_sd
                    elif not data_siswa:
                            
                            # pengecekan dan pengambilan data siswa dari database jika nis siswa ada di database siswa_smp
                            with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                                cursor.execute('SELECT * FROM siswa_smp where nis = %s', ([nis]))
                                data_siswa = cursor.fetchone()
                            
                            # jika data siswa ditemukan di database siswa_smp
                            if data_siswa:
                                
                                # pengambilan data tagihan siswa smp dari database tagihan_smp
                                with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                                    cursor.execute('SELECT * FROM tagihan_smp where nis = %s', ([nis]))
                                    data_tagihan = cursor.fetchall()

                            # jika data siswa tidak ditemukan di database siswa_smp
                            elif not data_siswa:
                                        
                                # pengecekan dan pengambilan data siswa dari database jika nis siswa ada di database siswa_tk
                                with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                                    cursor.execute('SELECT * FROM siswa_tk where nis = %s', ([nis]))
                                    data_siswa = cursor.fetchone()

                                # jika data siswa ditemukan di database siswa_tk
                                if data_siswa:
                                        
                                        # pengambilan data tagihan siswa tk dari database tagihan_tk
                                        with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                                            cursor.execute('SELECT * FROM tagihan_tk where nis = %s', ([nis]))
                                            data_tagihan = cursor.fetchall()                           

                #Render tabel-pembayaran.html jika ada request dari client
                return render_template('pembayaran.html', siswa=data_siswa, tagihan=data_tagihan)

    # jika user belum login, maka user akan diredirect ke halaman login
    return redirect('/login')

@app.route('/manajemen_pegawai', methods=['GET','POST'])
def manajemen_pegawai():
    # halaman manajemen staff
    # jika user sudah login, maka user tidak akan diredirect ke halaman login
    if 'loggedin' in session:
        # instruksi yang dijalankan ketika akun memiliki otoritas staff atau admin
        if session['otoritas'] == 'Staff' or session['otoritas'] == 'Admin':
                
                # instruksi yang dijalankan ketika request method GET
                if request.method == 'GET':
    
                    # Pengecekan dan pengambilan data staff dari database jika nis siswa ada di database siswa_sd
                    with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                        cursor.execute('SELECT pegawai.nip, pegawai.nama_pegawai, pegawai.jenis_kelamin, pegawai.status, pegawai.jabatan, user.otoritas FROM pegawai LEFT JOIN user ON pegawai.nip = user.nip')
                        data_pegawai = cursor.fetchall()
                        
                #Render tabel-pegawai.html jika ada request dari client
                return render_template('tabelpegawai.html', pegawai=data_pegawai)

    # jika user belum login, maka user akan diredirect ke halaman login
    return redirect('/login')

@app.route('/tambah_pegawai', methods=['GET','POST'])
def tambah_pegawai():
    # halaman tambah staff
    # jika user sudah login, maka user tidak akan diredirect ke halaman login
    if 'loggedin' in session:
        # instruksi yang dijalankan ketika akun memiliki otoritas staff atau admin
        if session['otoritas'] == 'Staff' or session['otoritas'] == 'Admin':
                
                # instruksi yang dijalankan ketika request method GET
                if request.method == 'GET':
                        
                    #Render tabel-pegawai.html jika ada request dari client
                    return render_template('tambahdatapegawai.html')

                # instruksi yang dijalankan ketika request method POST
                elif request.method == 'POST':
                # pengambilan data pegawai baru dari form

                    # pengambilan data nip dari form
                    nip = request.form['nip']

                    # pengambilan data nama dari form
                    nama = request.form['nama_pegawai']

                    # pengambilan data jenis kelamin dari form
                    jenis_kelamin = request.form['jenis_kelamin']

                    # pengambilan data status dari form
                    status = request.form['status']

                    # pengambilan data unit dari form
                    unit = request.form['unit']

                    # pengambilan data jabatan dari form
                    jabatan = request.form['jabatan']

                    # pengambilan data otoritas dari form
                    otoritas = request.form['otoritas']

                    # foto pegawai
                    foto_profil = request.files['foto_pegawai']
                    nama_foto = str(foto_profil.filename)
                    if foto_profil:
                        foto_profil.save(os.path.join(app.config['UPLOAD_FOLDER'], nama_foto))
                    else:
                        nama_foto = 'default.jpg'

                    with mysql.connection.cursor() as cursor:
                        # pemasukan data pegawai baru ke database
                        cursor.execute('INSERT IGNORE INTO pegawai (nip, nama_pegawai, jenis_kelamin, status, unit, jabatan, foto_path) VALUES (%s, %s, %s, %s, %s, %s, %s)', (nip, nama, jenis_kelamin, status, unit, jabatan, nama_foto))
                        mysql.connection.commit()

                    if not otoritas == 'None':
                        # pengambilan data username dari form
                        username = request.form['username']

                        # pengambilan data password dari form
                        password = request.form['password']

                        with mysql.connection.cursor() as cursor:
                            # pemasukan data user baru ke database
                            cursor.execute('INSERT IGNORE INTO user (nip, username, password, otoritas) VALUES (%s, %s, %s, %s)', (nip, username, password, otoritas))
                            mysql.connection.commit()

                    # mengalihkan ke halaman manajemen staff
                    return redirect('/manajemen_pegawai')

    # jika user belum login, maka user akan diredirect ke halaman login
    return redirect('/login')

@app.route('/detail_pegawai/<nip>', methods=['GET','POST'])
def detail_pegawai(nip):
    # halaman detail pegawai
    # jika user sudah login, maka user tidak akan diredirect ke halaman login
    if 'loggedin' in session:
        # instruksi yang dijalankan ketika akun memiliki otoritas staff atau admin
        if session['otoritas'] == 'Staff' or session['otoritas'] == 'Admin':
                
                # instruksi yang dijalankan ketika request method GET
                if request.method == 'GET':
    
                    # Pengecekan dan pengambilan data staff dari database jika nis siswa ada di database siswa_sd
                    with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                        cursor.execute('SELECT pegawai.nip, pegawai.nama_pegawai, pegawai.jenis_kelamin, pegawai.status, pegawai.unit, pegawai.jabatan, pegawai.foto_path,user.otoritas, user.username, user.password FROM pegawai LEFT JOIN user ON pegawai.nip = user.nip WHERE pegawai.nip = %s', ([nip]))
                        data_pegawai = cursor.fetchone()
                        
                #Render tabel-pegawai.html jika ada request dari client
                return render_template('datapegawai.html', pegawai=data_pegawai)

    # jika user belum login, maka user akan diredirect ke halaman login
    return redirect('/login')

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host='0.0.0.0',port=2431 ,debug=True)