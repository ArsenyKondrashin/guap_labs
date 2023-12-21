from fnmatch import *
def get_tables(cursor, conn):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            manufacturer_id INTEGER,
            quantity INTEGER,
            price INTEGER
        )
    ''')
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS manufacturers (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    phonenumber INTEGER
                )
    ''')
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS clients (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    address TEXT,
                    phonenumber INTEGER
                )
    ''')
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS sales (
                    id INTEGER PRIMARY KEY,
                    product_id INTEGER,
                    quantity INTEGER,
                    client_id INTEGER,
                    date DATE
                )
    ''')
    conn.commit()

def productsCRUD(products, manufacturers):
    while True:
        print("Что будем делать?\n"
              " 1 - получать данные\n"
              " 2 - менять данные\n"
              " 3 - удалять данные\n"
              " q - завершить программу")
        task = input("-> ")

        if task == '1':
            refresh_id(products)
            products_list = products.get_info()
            print('<- - - - - - ->')
            for product in products_list:
                print('id:', product[0])
                print('название:', product[1])
                print('id производителя:', product[2])
                print('в наличии:', product[3])
                print('цена:', product[4])
                print('<- - - - - - ->')

        elif task == '2':
            print("Что будем делать?\n"
                  " 1 - создавать новый продукт\n"
                  " 2 - менять значения в имеющемся продукте\n")
            task = input("-> ")

            if task == '1':
                creation_data = get_product_creation_data(manufacturers)
                products.create_product(creation_data["name"], creation_data["manufacturer_id"], creation_data["quantity"],
                                        creation_data["price"])

            elif task == '2':
                if len(products) > 0:
                    id = get_id(products)
                    update_data = get_product_update_data(manufacturers)
                    products.update_product(id, update_data["name"], update_data["manufacturer_id"],
                                            update_data["quantity"], update_data["price"])
                else:
                    print('Нечего изменять')

        elif task == '3':
            if len(products) > 0:
                id = get_id(products)
                products.delete_product(id)
            else:
                print('Нечего удалять')
            refresh_id(products)
        elif task == 'q':
            exit()
def manufacturersCRUD(manufacturers):
    while True:
        print("Что будем делать?\n"
              " 1 - получать данные\n"
              " 2 - менять данные\n"
              " 3 - удалять данные\n"
              " q - завершить программу")
        task = input("-> ")

        if task == '1':
            refresh_id(manufacturers)
            manufacturers_list = manufacturers.get_info()
            print('<- - - - - - ->')
            for manufacturer in manufacturers_list:
                print('id:', manufacturer[0])
                print('название:', manufacturer[1])
                print('номер телефона:', manufacturer[2])
                print('<- - - - - - ->')

        elif task == '2':
            print("Что будем делать?\n"
                  " 1 - создавать нового производителя\n"
                  " 2 - менять значения в имеющемся производителе\n")
            task = input("-> ")

            if task == '1':
                creation_data = get_manufacturer_creation_data()
                manufacturers.create_manufacturer(creation_data["name"], creation_data["phonenumber"])

            elif task == '2':
                if len(manufacturers) > 0:
                    id = get_id(manufacturers)
                    update_data = get_manufacturer_update_data()
                    manufacturers.update_manufacturer(id, update_data["name"], update_data["phonenumber"])
                else:
                    print('Нечего изменять')

        elif task == '3':
            if len(manufacturers) > 0:
                id = get_id(manufacturers)
                manufacturers.delete_manufacturer(id)
            else:
                print('Нечего удалять')
            refresh_id(manufacturers)

        elif task == 'q':
            exit()
def clientsCRUD(clients):
    while True:
        print("Что будем делать?\n"
              " 1 - получать данные\n"
              " 2 - менять данные\n"
              " 3 - удалять данные\n"
              " q - завершить программу")
        task = input("-> ")

        if task == '1':
            refresh_id(clients)
            clients_list = clients.get_info()
            print('<- - - - - - ->')
            for client in clients_list:
                print('id:', client[0])
                print('имя:', client[1])
                print('адрес:', client[2])
                print('номер телефона:', client[3])
                print('<- - - - - - ->')

        elif task == '2':
            print("Что будем делать?\n"
                  " 1 - создавать нового клиента\n"
                  " 2 - менять значения в имеющемся клиента\n")
            task = input("-> ")

            if task == '1':
                creation_data = get_client_creation_data()
                clients.create_client(creation_data["name"], creation_data["address"], creation_data["phonenumber"])

            elif task == '2':
                if len(clients) > 0:
                    id = get_id(clients)
                    update_data = get_client_update_data()
                    clients.update_client(id, update_data["name"], update_data["address"], update_data["phonenumber"])
                else:
                    print('Нечего изменять')

        elif task == '3':
            if len(clients) > 0:
                id = get_id(clients)
                clients.delete_client(id)
            else:
                print('Нечего удалять')
            refresh_id(clients)

        elif task == 'q':
            exit()
def salesCRUD(sales, products, clients):
    while True:
        print("Что будем делать?\n"
              " 1 - получать данные\n"
              " 2 - менять данные\n"
              " 3 - удалять данные\n"
              " q - завершить программу")
        task = input("-> ")

        if task == '1':
            refresh_id(sales)
            sales_list = sales.get_info()
            print('<- - - - - - ->')
            for sale in sales_list:
                print('id:', sale[0])
                print('id продукта:', sale[1])
                print('количество:', sale[2])
                print('id клиента:', sale[3])
                print('дата:', sale[4])
                print('<- - - - - - ->')

        elif task == '2':
            print("Что будем делать?\n"
                  " 1 - создавать новую продажу\n"
                  " 2 - менять значения в имеющейся продаже\n")
            task = input("-> ")

            if task == '1':
                creation_data = get_sale_creation_data(products, clients)
                sales.create_sale(creation_data["product_id"], creation_data["quantity"], creation_data["client_id"], creation_data["date"])

            elif task == '2':
                if len(sales) > 0:
                    id = get_id(sales)
                    update_data = get_sale_update_data(products, clients)
                    sales.update_sale(id, update_data["product_id"], update_data["quantity"], update_data["client_id"], update_data["date"])
                else:
                    print('Нечего изменять')

        elif task == '3':
            if len(sales) > 0:
                id = get_id(sales)
                sales.delete_sale(id)
            else:
                print('Нечего удалять')
            refresh_id(sales)

        elif task == 'q':
            exit()
def get_product_creation_data(manufacturers):
    while True:
        name = input("Введите имя продукта ")
        if len(name.split()) > 0:
            break
        else:
            print("Введена пустая строка")
    if len(manufacturers) > 0:
        print("ID производителя:")
        manufacturer_id = get_id(manufacturers)
    else:
        print('Нет производителей')
        exit()
    # while True:
    #     manufacturer_id = input("Введите id производителя продукта ")
    #     try:
    #         manufacturer_id = int(manufacturer_id)
    #         if manufacturer_id >= 0:
    #             break
    #         else:
    #             print("Введите неотрицательное число")
    #     except:
    #         print("Введите натуральное число")
    while True:
        quantity = input("Введите количество продукта в штуках ")
        try:
            quantity = int(quantity)
            if quantity >= 0:
                break
            else:
                print("Введите неотрицательное число")
        except:
            print("Введите натуральное число")
    while True:
        price = input("Введите цену продукта ")
        try:
            price = int(price)
            if price > 0:
                break
            else:
                print("Введите положительное число")
        except:
            print("Введите натуральное число")
    return {"name": name, "manufacturer_id": manufacturer_id, "quantity": quantity, "price": price}
def get_manufacturer_creation_data():
    while True:
        name = input("Введите имя продавца ")
        if len(name.split()) > 0:
            break
        else:
            print("Введена пустая строка")
    while True:
        phonenumber = input("Введите номер телефона ")
        try:
            phonenumber = int(phonenumber)
            if phonenumber > 0:
                break
            else:
                print("Введите положительное число")
        except:
            print("Введите натуральное число")
    return {"name": name, "phonenumber": phonenumber}
def get_client_creation_data():
    while True:
        name = input("Введите имя клиента ")
        if len(name.split()) > 0:
            break
        else:
            print("Введена пустая строка")
    while True:
        address = input("Введите адрес клиента ")
        if len(address.split()) > 0:
            break
        else:
            print("Введена пустая строка")
    while True:
        phonenumber = input("Введите номер телефона ")
        try:
            phonenumber = int(phonenumber)
            if phonenumber > 0:
                break
            else:
                print("Введите положительное число")
        except:
            print("Введите натуральное число")
    return {"name": name, "address": address, "phonenumber": phonenumber}
def get_sale_creation_data(products, clients):
    if len(products) > 0:
        print("ID продукта:")
        product_id = get_id(products)
    else:
        print('Нет продуктов')
        exit()
    # while True:
    #     product_id = input("Введите id продукта ")
    #     try:
    #         product_id = int(product_id)
    #         if product_id >= 0:
    #             break
    #         else:
    #             print("Введите неотрицательное число")
    #     except:
    #         print("Введите натуральное число")
    while True:
        quantity = input("Введите количество продукта в штуках ")
        try:
            quantity = int(quantity)
            if quantity >= 0:
                break
            else:
                print("Введите неотрицательное число")
        except:
            print("Введите натуральное число")
    if len(products) > 0:
        print("ID клиента:")
        client_id = get_id(clients)
    else:
        print('Нет клиентов')
        exit()
    # while True:
    #     client_id = input("Введите id клиента ")
    #     try:
    #         client_id = int(client_id)
    #         if client_id > 0:
    #             break
    #         else:
    #             print("Введите положительное число")
    #     except:
    #         print("Введите натуральное число")
    while True:
        date = input("Введите дату продажи в формате ГГГГ-ММ-ДД ")
        if fnmatch(date, '????-??-??'):
            x = date.replace('-', '0')
            try:
                x = int(x)
                break
            except ValueError:
                print("Дата введена неверно")
    return {"product_id": product_id, "quantity": quantity, "client_id": client_id, "date": date}
def get_product_update_data(manufacturers):
    while True:
        name = input("Введите имя продукта ")
        if len(name.split()) > 0:
            break
        else:
            print("Введена пустая строка")
    if len(manufacturers) > 0:
        print("ID производителя:")
        manufacturer_id = get_id(manufacturers)
    else:
        print('Нет производителей')
        exit()
    # while True:
    #     manufacturer_id = input("Введите id производителя продукта ")
    #     try:
    #         manufacturer_id = int(manufacturer_id)
    #         if manufacturer_id >= 0:
    #             break
    #         else:
    #             print("Введите неотрицательное число")
    #     except:
    #         print("Введите натуральное число")
    while True:
        quantity = input("Введите количество продукта в штуках ")
        try:
            quantity = int(quantity)
            if quantity >= 0:
                break
            else:
                print("Введите неотрицательное число")
        except:
            print("Введите натуральное число")
    while True:
        price = input("Введите цену продукта ")
        try:
            price = int(price)
            if price > 0:
                break
            else:
                print("Введите положительное число")
        except:
            print("Введите натуральное число")
    return {"name": name, "manufacturer_id": manufacturer_id, "quantity": quantity, "price": price}
def get_manufacturer_update_data():
    while True:
        name = input("Введите название производителя ")
        if len(name.split()) > 0:
            break
        else:
            print("Введена пустая строка")
    while True:
        phonenumber = input("Введите номер телефона ")
        try:
            phonenumber = int(phonenumber)
            if phonenumber > 0:
                break
            else:
                print("Введите положительное число")
        except:
            print("Введите натуральное число")
    return {"name": name, "phonenumber": phonenumber}
def get_client_update_data():
    while True:
        name = input("Введите имя клиента ")
        if len(name.split()) > 0:
            break
        else:
            print("Введена пустая строка")
    while True:
        address = input("Введите адрес клиента ")
        if len(address.split()) > 0:
            break
        else:
            print("Введена пустая строка")
    while True:
        phonenumber = input("Введите номер телефона ")
        try:
            phonenumber = int(phonenumber)
            if phonenumber > 0:
                break
            else:
                print("Введите положительное число")
        except:
            print("Введите натуральное число")
    return {"name": name, "address": address, "phonenumber": phonenumber}
def get_sale_update_data(products, clients):
    if len(products) > 0:
        print("ID продукта:")
        product_id = get_id(products)
    else:
        print('Нет продуктов')
        exit()
    # while True:
    #     product_id = input("Введите id продукта ")
    #     try:
    #         product_id = int(product_id)
    #         if product_id >= 0:
    #             break
    #         else:
    #             print("Введите неотрицательное число")
    #     except:
    #         print("Введите натуральное число")
    while True:
        quantity = input("Введите количество продукта в штуках ")
        try:
            quantity = int(quantity)
            if quantity >= 0:
                break
            else:
                print("Введите неотрицательное число")
        except:
            print("Введите натуральное число")
    if len(products) > 0:
        print("ID клиента:")
        client_id = get_id(clients)
    else:
        print('Нет клиентов')
        exit()
    # while True:
    #     client_id = input("Введите id клиента ")
    #     try:
    #         client_id = int(client_id)
    #         if client_id > 0:
    #             break
    #         else:
    #             print("Введите положительное число")
    #     except:
    #         print("Введите натуральное число")
    while True:
        date = input("Введите дату продажи в формате ГГГГ-ММ-ДД ")
        if fnmatch(date, '????-??-??'):
            x = date.replace('-', '0')
            try:
                x = int(x)
                break
            except ValueError:
                print("Дата введена неверно")
    return {"product_id": product_id, "quantity": quantity, "client_id": client_id, "date": date}
def get_id(obj):
    while True:
        id = input("Введите id ")
        try:
            id = int(id)
            if (id <= len(obj)) and (id > 0):
                break
            else:
                print("Введён несуществующий id")
        except:
            print("Введите натуральное число")
    return id
def refresh_id(obj):
    objects = obj.get_info()
    print(len(obj))
    for i in range(len(objects)):
        if objects[i][0] != i + 1:
            obj.update_id(objects[i][0], i + 1)
