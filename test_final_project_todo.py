from final_project_to_do import add_items, view_task
import pytest

def test_add_items():
    assert add_items("todo_list.csv", "w") != "file"

def test_view_items():
    assert view_task("todo_list.csv") != ""

pytest.main(["-v", "--tb=line", "-rN", __file__])

#CSE 212 programming with data structure