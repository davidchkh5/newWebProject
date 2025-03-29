import streamlit as st

# Initialize session state for todos
if "todos" not in st.session_state:
    st.session_state.todos = []

def add_todo():
    """Add a new todo to the list."""
    todo = st.session_state["new_todo"].strip()  # Remove extra spaces
    if todo:  # Prevent adding empty todos
        st.session_state.todos.append(todo)
        st.session_state["new_todo"] = ""  # Clear input field

st.title("My To-Do App")

# Display todos with checkboxes
for index, todo in enumerate(st.session_state.todos):
    if st.checkbox(todo, key=todo):
        st.session_state.todos.pop(index)
        del st.session_state[todo]
        st.rerun()  # Refresh the UI

# Input field for adding new todos
st.text_input(label="Enter a todo", placeholder="Add new todo...", on_change=add_todo, key="new_todo")
