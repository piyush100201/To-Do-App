FILEPATH = "todo.txt"

def read_todos():
    """Returns the todos from the todos text file as a list of strings"""
    with open(FILEPATH, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos):
    """Writes the todos text file with the given todos"""
    with open(FILEPATH, 'w') as file:
        file.writelines(todos)