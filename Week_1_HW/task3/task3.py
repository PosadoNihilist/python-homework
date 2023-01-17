symbols_per_line = 21
def read_data(file_name):
    file = open(file_name)
    content = file.read()
    return content

def write_data(file_name, data):
    f = open(file_name, "w")
    f.write(data)
    f.close()

def format_text(text):
    text_copy = text
    chunk_list = []
    while text_copy != '':
        chunk = text_copy[:symbols_per_line]
        i=0
        last_var = chunk[len(chunk)-1]
        while last_var!=" " and last_var!="," and last_var!="." and " " in chunk:
            i+=1
            chunk = text_copy[:symbols_per_line-i]
            last_var = chunk[len(chunk)-1]
        text_copy = text_copy.replace(chunk, "")
        chunk_list.append(chunk)
    output = ""
    for chunk in chunk_list:
        output = output + chunk + "\n"
    return output
content = read_data("input.txt")
write_data("output.txt", format_text(content))