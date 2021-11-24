# library import
from flask import Flask,render_template,url_for, request,jsonify,session
from werkzeug.utils import redirect
import pyodbc
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
    #Pengambilan data dari Form Login.html (NIP, Password)
    if request.method == 'POST':
        # session.pop('id', None)
        id = request.form['nip']
        password = request.form['password']
        try:
            Verify_ID = None
            Verify_Pass = None

            #Pencocokan data NIP masukan dengan NIP di basis data
            cursor.execute(f'SELECT NIP FROM pegawai where NIP = \'{id}\'')
            result = cursor.fetchall()
            for x in result:
                Verify_ID = x[0]

            #Pencocokan data password masukan dengan password pegawai di basis data
            cursor.execute(f'SELECT Password FROM pegawai where NIP = \'{id}\'')
            result = cursor.fetchall()
            for x in result:
                Verify_Pass = x[0]

            #Pengambilan data otoritas pegawai di basis data
            cursor.execute(f'SELECT Otoritas FROM pegawai where NIP = \'{id}\'')
            result = cursor.fetchall()
            for x in result:
                Otoritas = x[0]

            #Algoritma ketika NIP ditemukan di basis data dan password benar
            if not Verify_ID == None and Verify_Pass == password:
                print("\nLogin Success as ", end = '')
                print(Otoritas, end=' - ')
                print(request.remote_addr)
                # session['id'] = Verify_ID
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
    if request.method == 'POST':
        nis = request.form['nis']

        try:
            cursor.execute(f'SELECT Nama FROM siswa_sd where nis = \'{nis}\'')
            result = cursor.fetchall()
            if result == None:
                cursor.execute(f'SELECT Nama FROM siswa_smp where nis = \'{nis}\'')
                result = cursor.fetchall()
                if result == None:
                    cursor.execute(f'SELECT Nama FROM siswa_tk where nis = \'{nis}\'')
                    result = cursor.fetchall()
        except:
            pass
        for x in result:
            nama = x[0]
        # try:
        if not nama == None:
            print(nama)
            return render_template('cek_pembayaran.html')
        else:
            print("Wrong ID")
            return render_template('cek_pembayaran.html')
        # except:
        #     return render_template('cek_pembayaran.html')
    else:
        return render_template('cek_pembayaran.html')

#Backend laman home
@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        pass
    else:
        #Render home.html jika ada request dari client
        return render_template('home.html')

#run program
if __name__ == "__main__": 
    # app.secret_key = 'super secret key'
    # app.config["SESSION_PERMANENT"] = False
    # app.config["SESSION_TYPE"] = "filesystem"
    app.run(host='192.168.0.145', port=8080, debug=True)