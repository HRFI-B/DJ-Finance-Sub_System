from flask import Flask,render_template,url_for, request,jsonify
from werkzeug.utils import redirect
import pyodbc

app = Flask(__name__)

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\ihzaf\OneDrive\Documents\Project\DJ-Finance-Sub_Sistem\Sistem Keuangan Daarul Jannah - Access Ver\Database\sk_dj.accdb;')
cursor = conn.cursor()

@app.route('/', methods=['POST', 'GET'])
def function():
    return redirect('/login')

@app.route('/login', methods=['POST', 'GET'])
def login():
    log_stat = ""
    if request.method == 'POST':
        id = request.form['ID']
        password = request.form['Password']
        try:
            Verify_ID = None
            Verify_Pass = None

            cursor.execute(f'SELECT ID FROM account where ID = \'{id}\'')
            result = cursor.fetchall()
            for x in result:
                Verify_ID = x[0]

            cursor.execute(f'SELECT password FROM account where ID = \'{id}\'')
            result = cursor.fetchall()
            for x in result:
                Verify_Pass = x[0]

            cursor.execute(f'SELECT Otoritas FROM account where ID = \'{id}\'')
            result = cursor.fetchall()
            for x in result:
                Otoritas = x[0]

            if not Verify_ID == None and Verify_Pass == password:
                print("\nLogin Success as ", end = '')
                print(Otoritas, end=' - ')
                print(request.remote_addr)
                log_stat= "true"
                return redirect('/home')

            elif Verify_ID == None:
                print("\nWrong ID!")
                if log_stat == "" or log_stat == "false":
                    log_stat = "false"
                    return redirect('/login')
            elif not Verify_Pass == password:
                print("\nWrong Password!")
                if log_stat == "" or log_stat == "false":
                    log_stat = "false"
                    return redirect('/login')

        except ValueError:
            return 'There was an issue'
    else:
        return render_template('login.html')

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

@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        pass
    else:
        return render_template('home.html')

if __name__ == "__main__": 
    app.run(host='192.168.0.145', port=8080, debug=True)