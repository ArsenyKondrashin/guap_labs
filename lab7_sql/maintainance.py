import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('chemists.db')
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''
    DROP TABLE orders
''')
conn.commit()

# CRUD операции
# def create_product(name, price, quantity):
#     cursor.execute('INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)', (name, price, quantity))
#     conn.commit()
#
# def read_product(id):
#     cursor.execute('SELECT * FROM products WHERE id = ?', (id,))
#     return cursor.fetchone()
#
# def update_product(id, name, price, quantity):
#     cursor.execute('UPDATE products SET name = ?, price = ?, quantity = ? WHERE id = ?', (name, price, quantity, id))
#     conn.commit()
#
# def delete_product(id):
#     cursor.execute('DELETE FROM products WHERE id = ?', (id,))
#     conn.commit()
#
# Пример использования CRUD операций
# create_product('apple', 1.0, 100)
# create_product('banana', 0.5, 200)
# print(read_product(1))  # Выведет (1, 'apple', 1.0, 100)
# update_product(1, 'orange', 1.5, 150)
# print(read_product(1))  # Выведет (1, 'orange', 1.5, 150)
# delete_product(2)
# for i in range(1, 10):
#     print(read_product(i))
