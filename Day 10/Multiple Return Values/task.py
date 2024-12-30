def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "you have not given any input"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"result : {formated_f_name} {formated_l_name}"


print(format_name("an", ""))
