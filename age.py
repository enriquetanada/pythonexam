import csv
from datetime import date
import datetime
import requests

fieldnames = ["name", "birthday", "age"]

response = requests.get("https://tr148rto1k.execute-api.ap-southeast-2.amazonaws.com/dev/birthdays")

data = response.json()

today = date.today()

for person in (data["body"]):
    birthDate = datetime.datetime.strptime(person["birthday"], '%Y-%m-%d')

    compareMonthAndDay = ((today.month, today.day) < (birthDate.month, birthDate.day))

    person["age"] = today.year - birthDate.year - compareMonthAndDay

data["body"].sort(key=lambda x: x.get('age'))

with open("age.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data["body"])
