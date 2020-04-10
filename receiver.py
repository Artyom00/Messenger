from datetime import datetime
import requests
from time import sleep

last_message_time = 0
while True:
    response = requests.get('http://127.0.0.1:5000/history', params={'after': last_message_time})
    data = response.json()
    for message in data["messages"]:
        date = datetime.fromtimestamp(message["time"])  # преобразуем float в объект datetime
        date = date.strftime("%a %d/%m/%Y %H:%M:%S")
        print(date, message["username"])
        print(message["text"])
        print()
        last_message_time = message["time"]

    sleep(2)


