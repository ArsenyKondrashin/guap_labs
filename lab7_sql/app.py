import sqlite3
from classes import ProductsBase, ManufacturersBase, ClientsBase, SalesBase
from functions import *


conn = sqlite3.connect('chemists.db')
cursor = conn.cursor()
get_tables(cursor, conn)
products_parsed_data = cursor.execute('SELECT * FROM products').fetchall()
manufacturers_parsed_data = cursor.execute('SELECT * FROM manufacturers').fetchall()
clients_parsed_data = cursor.execute('SELECT * FROM clients').fetchall()
sales_parsed_data = cursor.execute('SELECT * FROM sales').fetchall()
products = ProductsBase(products_parsed_data, cursor, conn)
manufacturers = ManufacturersBase(manufacturers_parsed_data, cursor, conn)
clients = ClientsBase(clients_parsed_data, cursor, conn)
sales = SalesBase(sales_parsed_data, cursor, conn)
while True:
    print("С какой таблицей будем взаимодействовать?\n"
          " 1 - Таблица товаров\n"
          " 2 - Таблица производителей\n"
          " 3 - Таблица клиентов\n"
          " 4 - Таблица продаж\n"
          )
    task = input("-> ")
    if task == '1':
        productsCRUD(products, manufacturers)
    if task == '2':
        manufacturersCRUD(manufacturers)
    if task == '3':
        clientsCRUD(clients)
    if task == '4':
        salesCRUD(sales, products, clients)