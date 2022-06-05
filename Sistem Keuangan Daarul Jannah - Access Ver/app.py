from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from datetime import *
# from db_update_tagihan import update_tagihan_sd
import os
import MySQLdb.cursors

#get date
current_date = datetime.now()
datem = datetime.strptime(str(current_date), '%Y-%m-%d')

# inisiasi variabel aplikasi
app = Flask(__name__)


#Koneksi, inisialisasi DB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'nilaraya'
mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def function():
    if not 'loggedin' in session:
        pass
    return redirect(url_for('dashboard'))

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