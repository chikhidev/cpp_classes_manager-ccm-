from colors import GREEN, RED, YELLOW, ENDC
import os

from header import header_content
from source import source_content
from tools import is_file_updated

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