# get todos from file
FILEPATH = "todos.txt"


def get_todos(filename=FILEPATH):
    """function to get items from file"""
    with open(filename, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg,filename=FILEPATH):
    """write to file function"""
    with open(filename, "w") as file_local:
        file_local.writelines(todos_arg)


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

if __name__ == "__main__":
    print("Hello from functions")
    print(get_todos())