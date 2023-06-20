import requests
from bs4 import BeautifulSoup
url = 'https://emojipedia.org/search/'
list_of_categories = ["nature", "music", "science"]
list_of_emojis = []
count = 0
dict_of_count = {}
for category in list_of_categories:
  params = {'q': category}
  response = requests.get(url, params=params)
  soup = BeautifulSoup(response.text, 'html.parser')
  divsoup = soup.find('ol', class_='search-results')
  items = divsoup.find_all('a')
  for item in items:
    new_url = 'https://emojipedia.org/'+ (item.get("href"))
    new_response = requests.get(new_url)
    other_soup = BeautifulSoup(new_response.text, 'html.parser')
    meow = other_soup.find('section', class_='description')
    try: descript = meow.find('p').text
    except: descript = ""
    good = descript.strip()
    list_of_emojis.append((item.text)[2:] + ": " + good)
    count +=1
  print("The " + str(category) + " category has " + str(count) + " emojis.")
  print(list_of_emojis)
  list_of_emojis = []
  count = 0