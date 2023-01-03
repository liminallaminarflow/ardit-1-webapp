FILEPATH = "todos.txt"

# functions
def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list of its contents. """
    with open(filepath) as file:
        todos = file.readlines()
    return todos


def write_todos(new_todos, filepath=FILEPATH):
    """ Write to-do items in the list into a text file. """
    with open(filepath, "w") as file:
        file.writelines(new_todos)
