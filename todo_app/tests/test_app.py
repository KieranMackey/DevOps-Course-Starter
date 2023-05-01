from todo_app.data.trello_items import Item
from todo_app.data.view_model import ViewModel

def test_doing_items():
    # Arrange
    test_items = [Item("abcdef123", "Test Item 1", status = "Doing"), 
            Item("bcdef1234", "Test Item 2"), 
            Item("cdef12345", "Test Item 3", status = "Doing"), 
            Item("def123456", "Test Item 4"), 
            Item("ef1234567", "Test Item 5", status = "Done")]

    # Act
    item_view_model = ViewModel(test_items)
    todo_items = item_view_model.doing_items()

    # Assert
    assert(len(todo_items) == 2)