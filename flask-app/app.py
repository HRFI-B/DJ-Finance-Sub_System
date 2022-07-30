from re import S
from flask import Flask, render_template, request, redirect, url_for, session, send_file
from datetime import *
from flask_mysqldb import MySQL
import MySQLdb.cursors
from threading import Thread
import pandas.io.sql as psql

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
    
    # Inisialisasi MySQL
    # app.config['MYSQL_PORT'] = 25060

    mysql = MySQL(app)
    return mysql


# inisiasi variabel aplikasi
app = Flask(__name__)
mysql = connect_db()

app.config['UPLOAD_FOLDER'] = 'static/foto_siswa'

@app.route('/', methods=['GET', 'POST'])
def function():
    if not 'loggedin' in session:
        return redirect(url_for('login'))
    return redirect(url_for('home'))

@app.route('/login', methods=['POST', 'GET'])
def login():    
    msg = ''
    
    session['year'] = date.today().year
    session['datetime'] = datetime.now()
    
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

                # menyimpan data tanggal
                session['tanggal'] = datetime.now().strftime("%d-%m-%Y")
                
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

        # instruksi yang dijalankan ketika akun memiliki otoritas admin atau staff
        if session['otoritas'] == 'Admin' or session['otoritas'] == 'Staff':

            # pengambilan semua data siswa dari database
            with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:

                # pengambilan data siswa tk
                cursor.execute('SELECT * FROM siswa')
                siswa = cursor.fetchall()

            # render template manajemen_siswa.html dengan data siswa
            return render_template('tabelsiswa.html',siswa=siswa)
    
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
                cursor.execute('SELECT * FROM siswa WHERE nis = %s', ([nis]))
                siswa = cursor.fetchone()
            
            # render template detail_siswa.html dengan data siswa
            return render_template('datasiswa.html',siswa=siswa)

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
                        # foto_profil = request.files['foto_siswa']
                        # nama_foto = str(foto_profil.filename)
                        # if foto_profil:
                        #     foto_profil.save(os.path.join(app.config['UPLOAD_FOLDER'], nama_foto))
                        # else:
                        #     nama_foto = 'default.jpg'

                        # pemasukan data siswa baru ke database
                        with mysql.connection.cursor() as cursor:
                                cursor.execute('INSERT IGNORE INTO siswa (nis, nisn, nama_siswa, jenis_kelamin, kelas, status, tingkat) VALUES (%s, %s, %s, %s, %s, %s, %s)', (nis, nisn, nama_siswa, jenis_kelamin, kelas, status, tingkat))
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

                # tingkat siswa
                tingkat = request.form['tingkat']
                
                # pembaruan data siswa ke database
                with mysql.connection.cursor() as cursor:
                    
                    # pengecekan jika tingkat siswa adalah tk
                    cursor.execute('SELECT nis FROM siswa WHERE nis = %s', ([nis]))
                    siswa = cursor.fetchone()
                    if siswa:
                        cursor.execute('UPDATE IGNORE siswa SET nama_siswa = %s, jenis_kelamin = %s, kelas = %s, status = %s, nisn = %s, tingkat = %s WHERE nis = %s', (nama_siswa, jenis_kelamin, kelas, status, nisn, tingkat, nis))
                        mysql.connection.commit()

                # redirect ke halaman manajemen siswa
                return redirect('/manajemen_siswa')
            
            # instruksi yang dijalankan ketika request method GET
            elif request.method == 'GET':

                # pengambilan data siswa dari database
                with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                    # pengambilan data siswa berdasarkan nis
                    
                    cursor.execute('SELECT * FROM siswa WHERE nis = %s', ([nis]))
                    siswa = cursor.fetchone()

                # render template ubahdatasiswa.html dengan data siswa
                return render_template('ubahdatasiswa.html',siswa=siswa)

    # jika user belum login, maka user akan diredirect ke halaman login
    return redirect('/login')

@app.route('/hapus_siswa/<nis>', methods=['GET', 'POST'])
def hapus_siswa(nis):
    # halaman hapus siswa
    # jika user sudah login, maka user tidak akan diredirect ke halaman login
    if 'loggedin' in session:

        # instruksi yang dijalankan ketika akun memiliki otoritas staff atau admin
        if session['otoritas'] == 'Admin':
            
            #  penghapusan data siswa dari database
            with mysql.connection.cursor() as cursor:
                # penghapusan data siswa berdasarkan nis

                cursor.execute('DELETE IGNORE FROM siswa WHERE nis = %s', ([nis]))
                mysql.connection.commit()

            # redirect ke halaman manajemen siswa
            return redirect('/manajemen_siswa')
    
    # jika user belum login, maka user akan diredirect ke halaman login
    return redirect('/login')

@app.route('/riwayat_pembayaran/<nis>', methods=['GET', 'POST'])
def riwayat_pembayaran(nis):
    # halaman riwayat pembayaran
    # jika user sudah login, maka user tidak akan diredirect ke halaman login
    if 'loggedin' in session:

        # instruksi yang dijalankan ketika akun memiliki otoritas staff atau admin
        if session['otoritas'] == 'Staff' or session['otoritas'] == 'Admin':

            # instruksi yang dijalankan ketika request method GET
            if request.method == 'GET':

                # Pengecekan dan pengambilan data siswa dari database jika nis siswa ada di database siswa
                with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                    cursor.execute('SELECT * FROM siswa where nis = %s', ([nis]))
                    data_siswa = cursor.fetchone()
                    
                # jika data siswa ditemukan di database siswa
                if data_siswa:
                    
                    # pengambilan data pembayaran siswa dari database pembayaran
                    with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                        cursor.execute('SELECT * FROM pembayaran where nis = %s ORDER by waktu_pembayaran DESC', ([nis]))
                        data_pembayaran = cursor.fetchall()

                        # pengambilan data tagihan siswa dari database tagihan
                        # cursor.execute('SELECT * FROM tagihan_sd where nis = %s ORDER by tagihan_bulan ASC', ([nis]))
                        # tagihan_siswa = cursor.fetchall()   

                    tahun_ajaran = "Semua Tahun Ajaran"
                #Render tabel-pembayaran.html jika ada request dari client
                return render_template('riwayat_pembayaran.html', siswa=data_siswa, pembayaran=data_pembayaran, tahun_ajaran=tahun_ajaran)
            
            elif request.method == 'POST':
                tahun_ajaran = request.form['tahun_ajaran']
                # Pengecekan dan pengambilan data siswa dari database jika nis siswa ada di database siswa_tk
                with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                    cursor.execute('SELECT * FROM siswa where nis = %s', ([nis]))
                    data_siswa = cursor.fetchone()
                    
                # jika data siswa ditemukan di database siswa
                if data_siswa:
                    
                    # pengambilan data pembayaran siswa dari database pembayaran
                    with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                        cursor.execute('SELECT * FROM pembayaran where nis = %s AND pembayaran_periode_ta =%s ORDER by waktu_pembayaran DESC', ([nis], tahun_ajaran))
                        data_pembayaran = cursor.fetchall()

                #Render tabel-pembayaran.html jika ada request dari client
                return render_template('riwayat_pembayaran.html', siswa=data_siswa, pembayaran=data_pembayaran, tahun_ajaran=tahun_ajaran)
            

    # jika user belum login, maka user akan diredirect ke halaman login
    return redirect('/login')

@app.route('/pembayaran_siswa/<nis>', methods=['GET','POST'])
def pembayaran_siswa(nis):
    # halaman pembayaran
    # jika user sudah login, maka user tidak akan diredirect ke halaman login
    if 'loggedin' in session:
        # instruksi yang dijalankan ketika akun memiliki otoritas staff atau admin
        if session['otoritas'] == 'Staff' or session['otoritas'] == 'Admin':
                
                # instruksi yang dijalankan ketika request method GET
                if request.method == 'GET':
    
                    # Pengecekan dan pengambilan data siswa dari database jika nis siswa ada di database siswa
                    with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                        cursor.execute('SELECT * FROM siswa where nis = %s', ([nis]))
                        data_siswa = cursor.fetchone()       

                    #Render tabel-pembayaran.html jika ada request dari client
                    return render_template('pembayaran.html', siswa=data_siswa)

                # instruksi yang dijalankan ketika request method POST
                elif request.method == 'POST':

                    # Penentuan jenjang siswa
                    # Pengecekan dan pengambilan data siswa dari database jika nis siswa ada di database siswa
                    with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                        cursor.execute('SELECT nis FROM siswa where nis = %s', ([nis]))
                        data_siswa = cursor.fetchone()

                    # pengambilan data dari form pembayaran
                    pembayaran_periode_bulan = request.form['periode_bulan']
                    pembayaran_periode_ta = request.form['periode_ta']
                    waktu_pembayaran = datetime.now()

                    pembayaran_total = 0

                    pembayaran_spp = request.form['nominal_spp']
                    if not pembayaran_spp:
                        pembayaran_spp = 0
                    else:
                        pembayaran_spp = int(pembayaran_spp)
                        pembayaran_total += pembayaran_spp

                    pembayaran_tabungan_wajib = request.form['nominal_tabungan_wajib']
                    if not pembayaran_tabungan_wajib:
                        pembayaran_tabungan_wajib = 0
                    else:
                        pembayaran_tabungan_wajib = int(pembayaran_tabungan_wajib)
                        pembayaran_total += pembayaran_tabungan_wajib

                    pembayaran_katering = request.form['nominal_katering']
                    if not pembayaran_katering:
                        pembayaran_katering = 0
                    else:
                        pembayaran_katering = int(pembayaran_katering)
                        pembayaran_total += pembayaran_katering

                    pembayaran_jemputan = request.form['nominal_jemputan']
                    if not pembayaran_jemputan:
                        pembayaran_jemputan = 0
                    else:
                        pembayaran_jemputan = int(pembayaran_jemputan)
                        pembayaran_total += pembayaran_jemputan

                    pembayaran_ekskul = request.form['nominal_ekskul']
                    if not pembayaran_ekskul:
                        pembayaran_ekskul = 0
                    else:
                        pembayaran_ekskul = int(pembayaran_ekskul)
                        pembayaran_total += pembayaran_ekskul

                    pembayaran_majelis_sekolah = request.form['nominal_majelis_sekolah']
                    if not pembayaran_majelis_sekolah:
                        pembayaran_majelis_sekolah = 0
                    else:
                        pembayaran_majelis_sekolah = int(pembayaran_majelis_sekolah)
                        pembayaran_total += pembayaran_majelis_sekolah

                    pembayaran_kelas_berbakat = request.form['nominal_kelas_berbakat']
                    if not pembayaran_kelas_berbakat:
                        pembayaran_kelas_berbakat = 0
                    else:
                        pembayaran_kelas_berbakat = int(pembayaran_kelas_berbakat)
                        pembayaran_total += pembayaran_kelas_berbakat

                    pembayaran_bimbel = request.form['nominal_bimbel']
                    if not pembayaran_bimbel:
                        pembayaran_bimbel = 0
                    else:
                        pembayaran_bimbel = int(pembayaran_bimbel)
                        pembayaran_total += pembayaran_bimbel

                    # pembayaran_total = "{:,}".format(pembayaran_total)

                    with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                        cursor.execute('INSERT IGNORE INTO pembayaran (nis, pembayaran_periode_bulan, pembayaran_periode_ta, waktu_pembayaran, spp, tabungan_wajib, katering, jemputan, ekskul, majelis_sekolah, kelas_berbakat, bimbel, total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (nis, pembayaran_periode_bulan, pembayaran_periode_ta, waktu_pembayaran, pembayaran_spp, pembayaran_tabungan_wajib, pembayaran_katering, pembayaran_jemputan, pembayaran_ekskul, pembayaran_majelis_sekolah, pembayaran_kelas_berbakat, pembayaran_bimbel, pembayaran_total))
                        mysql.connection.commit()
                        # pembayaran = 'SELECT * FROM pembayaran WHERE nis = {} AND waktu_pembayaran = "{}"'.format(nis, waktu_pembayaran.strftime("%d-%m-%Y"))
                        # print(pembayaran)
                        # df = psql.read_sql(pembayaran, con = mysql.connection)
                        # df.to_excel('./data_export/{}_pembayaran_{}.xlsx'.format(nis,waktu_pembayaran.strftime("%d-%m-%Y")), index=False)
                        # return send_file("./data_export/{}_pembayaran_{}.xlsx".format(nis,waktu_pembayaran.strftime("%d-%m-%Y")), as_attachment=True)

                    return redirect('/manajemen_siswa')

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
    
                    # Pengecekan dan pengambilan data staff dari database jika nip pegawai ada di database pegawai
                    with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                        cursor.execute('SELECT pegawai.nip, pegawai.nama_pegawai, pegawai.jenis_kelamin, pegawai.status, pegawai.unit, pegawai.jabatan, user.otoritas FROM pegawai LEFT JOIN user ON pegawai.nip = user.nip')
                        data_pegawai = cursor.fetchall()
                        
                #Render tabel-pegawai.html jika ada request dari client
                return render_template('tabelpegawai.html', pegawai=data_pegawai)

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
                    # foto_profil = request.files['foto_pegawai']
                    # nama_foto = str(foto_profil.filename)
                    # if foto_profil:
                    #     foto_profil.save(os.path.join(app.config['UPLOAD_FOLDER'], nama_foto))
                    # else:
                    #     nama_foto = 'default.jpg'

                    with mysql.connection.cursor() as cursor:
                        # pemasukan data pegawai baru ke database
                        cursor.execute('INSERT IGNORE INTO pegawai (nip, nama_pegawai, jenis_kelamin, status, unit, jabatan) VALUES (%s, %s, %s, %s, %s, %s)', (nip, nama, jenis_kelamin, status, unit, jabatan))
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

@app.route('/ubah_pegawai/<nip>', methods=['GET','POST'])
def ubah_pegawai(nip):
    # halaman ubah staff
    # jika user sudah login, maka user tidak akan diredirect ke halaman login
    if 'loggedin' in session:
        # instruksi yang dijalankan ketika akun memiliki otoritas staff atau admin
        if session['otoritas'] == 'Admin':
                
                # instruksi yang dijalankan ketika request method GET
                if request.method == 'GET':
    
                    # Pengecekan dan pengambilan data staff dari database jika nis siswa ada di database siswa_sd
                    with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                        cursor.execute('SELECT pegawai.nip, pegawai.nama_pegawai, pegawai.jenis_kelamin, pegawai.status, pegawai.unit, pegawai.jabatan, pegawai.foto_path,user.otoritas, user.username, user.password FROM pegawai LEFT JOIN user ON pegawai.nip = user.nip WHERE pegawai.nip = %s', ([nip]))
                        data_pegawai = cursor.fetchone()
                        
                    #Render tabel-pegawai.html jika ada request dari client
                    return render_template('ubahdatapegawai.html', pegawai=data_pegawai)
            
                # instruksi yang dijalankan ketika request method POST
                elif request.method == 'POST':
                    
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
                    
                    with mysql.connection.cursor() as cursor:
                        # pemasukan data pegawai baru ke database
                        cursor.execute('UPDATE IGNORE pegawai SET nip =%s, nama_pegawai=%s, jenis_kelamin=%s, status=%s, unit=%s, jabatan=%s WHERE nip=%s', ([nip], nama, jenis_kelamin, status, unit, jabatan,nip))
                        mysql.connection.commit()

                    if not otoritas == 'None':
                        # pengambilan data username dari form
                        username = request.form['username']

                        # pengambilan data password dari form
                        password = request.form['password']

                        with mysql.connection.cursor() as cursor:
                            # pemasukan data user baru ke database
                            cursor.execute('UPDATE IGNORE user SET nip=%s, username=%s, password=%s, otoritas=%s WHERE nip=%s', ([nip], username, password, otoritas,nip))
                            mysql.connection.commit()
                    
                    return redirect('/manajemen_pegawai')

    # jika user belum login, maka user akan diredirect ke halaman login
    return redirect('/login')

@app.route('/hapus_pegawai/<nip>', methods=['GET','POST'])
def hapus_pegawai(nip):
    # halaman hapus staff
    # jika user sudah login, maka user tidak akan diredirect ke halaman login
    if 'loggedin' in session:
        # instruksi yang dijalankan ketika akun memiliki otoritas staff atau admin
        if session['otoritas'] == 'Staff' or session['otoritas'] == 'Admin':
                
                # instruksi yang dijalankan ketika request method GET atau POST
                if request.method == 'GET' or request.method == 'POST':
    
                    # Pengecekan dan pengambilan data staff dari database jika nis siswa ada di database siswa_sd
                    with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                        cursor.execute('DELETE IGNORE FROM pegawai WHERE nip = %s', ([nip]))
                        mysql.connection.commit()
                        
                #Redirect ke halaman manajemen staff
                return redirect('/manajemen_pegawai')

    # jika user belum login, maka user akan diredirect ke halaman login
    return redirect('/login')

@app.route('/riwayat_transaksi', methods=['GET','POST'])
def riwayat_transaksi():
    # halaman riwayat transaksi
    # jika user sudah login, maka user tidak akan diredirect ke halaman login
    if 'loggedin' in session:
        # instruksi yang dijalankan ketika akun memiliki otoritas staff atau admin
        if session['otoritas'] == 'Staff' or session['otoritas'] == 'Admin':
                
                # instruksi yang dijalankan ketika request method GET atau POST
                if request.method == 'GET' or request.method == 'POST':
    
                    return render_template('riwayat_transaksi.html')

    # jika user belum login, maka user akan diredirect ke halaman login
    return redirect('/login')

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host='0.0.0.0',port=2431 ,debug=True)