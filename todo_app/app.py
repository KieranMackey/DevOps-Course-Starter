from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
import todo_app.data.trello_items
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    todo_items = todo_app.data.trello_items.get_items()
    return render_template('index.html', todo_items=todo_items)

@app.route('/add', methods = ['POST', 'GET'])
def add_item():
    if request.method == 'POST':
        new_todo = request.form.get('todo_item')
        todo_app.data.trello_items.add_item(new_todo)
        return redirect(url_for('index'))
    if request.method == 'GET':
        return redirect(url_for('index'))

@app.route('/complete/<completed_task>', methods = ['POST', 'GET'])
def complete_item(completed_task):
    if request.method == 'POST':
        todo_app.data.trello_items.set_task_status(completed_task, 'Done')
        return redirect(url_for('index'))
    if request.method == 'GET':
        return redirect(url_for('index'))

@app.route('/read')
def read():
    todo_items = todo_app.data.trello_items.get_items()
    return render_template('index.html', todo_items=todo_items)