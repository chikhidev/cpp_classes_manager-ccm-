GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
ENDC = "\033[0m"

import sys
import os
import re

def header_content(class_name):
    content = "#ifndef " + class_name.upper() + "_H\n"
    content += "#define " + class_name.upper() + "_H\n\n"
    content += "class " + class_name + " {\n"
    content += "\tpublic:\n"
    content += "\t\t" + class_name + "();\n"
    content += "\t\t~" + class_name + "();\n"
    content += "\tprivate:\n\n"
    content += "};\n\n"
    content += "#endif\n"
    return content

def create_header(class_name):
    header_content_ = header_content(class_name)
    header_file = open(class_name + ".hpp", "w")
    header_file.write(header_content_)
    header_file.close()
    print(GREEN + "Created " + class_name + ".hpp" + ENDC)

def source_content(class_name):
    content = "#include \"" + class_name + ".hpp\"\n\n"
    content += class_name + "::" + class_name + "() {\n\n}\n\n"
    content += class_name + "::~" + class_name + "() {\n\n}\n"
    return content

def create_source(class_name):
    source_content_ = source_content(class_name)
    source_file = open(class_name + ".cpp", "w")
    source_file.write(source_content_)
    source_file.close()
    print(GREEN + "Created " + class_name + ".cpp" + ENDC)

def is_file_updated(file_path, content):
    file = open(file_path, "r")
    file_content = file.read()
    file.close()
    if file_content == content:
        return False
    return True

def manage_remove(class_name):
    if os.path.exists(class_name + ".hpp"):
        if is_file_updated(class_name + ".hpp", header_content(class_name)):
            print(YELLOW + "File " + class_name + ".hpp" + " has been modified. Do you want to remove it? [y/n]" + ENDC)
            answer = input()
            if answer == "y":
                os.remove(class_name + ".hpp")
                print(RED + "Removed " + class_name + ".hpp" + ENDC)
            else:
                return
    else:
        print(RED + "File " + class_name + ".hpp" + " not found" + ENDC)
        return

    if os.path.exists(class_name + ".cpp"):
        if is_file_updated(class_name + ".cpp", source_content(class_name)):
            print(YELLOW + "File " + class_name + ".cpp" + " has been modified. Do you want to remove it? [y/n]" + ENDC)
            answer = input()
            if answer == "y":
                os.remove(class_name + ".cpp")
                print(RED + "Removed " + class_name + ".cpp" + ENDC)
            else:
                return
    else:
        print(RED + "File " + class_name + ".cpp" + " not found" + ENDC)
        return
    if os.path.exists(class_name + ".hpp"):
        os.remove(class_name + ".hpp")
        print(RED + "Removed " + class_name + ".hpp" + ENDC)
    if os.path.exists(class_name + ".cpp"):
        os.remove(class_name + ".cpp")
        print(RED + "Removed " + class_name + ".cpp" + ENDC)

def print_help_menu():
    print("Usage: python cpp_manager.py <command> <class_name>")
    print("Commands:")
    print("\tcreate - Create a new class")
    print("\tremove - Remove a class")



def force_camel_case(string):
    name = re.split(r'\s|_|-', string)
    for i in range(len(name)):
        name[i] = name[i].capitalize()
    return "".join(name)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        if len(sys.argv) == 2 and sys.argv[1] == "help":
            print_help_menu()
            sys.exit(0)
        else:
            print("Usage: python cpp_manager.py <command> <class_name>")
        sys.exit(1)

    command = sys.argv[1]
    
    for i in range(2, len(sys.argv)):
        class_name = sys.argv[i]

        if command == "create":
            class_name = force_camel_case(class_name)
            print(GREEN + "Class name: " + class_name + ENDC)
            if not os.path.exists(class_name + ".hpp"):
                create_header(class_name)
            else:
                print(YELLOW + "File " + class_name + ".hpp" + " already exists" + ENDC)
            if not os.path.exists(class_name + ".cpp"):
                create_source(class_name)
            else:
                print(YELLOW + "File " + class_name + ".cpp" + " already exists" + ENDC)
        elif command == "remove":
            manage_remove(class_name)
        elif command == "help":
            print_help_menu()
        else:
            print(RED + "Invalid command, please use help" + ENDC)
            sys.exit(1)
