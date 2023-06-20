import requests
from bs4 import BeautifulSoup


clothes = []
page = 1
while True: 
  url = 'https://scrapingclub.com/exercise/list_basic/?page='+str(page)
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
  for item in items:
    name = item.find('h4', class_='card-title').text.strip('\n')
    price = item.find('h5').text
    clothes.append((name, price))
  pages = soup.find_all('li', class_='page-item')
  is_next = soup.body.findAll(string='Next') 
  if is_next == []: break
  page +=1 

print(clothes)