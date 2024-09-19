from colors import GREEN, RED, YELLOW, ENDC

def source_content(class_name):
    content = "#include \"" + class_name + ".hpp\"\n\n"
    content += class_name + "::" + class_name + "() {\n\n}\n\n"
    content += class_name + "::~" + class_name + "() {\n\n}\n\n"
    return content

def create_source(class_name):
    source_content_ = source_content(class_name)
    source_file = open(class_name + ".cpp", "w")
    source_file.write(source_content_)
    source_file.close()
    print(GREEN + "Created " + class_name + ".cpp" + ENDC)