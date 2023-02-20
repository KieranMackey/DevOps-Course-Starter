from flask import session
import os
import json
import requests

url = "https://api.trello.com/1/boards/" + str(os.environ.get('BOARD_ID'))

headers = {
  "Accept": "application/json"
}

_DEFAULT_ITEMS = [
    { 'id': 1, 'status': 'Not Started', 'title': 'List saved todo items' },
    { 'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added' }
]

trello_lists = []
items = [ ]

def get_list_id_from_name(name, create_list = False):
    query = {
    'key': os.environ.get('TRELLO_API_KEY'),
    'token': os.environ.get('TRELLO_TOKEN'),
    }

    response = requests.request(
        "GET",
        "https://api.trello.com/1/lists/To do",
        params=query,
        verify=False
    )

    # TODO: if there's no 'TO DO' list, create one
    print("TODO list id: " + str(response.text))
    return response.text

def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    query = {
    'key': os.environ.get('TRELLO_API_KEY'),
    'token': os.environ.get('TRELLO_TOKEN'),
    'cards' : 'all'
    }

    response = requests.request(
        "GET",
        (url + "/lists"),
        headers=headers,
        params=query,
        verify=False
    )

    items = [ ]
    json_resp = response.json()
    #print(str(json_resp))
    #print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

    # Go through cards and store name and ID
    for list in json_resp:
        list_id = list['id']
        list_name = list['name']
        trello_list = { 'id': list_id, 'name': list_name }
        trello_lists.append(trello_list)
        for card in list['cards']:
            #print ("This is a card: " + card['name'])
            item = { 'id': card['id'], 'title': card['name'], 'list_id': list_id, 'status': list_name }
            print(str(item))
            items.append(item)

    return items


def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    list_id = ''
    for list in trello_lists:
        if list['name'] == 'To Do':
            list_id = list['id']

    print(str(list_id))

    item = { 'id': id, 'title': title, 'status': 'Not Started' }

    cards_url = "https://api.trello.com/1/cards"

    query = {
    'idList': list_id,
    'key': os.environ.get('TRELLO_API_KEY'),
    'token': os.environ.get('TRELLO_TOKEN'),
    'name': str(title)
    }

    response = requests.request(
        "POST",
        cards_url,
        headers=headers,
        params=query,
        verify=False
    )
    # Add the item to the list
    items.append(item)
    #session['items'] = items
    print("add response: " + str(response))
    return item


def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    session['items'] = updated_items

    return item
