import requests

username = input("Enter username: ")
while True:
    password = input("Enter password: ")
    response = requests.post(
        'http://127.0.0.1:5000/login',
        json={"username": username, "password": password}
                             )

    if not response.json()["Response"]:
        print("Password entered incorrectly! Try again")
        continue
    else:
        while True:
            text = input("Enter message: ")
            response = requests.post(
                'http://127.0.0.1:5000/send',
                json={"username": username, "password": password, "text": text}
                                    )


