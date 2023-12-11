import requests

fieldnames = ["name", "birthday", "age"]

response = requests.get("https://tr148rto1k.execute-api.ap-southeast-2.amazonaws.com/dev/birthdays")

data = response.json()

print(data)
