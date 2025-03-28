import streamlit as st

from modules import Functions

todos = Functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]+ "\n"
    todos.append(todo)
    Functions.write_todos(todos)
    st.session_state["new_todo"] = ""

st.title("My todo app")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        Functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()      


st.text_input(label="Enter a todo", placeholder="Add new todo...", on_change=add_todo, key="new_todo")




