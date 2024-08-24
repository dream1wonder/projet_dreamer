import sqlite3
from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

def connect_db():
    conn = sqlite3.connect('database1.db')
    conn.execute('CREATE TABLE IF NOT EXISTS dreamy (id INTEGER PRIMARY KEY AUTOINCREMENT, thoughts TEXT)')
    conn.row_factory = sqlite3.Row
    return conn
@app.route('/',methods=['GET', 'POST'],)
def index():
    return render_template('index.html')


@app.route('/create',methods=['GET', 'POST'],)
def create():
    conn = connect_db()

    if request.method == 'POST':
        thoughts = request.form['thoughts']
        conn.execute('INSERT INTO dreamy ( thoughts) VALUES (?)', (thoughts,))
        conn.commit()

    tasks = conn.execute('SELECT * FROM dreamy ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('create.html', tasks=tasks)
'''
@app.route('/delete/<int:id>')
def delete_task(id):
    conn = connect_db()
    conn.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('create'))'''

if __name__ == '__main__':
    app.run(debug=True)
