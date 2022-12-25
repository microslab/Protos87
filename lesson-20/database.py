import sqlite3

database = sqlite3.connect('bot.db')
cursor = database.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS history(
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id BIGINT,
    city_name TEXT,
    description TEXT,
    temp INTEGER,
    wind INTEGER,
    sunrise TEXT,
    sunset TEXT
);
''')

database.commit()
database.close()