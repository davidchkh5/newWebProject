import os

def get_todos(filepath ="todos.txt"):
    """ Read a text file and return the list of
    to-do items
    """ #when we type help(get_todos) the document string that is top of the function will appear its used to show what current function do

    if not os.path.exists(filepath):
        with open(filepath, 'w') as file:
            pass


    with open(filepath,'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath = "todos.txt"):
    """ Write to-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

