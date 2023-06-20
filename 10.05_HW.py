#Решить систему линейных уравнений:
import numpy as np
#x + y + z = 6
#2x + 5y - z = -4
#2x - y + 3z = 27

A = np.array ([[1,1,1],[2,5,-1],[2,-1,3]])
B = np.array([6, -4, 27])
C = np.linalg.solve(A,B)


#1. Сгенерировать данные
import requests
import random
import pandas as pd
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

n = 50
city_names = load_countries_name(10)
data = np.column_stack((generate_product_id(n), generate_region_sales(n), generate_regions(n, city_names)))

np.savetxt('data.txt', data, delimiter=',', fmt='%s')
#2. Посчитать определенные значения, которые бизнес хочет вычислить
data = np.loadtxt('data.txt', delimiter=',', dtype="str")
df = pd.DataFrame(data, columns=['id', 'sales', 'region'])
df['id'] = df['id'].astype('int')
df['sales'] = df['sales'].astype('int')
#Какова общая сумма продаж для всех продуктов?
print(df['sales'].sum())
#Сколько уникальных регионов продаж существует?
print(len(np.unique(data[:, 2])))
#Какова средняя сумма продаж на продукт?
print(df.groupby('id')['sales'].sum().sort_values(ascending=False).mean())
#Какой продукт имеет наибольшую сумму продаж?
print(df.groupby('id')['sales'].sum().sort_values(ascending=False)[:1])
#Рассчитайте сумму продаж для каждого региона продаж. (постройте круговую гистограмму)
answer = df.groupby('region')['sales'].sum().sort_values(ascending=False)
answer.plot(kind='pie')
#Топ 5 продуктов по продажам и построить круговую гистограмму, где будет 6 секторов: топ 5 и все остальное
top_5 = df.groupby('region')['sales'].sum().sort_values(ascending=False)[:5]
all_else = df.groupby('region')['sales'].sum().sort_values(ascending=False)[5:].sum()
top_5.loc["others"] = all_else
top_5.plot(kind='pie')



