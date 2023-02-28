import requests
url = "https://official-joke-api.appspot.com/jokes/ten"
result = requests.get(url)
data = result.json()
types = []
for item in data:
  types.append(item['type']) 
print(types)