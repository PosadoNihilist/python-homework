left_section = "KP2.2-"

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
    indexes = []
    rows = []
    for line in lines:
        line = line.replace(left_section, "")
        indexes.append(float(line.split(" - ")[0]))
        rows.append(line)
    index = list(zip(indexes, rows))
    index = sorted(index)
    result = ''
    for elem in index:
        result = result + elem[1] + '\n'
    return result

text = read_data("input.txt")
out = format_data(text)
write_data('output.txt', out)
