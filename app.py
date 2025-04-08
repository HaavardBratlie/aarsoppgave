from flask import Flask, render_template, request, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

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
    if 'user_id' in session:  # Check if the user is logged in
        return render_template('index.html', logged_in=True)
    return render_template('index.html', logged_in=False)

@app.route('/ommeg')
def ommeg_page():
    if 'user_id' in session:
        return render_template('ommeg.html', logged_in=True)
    return render_template('ommeg.html', logged_in=False)

@app.route('/quiz')
def quiz_page():
    if 'user_id' in session:
        return render_template('quiz.html', logged_in=True)
    return render_template('quiz.html', logged_in=False)

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

        return render_template("login.html") #melling om registrerring lykkes

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
            session['user_id'] = user['id']  # Store user ID in session
            session['user_name'] = user['fornavn']  # Store user's first name in session
            return render_template("index.html")  # Redirect to home page
        else:
            return render_template('login.html')  # Add error message for incorrect login
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()  # Clear all session data
    return render_template("index.html")  # Redirect to home page after logout

@app.context_processor
def inject_user():
    user_id = session.get('user_id')  # Get user_id from session
    user_name = session.get('user_name')  # Get user_name from session
    return {'user_id': user_id, 'user_name': user_name}

if __name__ == '__main__':  
    app.run(debug=True, host="0.0.0.0", port=2200)