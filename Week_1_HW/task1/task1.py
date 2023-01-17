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
    students_dict = {}
    full_name_list = []
    for line in lines:
        line_list = line.split()
        full_name = line_list[1] + " " + line_list[2].strip(":")
        score = line_list[3]
        students_dict.update({full_name: score})
        full_name_list.append(full_name)
    sorted_full_name_list = sorted(full_name_list)
    final_output = "name,grade\n"
    for name in sorted_full_name_list:
        template = '{},{}\n'
        final_output += template.format(name, students_dict.get(name))
    return str(final_output)

text = read_data("data.txt")
out = format_data(text)
write_data('out.csv', out)