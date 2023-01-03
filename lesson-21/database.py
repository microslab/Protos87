import sqlite3


def select_categories():
    database = sqlite3.connect('wallpapers.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT category_name FROM categories
    ''')
    categories = cursor.fetchall()
    database.close()
    return categories


def check_category_name(category_name):
    database = sqlite3.connect('wallpapers.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT category_id FROM categories WHERE category_name = ?
    ''', (category_name,))
    category_id = cursor.fetchone()
    database.close()
    return category_id


def get_image_links(category_id):
    database = sqlite3.connect('wallpapers.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT image_link FROM images WHERE category_id = ?
    ''', (category_id,))
    links = cursor.fetchall()
    database.close()
    return links


def get_image_id(image_link):
    database = sqlite3.connect('wallpapers.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT image_id FROM images WHERE image_link = ?
    ''', (image_link,))
    image_id = cursor.fetchone()
    database.close()
    return image_id


def get_image(image_id):
    database = sqlite3.connect('wallpapers.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT image_link FROM images WHERE image_id = ?
    ''', (image_id,))
    image_link = cursor.fetchone()
    database.close()
    return image_link[0]
