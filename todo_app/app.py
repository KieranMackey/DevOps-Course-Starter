from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
import os
import todo_app.data.session_items
import todo_app.data.trello_items
import json
import requests

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

url = "https://api.trello.com/1/boards/" + str(os.environ.get('BOARD_ID'))

headers = {
  "Accept": "application/json"
}

query = {
  'key': os.environ.get('TRELLO_API_KEY'),
  'token': os.environ.get('TRELLO_TOKEN')
}

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

@app.route('/read')
def read():
    todo_items = todo_app.data.trello_items.get_items()
    return render_template('index.html', todo_items=todo_items)

@app.route('/trello')
def trello_get():
    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=query,
        verify=False
    )
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
    return redirect(url_for('index'))