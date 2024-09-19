from colors import GREEN, RED, YELLOW, ENDC

def header_content(class_name):
    content = "#ifndef " + class_name.upper() + "_H\n"
    content += "#define " + class_name.upper() + "_H\n\n"
    content += "class " + class_name + " {\n"
    content += "\tprivate:\n"
    content += "\tpublic:\n"
    content += "\t\t" + class_name + "();\n"
    content += "\t\t~" + class_name + "();\n"
    content += "};\n\n"
    content += "#endif\n"
    return content

def create_header(class_name):
    header_content_ = header_content(class_name)
    header_file = open(class_name + ".hpp", "w")
    header_file.write(header_content_)
    header_file.close()
    print(GREEN + "Created " + class_name + ".hpp" + ENDC)
