def read_data(file_name):
    file = open(file_name)
    content = file.read()
    return content

def write_data(file_name, data):
    f = open(file_name, "w")
    f.write(data)
    f.close()
    
def format_data(text):
    lines = text.split('\n')
    complete_dict = {}
    number_list = []
    for line in lines:
        three_vals = line.split("-")
        A = three_vals[0]
        B = three_vals[1].strip(" ")
        location = three_vals[2].strip(" ")
        AandB = A+"-"+B
        complete_dict.update({AandB: location})
        number_list.append(float(B))
    final_output = ""
    for number in sorted(number_list):
        template = '{} - {}\n'
        if number.is_integer():
            key_number = str(int(number))
        else:
            key_number = str(number)
        check_if_left = key_number.split(".")
        if check_if_left[0] == "1":
            key_number = "0"+key_number
        key = "KP2.2-" + key_number
        final_output += template.format(key, complete_dict.get(key))
    return str(final_output)
text = read_data("input.txt")
out = format_data(text)
write_data('output.txt', out)