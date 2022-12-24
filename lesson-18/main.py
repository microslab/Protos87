import psycopg2
import requests

database = psycopg2.connect(
    dbname='chetverg15',
    host='localhost',
    user='postgres',
    password='123456'
)

cursor = database.cursor()

users = requests.get('https://jsonplaceholder.typicode.com/users').json()
posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
comments = requests.get('https://jsonplaceholder.typicode.com/comments').json()
albums = requests.get('https://jsonplaceholder.typicode.com/albums').json()
photos = requests.get('https://jsonplaceholder.typicode.com/photos').json()
todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()


for user in users:
    name = user['name']
    username = user['username']
    email = user['email']
    cursor.execute('''
    INSERT INTO users(name, username, email) VALUES (%s, %s, %s)
    ''', (name, username, email))
    database.commit()


for post in posts:
    title = post['title']
    body = post['body']
    userid = post['userId']
    cursor.execute('''
    INSERT INTO posts(title, body, userid) VALUES (%s, %s, %s)
    ''', (title, body, userid))
    database.commit()

for comment in comments:
    name = comment['name']
    email = comment['email']
    body = comment['body']
    cursor.execute('''
    INSERT INTO comments(name, email, body) VALUES (%s, %s, %s)
    ''', (name, email, body))
    database.commit()

for album in albums:
    title = album['title']
    user = album['userId']
    cursor.execute('''
    INSERT INTO albums(userId, title) VALUES (%s, %s)
    ''', (userId, title))
    database.commit()

for photo in photos:
    albumId = photo['albumId']
    title = photo['title']
    url = photo['url']
    thumbnailUrl = photo['thumbnailUrl']
    cursor.execute('''
    INSERT INTO photos(albumId, title, url, thumbnailUrl) VALUES (%s, %s, %s, %s)
    ''', (albumId, title, url, thumbnailUrl))
    database.commit()

for todo in todos:
    userId = todo['userId']
    title = todo['title']
    completed = todo['completed']
    cursor.execute('''
    INSERT INTO todos(userId, title, completed) VALUES (%s, %s, %s)
    ''', (userId, title))
    database.commit()

database.close()
















