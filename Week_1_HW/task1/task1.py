first_line = "name,grade\n"
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
    line_list = []
    for line in lines:
        cleaned_line = line.replace(': ', ',')
        line_list.append(cleaned_line.split('. ')[1])
    line_list = sorted(line_list)
    output = first_line +'\n'.join(line_list)
    return output

text = read_data("data.txt")
out = format_data(text)
write_data('out.csv', out)
