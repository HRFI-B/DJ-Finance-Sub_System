# library import
from flask import Flask,render_template,url_for, request,jsonify
from werkzeug.utils import redirect
import pyodbc

#inisialisasi variabel app
app = Flask(__name__)

#Koneksi ke basis data
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\ihzaf\OneDrive\Documents\Project\DJ-Finance-Sub_Sistem\Sistem Keuangan Daarul Jannah - Access Ver\Database\sk_dj.accdb;')
cursor = conn.cursor()

#Direct to /login
@app.route('/', methods=['POST', 'GET'])
def function():
    return redirect('/login')

#Backend laman Login
@app.route('/login', methods=['POST', 'GET'])
def login():
    log_stat = ""
    #Pengambilan data dari Form Login.html (NIP, Password)
    if request.method == 'POST':
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
                log_stat= "true"
                #Pengalihan ke laman home
                return redirect('/home')

            #Algoritma ketika NIP tidak ditemukan
            elif Verify_ID == None:
                print("\nWrong ID!")
                if log_stat == "" or log_stat == "false":
                    log_stat = "false"
                    return redirect('/login')
                
            #Algoritma ketika NIP tidak ditemukan
            elif not Verify_Pass == password:
                print("\nWrong Password!")
                if log_stat == "" or log_stat == "false":
                    log_stat = "false"
                    return redirect('/login')
        
        #jika ada error dalam masukan data
        except ValueError:
            return 'There was an issue'
    else:
        #Render login.html jika ada request dari client
        return render_template('login.html')

#Backend laman pengecekan pembayaran siswa
@app.route('/pengecekan_pembayaran_siswa', methods=['POST', 'GET'])
def pengecekan_pembayaran_siswa():
    if request.method == 'POST':
        nis = request.form['nis']

        cursor.execute(f'SELECT Nama FROM data_siswa where nis = \'{nis}\'')
        result = cursor.fetchall()
        for x in result:
            nama = x[0]
        if not nama == None:
            print(nama)
            return render_template('cek_pembayaran.html')
        else:
            print("Wrong ID")
            return render_template('cek_pembayaran.html')
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
    app.run(host='192.168.0.145', port=8080, debug=True)