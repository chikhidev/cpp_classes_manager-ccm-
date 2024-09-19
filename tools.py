import re

def is_file_updated(file_path, content):
    file = open(file_path, "r")
    file_content = file.read()
    file.close()
    if file_content == content:
        return False
    return True

def print_help_menu():
    print("Usage: python cpp_manager.py <command> <class_name>")
    print("Commands:")
    print("\tcreate - Create a new class")
    print("\tremove - Remove a class")
    print("\taddto - Add a new method into a class")
    print("\thelp - Print this menu")

def force_camel_case(string):
    name = re.split(r'\s|_|-', string)
    for i in range(len(name)):
        name[i] = name[i].capitalize()
    return "".join(name)
