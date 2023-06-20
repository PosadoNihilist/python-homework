import numpy as np
import requests
import random
from bs4 import BeautifulSoup
def load_countries_name(n):
    url = 'https://randomuser.me/api/'
    params = {'results': n} 
    response = requests.get(url, params)
    data = response.json()['results']
    countries = [user['location']['country'] for user in data]
    return countries
    
def generate_product_id(n):
    return np.random.randint(1, 10, n)

def generate_region_sales(n):
    return np.round(np.random.randint(1, 300, n))

def generate_regions(n, city_names = []):
    return np.random.choice(city_names, n)
  
def extract_currency_codes():
    url = "https://www.exchangerate-api.com/docs/supported-currencies"
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    tables = soup.find_all("table")
    currency_codes = {}
    for table in tables:
        for row in table.find_all("tr")[1:]:
            cells = row.find_all("td")
            country = cells[2].text.strip()
            currency_code = cells[0].text.strip()
            currency_codes[country] = currency_code
    return currency_codes

def get_exchange_rate(currency_code):
    url = f"https://open.er-api.com/v6/latest/{currency_code}"
    response = requests.get(url)
    data = response.json()["rates"]
    rub_value = data["RUB"]
    return rub_value

def add_currency_and_sales_in_rub(data, currency_codes):
    cur = []
    a = []
    for i in range(data.shape[0]):
          country = data[i, 2]
          currency_code = currency_codes.get(country, "EUR")
          exchange_rate = get_exchange_rate(currency_code)
          sales = float(data[i, 1])
          converted_sales = sales * exchange_rate
          cur.append([currency_code])
          a.append([converted_sales])
    data = np.append(data, cur, axis = 1)
    data = np.append(data, a, axis = 1)
    return(data)
currency_codes = extract_currency_codes()
n = 50
city_names = load_countries_name(10)
data = np.column_stack((generate_product_id(n), generate_region_sales(n), generate_regions(n, city_names)))
data = add_currency_and_sales_in_rub(data, currency_codes)
np.savetxt('data.txt', data, delimiter=',', fmt='%s')




