from todo_app.data.trello_items import Item
from todo_app.data.view_model import ViewModel

item_status_test_set = [
            Item("abcdef123", "Test Item 1", status = "Doing"), 
            Item("bcdef1234", "Test Item 2"), 
            Item("cdef12345", "Test Item 3", status = "Doing"), 
            Item("def123456", "Test Item 4", status = "To Do"), 
            Item("ef1234567", "Test Item 5", status = "Done"), 
            Item("f12345678", "Test Item 6", status = "Done")]

def test_doing_items():
    # Arrange
    test_items = item_status_test_set

    # Act
    item_view_model = ViewModel(test_items)
    todo_items = item_view_model.doing_items

    # Assert
    assert(len(todo_items) == 2)
    assert todo_items[0].name == "Test Item 1"
    assert todo_items[1].name == "Test Item 3"

def test_todo_items():
    # Arrange
    test_items = item_status_test_set

    # Act
    item_view_model = ViewModel(test_items)
    todo_items = item_view_model.todo_items

    # Assert
    assert(len(todo_items) == 2)
    assert todo_items[0].name == "Test Item 2"
    assert todo_items[1].name == "Test Item 4"

def test_done_items():
    # Arrange
    test_items = item_status_test_set

    # Act
    item_view_model = ViewModel(test_items)
    todo_items = item_view_model.done_items

    # Assert
    assert(len(todo_items) == 2)
    assert todo_items[0].name == "Test Item 5"
    assert todo_items[1].name == "Test Item 6"