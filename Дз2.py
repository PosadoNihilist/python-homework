def read_data(file_name):
    file = open(file_name, "r")
    content = file.read()
    return content
    
def write_data(file_name, data):
    f = open(file_name, "w")
    f.write(data)
    f.close()
    
def prepare_lines(data):
    output = ''
    splitted = data.split('\n')
    titles = splitted.pop(0)
    labels = titles.split(',')
    for i in range(len(labels)): labels[i]= '"' + labels[i] + '"'
    user1_vals, user2_vals, user3_vals, user1, user2, user3 = [], [], [], [], [], []
    user_list = [user1_vals, user2_vals, user3_vals]
    dictionary_list = [user1, user2, user3]
    a = 0
    for user in user_list:
        k=0
        for elem in splitted[a].split(','):
            k += 1
            if k == 2: user.append('"' + elem + '"')
            else: user.append(elem)
        dictionary_list[a] = dict(zip(labels, user1_vals))
        a += 1
    
    count_list = ["1", "2", "3"]
    full_dictionary = dict(zip(count_list, dictionary_list))
    
    result = '[' + "\n"
    a = 0
    for key, value in full_dictionary.items():
        a+=1
        result += '  {' + "\n"
        i = 0
        for subject, score in value.items():
            result += '    ' + str((str(subject) + ':' + str(score))) 
            i+=1
            if i<= 3: result += ","
            result += "\n"
        if a <= 2: result += '  },'
        else: result += '  }'
        result += "\n"
    result += ']'
    return result

content = read_data("input.csv")
final_output = prepare_lines(content)
write_data("out.json", final_output)