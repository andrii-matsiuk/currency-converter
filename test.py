response = requests.get(url='https://api.exchangerate-api.com/v4/latest/USD').json()
print(response)