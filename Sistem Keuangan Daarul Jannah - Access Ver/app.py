from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import *
from flask_mysqldb import MySQL
import MySQLdb.cursors

#Koneksi, inisialisasi DB
def connect_db():
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'sistem_pembayaran'
    mysql = MySQL(app)
    return mysql

# inisiasi variabel aplikasi
app = Flask(__name__)
mysql = connect_db()

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
                session['loggedin'] = True
                session['username'] = user['username']
                session['otoritas'] = user['otoritas']
                
                # pengambilan data nama pegawai dari database
                nip = user['nip']
                with mysql.connection.cursor(MySQLdb.cursors.DictCursor) as cursor:
                    cursor.execute('SELECT nama_pegawai FROM pegawai where nip = %s', ([nip]))
                    nama = cursor.fetchone()
                session['nama'] = nama['nama_pegawai']
                
                # Redirect to home page
                return redirect(url_for('home'))
            
            # jika username atau password salah
            else:
                msg = 'Incorrect username/password!'
    
    # redirect user ke halaman home jika sudah login 
    elif 'loggedin' in session:
        return redirect(url_for('home'))
    
    #Render login.html jika ada request dari client
    return render_template('Login.html',msg=msg)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/home', methods=['POST', 'GET'])
def home():
    if 'loggedin' in session:
        if session['otoritas'] =='Staff':
            return render_template('home.html')
        elif session['otoritas']=='Admin':
            return render_template('maintenance.html')
    return redirect('/login')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=2431 ,debug=True)