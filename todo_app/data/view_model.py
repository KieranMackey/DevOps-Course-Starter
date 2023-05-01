from todo_app.data.trello_items import Item
class ViewModel:

    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items
    
    @property
    def doing_items(self):
        items = []
        for item in self._items:
            if item.status == "Doing":
                items.append(item)

        return items