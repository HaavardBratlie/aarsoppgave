from flask import Flask, render_template, request, session, redirect, url_for
import mysql.connector
import bcrypt

app = Flask(__name__)
app.secret_key = 'abc123'

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

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quiz_scores (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            quiz_name VARCHAR(255) NOT NULL,
            score INT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES brukere(id)
        )
    ''')

    conn.commit()
    cursor.close()
    conn.close()

init_db()


@app.route('/')
def home():
    if 'user_id' in session:
        return render_template('index.html', logged_in=True)
    return render_template('index.html', logged_in=False)

@app.route('/ommeg')
def ommeg_page():
    if 'user_id' in session:
        return render_template('ommeg.html', logged_in=True)
    return render_template('ommeg.html', logged_in=False)

@app.route('/innhold')
def innhold_page():
    if 'user_id' in session:
        return render_template('innhold.html', logged_in=True)
    return render_template('innhold.html', logged_in=False)

@app.route('/quiz_hub')
def quiz_hub_page():
    if 'user_id' in session:
        return render_template('quiz_hub.html', logged_in=True)
    return render_template('quiz_hub.html', logged_in=False)

@app.route('/quiz')
def quiz_page():
    if 'user_id' in session:
        return render_template('quiz.html', logged_in=True)
    return render_template('quiz.html', logged_in=False)

@app.route('/quiz2')
def quiz2_page():
    if 'user_id' in session:
        return render_template('quiz2.html', logged_in=True)
    return render_template('quiz2.html', logged_in=False)

@app.route('/registrer', methods=['GET', 'POST'])
def registrer_page():
    if request.method == 'POST':
        fornavn = request.form['fornavn']
        etternavn = request.form['etternavn']
        epost = request.form['epost']
        passord = request.form['passord']

        hashed_password = bcrypt.hashpw(passord.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        conn = None
        cursor = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO brukere (fornavn, etternavn, epost, passord)
                VALUES (%s, %s, %s, %s)
            ''', (fornavn, etternavn, epost, hashed_password))
            conn.commit()
            
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        return redirect(url_for("login_page")) #melling om registrerring lykkes

    return render_template('registrer.html')

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        epost = request.form['epost']
        passord = request.form['passord']

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM brukere WHERE epost = %s', (epost,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user and bcrypt.checkpw(passord.encode('utf-8'), user['passord'].encode('utf-8')):
            session['user_id'] = user['id']
            session['user_name'] = user['fornavn']
            return render_template("index.html")
        else:
            return render_template('login.html')  # Add error message for incorrect login
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return render_template("index.html")  

@app.context_processor
def inject_user():
    user_id = session.get('user_id')
    user_name = session.get('user_name')
    return {'user_id': user_id, 'user_name': user_name}


@app.route('/tabell')
def tabell():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Fetch tabell for Quiz 1
    cursor.execute('''
        SELECT b.fornavn, b.etternavn, MAX(q.score) AS best_score
        FROM quiz_scores q
        JOIN brukere b ON q.user_id = b.id
        WHERE q.quiz_name = 'quiz1'
        GROUP BY b.id
        ORDER BY best_score DESC
    ''')
    tabell_quiz1 = cursor.fetchall()

    # Fetch tabell for Quiz 2
    cursor.execute('''
        SELECT b.fornavn, b.etternavn, MAX(q.score) AS best_score
        FROM quiz_scores q
        JOIN brukere b ON q.user_id = b.id
        WHERE q.quiz_name = 'quiz2'
        GROUP BY b.id
        ORDER BY best_score DESC
    ''')
    tabell_quiz2 = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('tabell.html', tabell_quiz1=tabell_quiz1, tabell_quiz2=tabell_quiz2)

@app.route('/submit_result', methods=['POST'])
def submit_result():
    if 'user_id' not in session:
        return "Unauthorized", 401

    user_id = session['user_id']
    score = request.form.get('score')
    quiz_name = "quiz1"

    if score is None:
        return "Score not provided", 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO quiz_scores (user_id, quiz_name, score)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE score = GREATEST(score, VALUES(score))
    ''', (user_id, quiz_name, score))
    conn.commit()
    cursor.close()
    conn.close()

    return "Score submitted successfully", 200

@app.route('/submit_result2', methods=['POST'])
def submit_result2():
    if 'user_id' not in session:
        return "Unauthorized", 401

    user_id = session['user_id']
    score = request.form.get('score')
    quiz_name = "quiz2"

    if score is None:
        return "Score not provided", 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO quiz_scores (user_id, quiz_name, score)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE score = GREATEST(score, VALUES(score))
    ''', (user_id, quiz_name, score))
    conn.commit()
    cursor.close()
    conn.close()

    return "Score submitted successfully", 200

if __name__ == '__main__':  
    app.run(debug=True, host="0.0.0.0", port=2200)