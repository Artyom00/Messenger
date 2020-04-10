import pyodbc
import time


class MyDatabase:

    def __init__(self, driver, server, database):
        self.driver = driver
        self.server = server
        self.database = database

        try:
            self.conn = pyodbc.connect('Driver={' + self.driver + '};SERVER=' + self.server + ';DATABASE=' + self.database +';Trusted_Connection=Yes')
        except pyodbc.Error as er:
            print('Ошибка при подключении к БД!', er)

        self.cursor = self.conn.cursor()

    def break_connection(self):
        self.cursor.close()
        self.conn.close()

    def select(self, table_name):
        self.cursor.execute(f'select * from {table_name}')
        return self.cursor.fetchall()

    def insert(self, table_name, name, password, text):
        self.cursor.execute(f"""insert into {table_name} values ('{name}','{password}','{text}')""")
        self.conn.commit()


my_db = MyDatabase('ODBC Driver 17 for SQL Server', 'LAPTOP-GGDVFMGH\\SQLEXPRESS', 'messenger')

mess = my_db.select('users')
messages_list = []
for record in mess:
    messages_list.append({"username": record[1], "text": record[3], "time": time.time()})

user = my_db.select('users')
users_dict = {}
for record in user:
    users_dict.update({f'{record[1]}': record[2]})

print(users_dict)