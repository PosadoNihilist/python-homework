def read_data(file_name):
    file = open(file_name)
    content = file.read()
    return content

def write_data(file_name, data):
    f = open(file_name, "w")
    f.write(data)
    f.close()

def format_text(text):
    words = text.split()
    words_freq = {}
    for temp_word in words:
        temp_word = temp_word.strip(".")
        temp_word = temp_word.strip(",")
        word = temp_word.lower()
        if word not in words_freq:
            words_freq.update({word: 1})
        else:
            old = words_freq.get(word)
            words_freq.update({word: old+1})
    words_freq_copy = dict(words_freq)
    max_keys = []
    while len(max_keys) < 10:
        max_keys += [key for key, value in words_freq_copy.items() if value == max(words_freq_copy.values())]
        for elem in max_keys:
            try: words_freq_copy.pop(elem)
            except: pass
    final_output = ""
    for key in max_keys[:10]:
        template = '{},{}\n'
        final_output += template.format(key, words_freq.get(key))
    return str(final_output)

    
content = read_data("input.txt")
write_data("output.txt", format_text(content))