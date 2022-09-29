from flask import Flask, render_template, request, flash
from hashlib import sha384
from uuid import uuid4
import sqlite3

def init_db():
    db = sqlite3.connect('users.db')
    with open('schema.sql', 'r') as schema:
        db.executescript(schema.read())
    db.commit()

def init_secret_key():
    secret_key = uuid4().hex + uuid4().hex
    with open('.secretkey', 'w') as sk_fp:
        sk_fp.write(secret_key)
    app.secret_key = secret_key

def get_secret_key():
    try:
        with open('.secretkey', 'r') as sk_fp:
            return sk_fp.read()
    except FileNotFoundError as e:
        init_secret_key()
        print("Initialised secret key")

app = Flask(__name__)
app.secret_key = get_secret_key()


@app.cli.command('init_app')
def init_app_cmd():
    init_db()
    print("Initialised database.")

def get_db():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html', title='Home')


@app.route('/signin', methods=('GET', 'POST'))
def signin():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        user = db.execute(
            'SELECT password FROM users WHERE username = ?', (username, )
        ).fetchone()
        
        if user is None:
            error = 'Incorrect Username/Password.'
        elif user[0] != sha384(password.encode()).hexdigest():
            error = 'Incorrect Password.'

        if error is None:
            return render_template('index.html', title="Home", succ="Sign In Successful!")
        flash(error)
        db.close()

    return render_template('signin.html', title='Sign In', error=error)


@app.route('/signup', methods=('POST', 'GET'))
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        curr = db.cursor()
        
        curr.execute(
            'INSERT INTO users (username, password) VALUES (?, ?);', (username, sha384(password.encode()).hexdigest())
        )
        db.commit()
        curr.close()
        db.close()
        return render_template('index.html', title="Home", succ="Registration Successful!")
        

    return render_template('signup.html', title='Sign Up')
