import random
import requests
import csv
import pandas as pd

def generate_ids(data_len):
    l = [str(random.randint(0, 99999)) for _ in range(data_len)]
    return l
    
    
def generate_salary(data_len):
    l = [str(random.randint(100000, 999999)) for _ in range(data_len)]
    return l
    
    
def generate_month(data_len):
    months = [str(random.randint(1, 12)) for _ in range(data_len)]
    return months
    
def generate_users(data_len):
    url = "https://randomuser.me/api/"
    params = {'results': data_len}
    response = requests.get(url, params=params)
    data = response.json()
    result = list(map(lambda x: x['name'], data['results']))  
    return []
    
data_len = 10  
titles = ['id', 'salary', 'month', 'name']
merged = zip(generate_ids(data_len), generate_salary(data_len), generate_month(data_len), generate_users(data_len))    

with open("data.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(titles)
    for row in merged:
        writer.writerow(row)

#открыть с помощью pandas  и посчитать среднюю зарплату

df = pd.read_csv('data.csv')
print(df['salary'].mean())
