import os

from colors import GREEN, RED, YELLOW, ENDC


def create_header_method(class_name, method_name, return_type, params = []) -> str:
    buffer = "\t\t" + return_type + " " + method_name + "("
    for i in range(len(params)):
        buffer += params[i]["data_type"] + " " + params[i]["var_name"]
        if i < len(params) - 1:
            buffer += ", "
    buffer += ");\n"
    return buffer

def create_source_method(class_name, method_name, return_type, params = []) -> str:
    buffer = return_type + " " + class_name + "::" + method_name + "("
    for i in range(len(params)):
        buffer += params[i]["data_type"] + " " + params[i]["var_name"]
        if i < len(params) - 1:
            buffer += ", "
    buffer += ") {\n\n}\n"
    return buffer

def add_method(class_name, method_name, return_type, params=[]):

    if not os.path.exists(class_name + ".hpp") or not os.path.exists(class_name + ".cpp"):
        print(RED + "Class " + class_name + " not found" + ENDC)
        return
    
    header_file = open(class_name + ".hpp", "a")

    buffer = ""

    inside_class = False
    # find exactly the class definition
    with open(class_name + ".hpp", "r") as file:
        for line in file:
            if line.startswith("class " + class_name):
                inside_class = True
            if inside_class and line.startswith("};"):
                buffer += create_header_method(class_name, method_name, return_type, params)
            buffer += line

    header_file.close()
    # overwrite the file
    header_file = open(class_name + ".hpp", "w")
    header_file.write(buffer)
    header_file.close()
    print(GREEN + "Method " + method_name + " added to " + class_name + ".hpp" + ENDC)

    source_file = open(class_name + ".cpp", "a")
    source_file.write(create_source_method(class_name, method_name, return_type, params))
    source_file.close()
    print(GREEN + "Method " + method_name + " added to " + class_name + ".cpp" + ENDC)
    