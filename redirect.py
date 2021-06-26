import requests


response = requests.get("https://playground.learnqa.ru/api/long_redirect")
redirects_number = len(response.history)
print(redirects_number)
print(response.url)
