import streamlit as st

# Initialize session state for todos
if "todos" not in st.session_state:
    st.session_state.todos = []

def get_todos():
    """Return the list of to-do items from session state."""
    return st.session_state.todos

def write_todos(todos_arg):
    """Write to-do items list in session state."""
    st.session_state.todos = todos_arg
