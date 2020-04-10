import requests


response = requests.get('http://127.0.0.1:5000/status')
data = response.json()
print("Status: ", data["Status"])
print("Date: ", data["Date"])
print("Number of messages: ", data["Number_of_messages"])
print("Number_of_users: ", data["Number_of_users"])

