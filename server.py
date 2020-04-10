from flask import Flask, request
from SQLServer import *


app = Flask(__name__)


@app.route("/")
def hello():
    return "My first web app!"


@app.route("/login", methods=['POST'])
def user_login():

    data = request.json
    username = data["username"]
    password = data["password"]

    #  если пользователь существует, проверяем пароль
    #  иначе регистрируем его
    # users_dict = {
    #     username: password
    #     'Jack': '12345',
    #     ...
    # }

    if username in users_dict:
        real_password = users_dict[username]
        if real_password != password:
            return {"Response": False}
    else:
        users_dict[username] = password

    return {"Response": True}


@app.route("/status")
def server_status():
    return {
        "Number_of_messages": len(messages_list),
        "Status": True,
        "Date": time.strftime("%A %d %B %Y %H:%M:%S", time.localtime()),
        "Number_of_users" : len(users_dict)
    }


@app.route("/history")
def history():
    """
    request: ?after=...
     response: {
     "messages_list": [
     {"username": "str", "text": "str", "time": float},
     ...
     ]
     }
    """
    after = float(request.args['after'])

    filtered_messages = []
    for message in messages_list:
        if after < message["time"]:
            filtered_messages.append(message)

    return {"messages": filtered_messages}


@app.route("/send", methods=["POST"])
def send():
    """
     request: {"username": "str", "password": "str", "text": "str"}
     response: {"Response": true}
    """
    data = request.json
    username = data["username"]
    password = data["password"]
    text = data["text"]

    new_message = {"username": username, "text": text, "time": time.time()}
    messages_list.append(new_message)
    my_db.insert('users', username, password, text)

    return {"Response": True}


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/shutdown', methods=['POST', 'GET'])
def shutdown():
    shutdown_server()
    my_db.break_connection()
    return 'Server shutting down...'


app.run()

