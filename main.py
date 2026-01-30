"""
To-Do List Manager with Streamlit
"""

import streamlit as st

from todoitem import Todo
from todolist import ToDoList

def add_todo():
    new_todo = Todo(st.session_state.new_task)
    todo_list.add_todo_item(new_todo)
    todo_list.save_items_to_file()
    st.session_state.new_task = ""

todo_list = ToDoList()
st.title("To-Do List Manager")
for index, todo in enumerate(todo_list.get_todo_items(), 1):
    checkbox = st.checkbox(f"{todo}", key=todo.task)
    if checkbox:
        todo_list.complete_todo(index)
        todo_list.save_items_to_file()
        del st.session_state[todo.task]
        st.rerun()

st.text_input("", placeholder="Enter a task...", key="new_task", on_change=add_todo)
