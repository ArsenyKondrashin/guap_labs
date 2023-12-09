class ProductsBase():
    def __init__(self, data, cursor,conn):
        self.products = []
        for obj in data:
            product = Product(obj)
            self.products.append(product)
        self.cursor = cursor
        self.conn = conn

    def __len__(self):
        return len(self.products)
    def get_info(self):
        return self.cursor.execute('SELECT * FROM products').fetchall()
    def create_product(self, name, manufacturer_id, quantity, price):
        self.products.append(Product((len(self.products)+1, name, manufacturer_id, quantity, price)))
        self.cursor.execute('INSERT INTO products (name, manufacturer_id, quantity, price) VALUES (?, ?, ?, ?)',
                            (name, manufacturer_id, quantity, price))
        self.conn.commit()
    def delete_product(self, id):
        self.products.pop(id-1)
        self.cursor.execute('DELETE FROM products WHERE id = ?', (id,))
        self.conn.commit()
    def update_product(self, id, name, manufacturer_id, quantity, price):
        self.products[id-1] = Product((id, name, manufacturer_id, quantity, price))
        self.cursor.execute('UPDATE products SET name = ?, manufacturer_id = ?, quantity = ?, price = ? WHERE id = ?',
                            (name, manufacturer_id, quantity, price, id))
        self.conn.commit()

class Product():
    def __init__(self, obj):
        self.id = obj[0]
        self.name = obj[1]
        self.manufacturer_id = obj[2]
        self.quantity = obj[3]
        self.price = obj[4]
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_manufacturer_id(self):
        return self.manufacturer_id
    def get_quantity(self):
        return self.quantity
    def get_price(self):
        return self.price

class ManufacturersBase():
    def __init__(self, data, cursor,conn):
        self.manufacturers = []
        for obj in data:
            manufacturer = Manufacturer(obj)
            self.manufacturers.append(manufacturer)
        self.cursor = cursor
        self.conn = conn

    def __len__(self):
        return len(self.manufacturers)
    def get_info(self):
        return self.cursor.execute('SELECT * FROM manufacturers').fetchall()
    def create_manufacturer(self, name, phonenumber):
        self.manufacturers.append(Manufacturer((len(self.manufacturers)+1, name, phonenumber)))
        self.cursor.execute('INSERT INTO manufacturers (name, phonenumber) VALUES (?, ?)', (name, phonenumber))
        self.conn.commit()
    def delete_manufacturer(self, id):
        self.manufacturers.pop(id-1)
        self.cursor.execute('DELETE FROM manufacturers WHERE id = ?', (id,))
        self.conn.commit()
    def update_manufacturer(self, id, name, phonenumber):
        self.manufacturers[id-1] = Manufacturer((id, name, phonenumber))
        self.cursor.execute('UPDATE manufacturers SET name = ?, phonenumber = ? WHERE id = ?',
                            (name, phonenumber, id))
        self.conn.commit()

class Manufacturer():
    def __init__(self, obj):
        self.id = obj[0]
        self.name = obj[1]
        self.phonenumber = obj[2]
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_phonenumber(self):
        return self.phonenumber

class ClientsBase():
    def __init__(self, data, cursor,conn):
        self.clients = []
        for obj in data:
            client = Client(obj)
            self.clients.append(client)
        self.cursor = cursor
        self.conn = conn

    def __len__(self):
        return len(self.clients)
    def get_info(self):
        return self.cursor.execute('SELECT * FROM clients').fetchall()
    def create_client(self, name, address, phonenumber):
        self.clients.append(Client((len(self.clients)+1, name, address, phonenumber)))
        self.cursor.execute('INSERT INTO clients (name, address, phonenumber) VALUES (?, ?, ?)', (name, address, phonenumber))
        self.conn.commit()
    def delete_client(self, id):
        self.clients.pop(id-1)
        self.cursor.execute('DELETE FROM clients WHERE id = ?', (id,))
        self.conn.commit()
    def update_client(self, id, name, address, phonenumber):
        self.clients[id-1] = Client((id, name, address, phonenumber))
        self.cursor.execute('UPDATE clients SET name = ?, address = ?, phonenumber = ? WHERE id = ?',
                            (name, address, phonenumber, id))
        self.conn.commit()

class Client():
    def __init__(self, obj):
        self.id = obj[0]
        self.name = obj[1]
        self.address = obj[2]
        self.phonenumber = obj[3]
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_adress(self):
        return self.address
    def get_phonenumber(self):
        return self.phonenumber

class SalesBase():
    def __init__(self, data, cursor, conn):
        self.sales = []
        for obj in data:
            self.sales.append(Sale(obj))
        self.conn = conn
        self.cursor = cursor

    def get_info(self):
        return self.cursor.execute('SELECT * FROM sales').fetchall()
    def __len__(self):
        return len(self.sales)
    def create_sale(self, product_id, quantity, client_id, date):
        self.sales.append(Sale((len(self.sales)+1, product_id, quantity, client_id, date)))
        self.cursor.execute('INSERT INTO sales (product_id, quantity, client_id, date) VALUES (?, ?, ?, ?)',
                            (product_id, quantity, client_id, date))
        self.conn.commit()

    def delete_sale(self, id):
        self.sales.pop(id - 1)
        self.cursor.execute('DELETE FROM sales WHERE id = ?', (id,))
        self.conn.commit()

    def update_sale(self, id, product_id, quantity, client_id, date):
        self.sales[id - 1] = Client((id, product_id, quantity, client_id, date))
        self.cursor.execute('UPDATE sales SET product_id = ?, quantity = ?, client_id = ?, date = ? WHERE id = ?',
                            (product_id, quantity, client_id, date, id))
        self.conn.commit()



class Sale():
    def __init__(self, obj):
        self.id = obj[0]
        self.product_id = obj[1]
        self.quantity = obj[2]
        self.client_id = obj[3]
        self.date = obj[4]
    def get_id(self):
        return self.id
    def get_product_id(self):
        return self.product_id
    def get_quantity(self):
        return self.quantity
    def get_client_id(self):
        return self.client_id
    def get_date(self):
        return self.date
