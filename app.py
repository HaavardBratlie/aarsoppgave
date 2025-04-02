from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="10.2.3.108",
        user="haavard",
        password="1234567",
        database="portfolio"
    )


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS brukere (
            id INT AUTO_INCREMENT PRIMARY KEY,
            fornavn VARCHAR(255) NOT NULL,
            etternavn VARCHAR(255) NOT NULL,
            epost VARCHAR(255) NOT NULL UNIQUE,
            passord VARCHAR(255) NOT NULL
            )
''')
    conn.commit()
    cursor.close()
    conn.close()

init_db()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/registrer', methods=['GET', 'POST'])
def registrer_page():
    if request.method == 'POST':
        fornavn = request.form['fornavn']
        etternavn = request.form['etternavn']
        epost = request.form['epost']
        passord = request.form['passord']

        conn = None
        cursor = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO brukere (fornavn, etternavn, epost, passord)
                VALUES (%s, %s, %s, %s)
            ''', (fornavn, etternavn, epost, passord))
            conn.commit()
            
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        return redirect(url_for('login_page')) #melling om registrerring lykkes

    return render_template('registrer.html')

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        epost = request.form['epost']
        passord = request.form['passord']

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM brukere WHERE epost = %s AND passord = %s', (epost, passord))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            return render_template('index.html')#legg inn melling innlogging lykkes
        else:
            
            return render_template('login.html')#legg inn melling innlogging feilet
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=2200)