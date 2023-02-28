import requests
currency_error = "Sorry, please make sure you correctly inputted the currency."
def conversion(amount, first_currency, second_currency): 
  url = "https://open.er-api.com/v6/latest/" + str(first_currency)
  result = requests.get(url)
  data = result.json()
  try: rate = data['rates'][second_currency]
  except: return(currency_error)
  else: 
    return amount * rate

def ask():
  while True:
    first_input = input("How much money and in which currency do you want to convert? (For example, write '100 RUB' or '200 EUR') ")
    try: 
      amount = float(first_input.split(" ")[0])
      first_currency = str(first_input.split(" ")[1])
    except: 
      print("Please input the money and currency you are converting in the format '[Amount] [Currency]' ")
    else: 
        second_input = input("Which currency do you want to convert to? ")
        second_currency = str(second_input)
        return(amount, first_currency, second_currency)

amount, first_currency, second_currency = ask()
result = conversion(amount, first_currency, second_currency)
if result == currency_error:
  print(result)
else:
  print(str(result) + " " + second_currency)
