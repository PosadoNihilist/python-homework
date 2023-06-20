import requests
import datetime
url = 'https://kontests.net/api/v1/sites'
response = requests.get(url)
data = response.json()

now = datetime.datetime.now()
for item in data:
    new_url = 'https://kontests.net/api/v1/' + str(item[1])
    new_response = requests.get(new_url)
    new_data = new_response.json()
    if new_data != []:
      cringe_format = new_data[0]['start_time']
      try: start_date = datetime.datetime.strptime(cringe_format, '%Y-%m-%dT%H:%M:%S.%fZ')
      except: start_date = datetime.datetime.strptime(cringe_format, '%Y-%m-%d %H:%M:%S %Z')
      if start_date >= now and start_date <= now + datetime.timedelta(days=15):
        print(str(new_data[0]['name']) + ' - ' + str(start_date))