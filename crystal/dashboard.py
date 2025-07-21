from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
from core.database import Database

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id):
        self.id = id

users = {'user': {'password': 'password'}}

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/shell')
@login_required
def shell():
    return render_template('shell.html')

@app.route('/logs')
@login_required
def logs():
    return render_template('logs.html')

@app.route('/generate-payload')
@login_required
def generate_payload():
    return render_template('generate_payload.html')

@app.route('/listener')
@login_required
def listener():
    return render_template('listener.html')

@app.route('/chat')
@login_required
def chat():
    return render_template('chat_client.html')

@app.route('/files')
@login_required
def files():
    return render_template('files.html')

@app.route('/files/<path:path>')
@login_required
def file_browser(path):
    abs_path = os.path.abspath(path)
    if os.path.isdir(abs_path):
        files = os.listdir(abs_path)
        return render_template('file_browser.html', path=path, files=files)
    else:
        with open(abs_path, 'r') as f:
            content = f.read()
        return render_template('file_view.html', path=path, content=content)

@app.route('/database')
@login_required
def database():
    db = Database()
    targets = db.get_targets()
    db.close()
    return render_template('database.html', targets=targets)

if __name__ == "__main__":
    app.run(debug=True)
