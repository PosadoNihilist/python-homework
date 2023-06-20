import requests

data = """Ivan Ivanov,1000 USD
Alex Random,1000 EUR
Athur Smith,1000 RUB
Joe Mama,100 USD
Mark Smith,500 USD
Adam Nice,500 EUR"""

def conversion(amount, first_currency, second_currency): 
  url = "https://open.er-api.com/v6/latest/" + str(first_currency)
  result = requests.get(url)
  data = result.json()
  try: rate = data['rates'][second_currency]
  except: return("oops")
  else: 
    return amount * rate

def format_data(data):
  workers_dict = {}
  lines = data.split("\n")
  for line in lines:
    line_split = line.split(",")
    name = line_split[0]
    old_curr = line_split[1].split(" ")[1]
    old_ammt = int(line_split[1].split(" ")[0])
    salary_in_rub = conversion(old_ammt, old_curr, "RUB")
    workers_dict[name] = salary_in_rub
  return workers_dict

def calculate_salaries(dictionary):
  months = ["3", "4", "5"]
  total_hours = 0
  for i in months:
    url = 'https://isdayoff.ru/api/getdata?year=2022&month='+i
    response = requests.get(url)
    if response.status_code == 200:
      line = str(response.content)
      full = line.count('0')
      half = line.count('2')
      full_again = line.count('4')
      month_hours = 8*(full + full_again) + 4*(half)
      total_hours += month_hours
  for name, salary in dictionary.items():
    print(name + " " + str(round(salary*total_hours, 2)) + " RUB")

  
calculate_salaries(format_data(data))

