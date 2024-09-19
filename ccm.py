

import sys
import os

from colors import GREEN, RED, YELLOW, ENDC
from tools import print_help_menu, force_camel_case
from header import create_header
from source import create_source
from deletion import manage_remove
from methods import add_method

if __name__ == "__main__":
    if len(sys.argv) < 2:
        if len(sys.argv) == 2 and sys.argv[1] == "help":
            print_help_menu()
            sys.exit(0)
        else:
            print("Usage: python cpp_manager.py <command>")
        sys.exit(1)

    command = sys.argv[1]
    
    if command == "addto":
        # addinto <class_name> <method_name> <return_type> data_type:var1 data_type:var2 ...
        if len(sys.argv) < 5:
            print(RED + "Missing parameters, please use help" + ENDC)
            printf(RED + "Usage: python cpp_manager.py addto <class_name> <return_type> <method_name> data_type:var1 data_type:var2 ..." + ENDC)
            sys.exit(1)
        class_name = sys.argv[2]
        return_type = sys.argv[3]
        method_name = sys.argv[4]
        params = []
        for i in range(5, len(sys.argv)):
            # if starts with std:: pass it
            includes_std = sys.argv[i].startswith("std::")
            arg = sys.argv[i].replace("std::", "")
            data = arg.split(":")
            if includes_std:
                data[0] = "std::" + data[0]
            params.append({"data_type": data[0], "var_name": data[1]})
        add_method(class_name, method_name, return_type, params)
    else:
        if command == "help":
            print_help_menu()
        elif command == "create" or command == "remove":
            if len(sys.argv) < 3:
                print(RED + "Missing parameters, please use help" + ENDC)
                sys.exit(1)

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
        else:
            print(RED + "Invalid command, please use help" + ENDC)
            sys.exit(1)
