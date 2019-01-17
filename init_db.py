#
import psycopg2
from config import connstring, user_list

conn = psycopg2.connect(connstring)
cur = conn.cursor()

cur.execute('''
CREATE TABLE users (
    ID SERIAL,
    username varchar(255),
    email varchar(255),
    notifications int
);''')

cur.execute(
    f'INSERT INTO users (username, email, notifications) VALUES {user_list};')


def print_out():
    cur.execute('select * from users')
    results = cur.fetchall()
    for result in results:
        print(result)


print_out()
