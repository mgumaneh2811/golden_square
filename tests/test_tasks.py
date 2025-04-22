from lib.tasks import *
import pytest

def test_that_list_is_empty():
    todo_list = Task()
    assert todo_list.todo_list == []

def test_that_tasks_are_added():
    todo_list = Task()
    todo_list.add("go buy milk")
    assert todo_list.todo_list == ["go buy milk"]

def test_that_tasks_are_marked_complete():
    todo_list = Task()
    todo_list.add("go buy milk")
    todo_list.completed("go buy milk")
    assert todo_list.completed_tasks == ["go buy milk"]

def test_that_task_is_removed_from_list():
    todo_list = Task()
    todo_list.add("go buy milk")
    todo_list.add("go home")
    todo_list.completed("go buy milk")
    todo_list.remove("go buy milk")
    assert todo_list.todo_list == ["go home"]