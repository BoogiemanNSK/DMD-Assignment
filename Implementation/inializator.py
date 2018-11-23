import sqlite3
import random
import rstr

connection = sqlite3.connect('db.db')
cursor = connection.cursor()

first_names = [name.strip() for name in open('first-names.txt', 'r')]
last_names = [name.strip() for name in open('last-names.txt', 'r')]

def add_car(vals):
    sql = '''INSERT INTO car(plate, battery_charge, location, type, color) 
    VALUES(?,?,?,?,?)'''

    cursor.execute(sql, vals)

def get_plates():
    cursor.execute('SELECT * FROM car;')
    rows = cursor.fetchall()
    plates = []
    for row in rows:
        plates.append(row[0])
    return plates

def get_usernames():
    cursor.execute('SELECT * FROM customer;')
    rows = cursor.fetchall()
    usernames = []
    for row in rows:
        usernames.append(row[0])
    return usernames

def get_phones():
    cursor.execute('SELECT phone FROM customer;')
    rows = cursor.fetchall()
    phones = []
    for row in rows:
        phones.append(row[0])
    return phones

def get_wids():
    cursor.execute('SELECT wid FROM workshop;')
    rows = cursor.fetchall()
    values = []
    for row in rows:
        values.append(row[0])
    return values

def get_sids():
    cursor.execute('SELECT sid FROM charging_station;')
    rows = cursor.fetchall()
    values = []
    for row in rows:
        values.append(row[0])
    return values

def add_random_cars(n):
    plates = get_plates()

    for i in range(n):
        plate = None
        while plate == None or plate in plates:
            plate = rstr.xeger(r'[A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9]')
        battery = random.randint(8, 40) * 100
        location = '{0}, {1}'.format(random.randint(-10000, 10000), random.randint(-10000, 10000))
        cartype = random.choice(['Hatchback', 'Sedan', 'Crossover', 'Coupe'])
        color = random.choice(['Black', 'White', 'Green', 'Red', 'Yellow', 'Cyan', 'Gray', 'Blue',
        'Magenta', 'Purple'])
        
        add_car((plate, battery, location, cartype, color))

def create_random_name():
    return '{} {}'.format(random.choice(first_names), random.choice(last_names))

def create_unique_username():
    names = get_usernames()
    name = None
    while name == None or name in names:
        name = rstr.xeger(r'[a-z][a-z0-9]{2,14}')
    return name

def create_random_location():
    return '{0}, {1}'.format(random.randint(-10000, 10000), random.randint(-10000, 10000))

def create_unique_phone():
    phones = get_phones()
    phone = None
    while phone == None or phone in phones:
        phone = '+1' + rstr.xeger(r'[0-9]{10}')
    return phone

def add_customer(vals):
    sql = '''INSERT INTO customer(username, fullname, address, phone, email) 
    VALUES(?,?,?,?,?)'''

    cursor.execute(sql, vals)

def add_workshop(vals):
    sql = '''INSERT INTO workshop(wid, availability, location) 
    VALUES(?,?,?)'''

    cursor.execute(sql, vals)

def add_random_workshops(n):
    wid = 0
    wids = get_wids()
    for i in range(n):
        while wid in wids:
            wid += 1
        wids.append(wid)
        availability = '{}-{}'.format(random.randint(0, 10), random.randint(11, 24))
        location = create_random_location()

        add_workshop((wid, availability, location))

def add_random_customers(n):
    for i in range(n):
        username = create_unique_username()
        fullname = create_random_name()
        address = create_random_location()
        phone = create_unique_phone()
        email = '{}@{}'.format(username, random.choice(['gmail.com', 'yandex.com', 'aol.com',
        'outlook.com', 'yahoo.com', 'hotmail.com']))

        add_customer((username, fullname, address, phone, email))

def add_station(vals):
    sql = '''INSERT INTO charging_station(sid, location, 
    soc_shape, soc_size, soc_count, cost, charging_time) VALUES(?,?,?,?,?,?,?)'''

    cursor.execute(sql, vals)

def add_random_stations(n):
    sid = 0
    sids = get_sids()
    for i in range(n):
        while sid in sids:
            sid += 1
        sids.append(sid)
        location = create_random_location()
        shape = random.choice(['square', 'rectangular', 'circular', 'semicircular', 'oval', 
        'triangular', 'hexagonal', 'octagonal'])
        size = random.choice(['Tiny', 'Small', 'Normal', 'Big', 'Huge'])
        count = random.randint(2, 10)
        cost = random.randint(5, 20) * 100
        time = random.randint(4, 24) * 5

        add_station((sid, location, shape, size, count, cost, time))

add_random_stations(20)

connection.commit()
connection.close()
