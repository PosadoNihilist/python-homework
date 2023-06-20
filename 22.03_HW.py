from bs4 import BeautifulSoup
import os


full_path = "/data"
dir_list = os.listdir(full_path)
dir_list = ['1.html', 'hello.csv', 'programmer.html', 'discount.html', 'data.txt']
for file in dir_list:
    if file[-5:] != ".html":
        dir_list.remove(file)
        
def get_all_links(file):
    link_list = []
    response = os.open(full_path+dir_list, os.O_RDONLY)
    soup = BeautifulSoup(response, 'html.parser')
    links = soup.find_all("a")
    for link in links:
        link_list.append(link.get("href"))
    return(link_list)
    

for file in dir_list: 
    no_html = file[:len(file) - 5]
    name_with_txt = no_html+".txt"
    os.mkdir(full_path, links)
    f = open(name_with_txt, "w")
    f.write(get_all_links(file))
    f.close()
