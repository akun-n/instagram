from flask import Flask, request, render_template_string
import sqlite3
import os

app = Flask(__name__)

DATABASE = 'login_data.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

@app.route('/')
def index():
    with open('test-index.html', 'r', encoding='utf-8') as file:
        return render_template_string(file.read())

@app.route('/login', methods=['POST'])
def login():
    new_username = request.form['new_username']
    new_password = request.form['new_password']

    conn = get_db()
    c = conn.cursor()
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (new_username, new_password))
    conn.commit()
    conn.close()

    with open('test-index.html', 'r', encoding='utf-8') as file:
        return render_template_string(file.read())

@app.route('/kemalettin', methods=['GET'])
def users():
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    conn.close()

    return render_template_string('''
    <h2>Registered Users</h2>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Username</th>
            <th>Password</th>
        </tr>
        {% for user in users %}
        <tr>
            <td>{{ user[0] }}</td>
            <td>{{ user[1] }}</td>
            <td>{{ user[2] }}</td>
        </tr>
        {% endfor %}
    </table>
    ''', users=users)

if __name__ == '__main__':
    # Ensure the database and table are created
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
    app.run(debug=True)
