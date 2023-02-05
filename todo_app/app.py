from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
import todo_app.data.session_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    todo_items = todo_app.data.session_items.get_items()
    return render_template('index.html', todo_items=todo_items)

@app.route('/add', methods = ['POST', 'GET'])
def add_item():
    if request.method == 'POST':
        new_todo = request.form.get('todo_item')
        todo_app.data.session_items.add_item(new_todo)
        return redirect(url_for('index'))
    if request.method == 'GET':
        return redirect(url_for('index'))

@app.route('/read')
def read():
    todo_items = todo_app.data.session_items.get_items()
    return render_template('index.html', todo_items=todo_items)