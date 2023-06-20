from bs4 import BeautifulSoup #импортируем библиотеку beautifulsoup
import requests #импортируем библиотеку requests

url = "https://adme.media/svoboda-psihologiya/100-voprosov-kotorye-nuzhno-obsudit-s-rebenkom-chtoby-ukrepit-s-nim-svyaz-2043665/" #задаём url

response = requests.get(url) #получаем необработанные данные со страницы
soup = BeautifulSoup(response.text.replace('\xa0', ' '), 'html.parser') #переводим данные в формат beautifulsoup используя html.parser, заменяем все \xa0 на пробелы
asks = soup.find_all('div', class_="e599d42b92530cddc130") #достаём всё с классом e599d42b92530cddc130 (вопросы)
title_tags = list(filter(lambda x: x[1].text[0].isdigit(), enumerate(asks))) #достаём все теги которые начинаются на цифру (штуки с названиями)
titles = [tag.text[tag.text.find('.') + 2:] for _, tag in title_tags] #создаём список из только текста
question_tags  = [asks[i + 1] for i, _ in title_tags] #берём все теги с вопросами
questions = [[p_tag.text for p_tag in tag.find_all('p')] for tag in question_tags] #создаём список из только текста
result = dict(zip(titles, questions)) #создаём словарь с названиями и вопросами
print(result) #печатаем