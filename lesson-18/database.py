import psycopg2

database = psycopg2.connect(
    dbname='chetverg15',
    host='localhost',
    user='postgres',
    password='123456'
)

cursor = database.cursor()
cursor.execute('''
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS photos;
DROP TABLE IF EXISTS todos;
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(60),
    username VARCHAR(30),
    email  VARCHAR(100)
);
CREATE TABLE IF NOT EXISTS posts(
    user_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title TEXT,
    body TEXT,
    userid INTEGER REFERENCES users(user_id) 
);
CREATE TABLE IF NOT EXISTS comments(
    comments_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT,
    email TEXT,
    body TEXT
);
CREATE TABLE IF NOT EXISTS albums(
    albums_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title TEXT,
    userid INTEGER REFERENCES users(user_id) 
);
CREATE TABLE IF NOT EXISTS photos(
    photos_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    albumId INTEGER,
    title TEXT,
    url TEXT,
    thumbnailUrl TEXT
);
CREATE TABLE IF NOT EXISTS todos(
    todos_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title TEXT,
    completed TEXT,
    userid INTEGER REFERENCES users(user_id) 
);
''')

database.commit()
database.close()