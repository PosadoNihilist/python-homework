import requests
from bs4 import BeautifulSoup
url = 'https://quotes.toscrape.com/page/'
page = 1
while True:
    response = requests.get(url + str(page))
    soup = BeautifulSoup(response.text, 'html.parser')
    response = soup.find('ul', class_='pager').find_all('a')[-1].text
    if response == "← Previous": break
    page +=1
print("Number of pages: " + str(page))
