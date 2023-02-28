import requests
url = 'https://api.publicapis.org/entries'
response = requests.get(url)
data = response.json()
def count_auth_types():
  total_count = 0
  auth_count_dict = {}
  for elem in data['entries']:
    total_count +=1
    if 'Auth' in elem and elem['Auth']!= '':
      auth_type = elem['Auth']
      if auth_type in auth_count_dict:
        auth_count_dict[auth_type] += 1
      else:
        auth_count_dict[auth_type] = 1
  for key, value in auth_count_dict.items():
    percent = (int(value)/int(total_count))*100
    print(str(percent) + "% of these public APIs use " + str(key) + " authentication")

def count_github_api():
  github_api_count = 0
  for elem in data['entries']:
    if 'Link' in elem and 'github' in elem['Link']:
      github_api_count +=1
  return(github_api_count)

def count_category_types():
  category_type_dict = {}
  for elem in data['entries']:
    if 'Category' in elem and elem['Category']!= '':
      category_type = elem['Category']
      if category_type in category_type_dict:
        category_type_dict[category_type] += 1
      else:
        category_type_dict[category_type] = 1
  for key, value in category_type_dict.items():
    print("The '" + str(key) + "' category has " + str(value) + " public APIs")

count_auth_types()
count_github_api()
count_category_types()