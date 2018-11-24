import sqlite3
import random
import rstr
import datetime

connection = sqlite3.connect('db.db')
cursor = connection.cursor()

first_names = [name.strip() for name in open('first-names.txt', 'r')]
last_names = [name.strip() for name in open('last-names.txt', 'r')]

def add_car(vals):
    sql = '''INSERT INTO car(plate, battery_charge, location, type, color) 
    VALUES(?,?,?,?,?);'''

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
    cursor.execute('SELECT phone FROM car_parts_provider;')
    rows = cursor.fetchall()
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
    VALUES(?,?,?,?,?);'''

    cursor.execute(sql, vals)

def add_workshop(vals):
    sql = '''INSERT INTO workshop(wid, availability, location) 
    VALUES(?,?,?);'''

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
    soc_shape, soc_size, soc_count, cost, charging_time) VALUES(?,?,?,?,?,?,?);'''
    cursor.execute(sql, vals)

def add_carpart(vals):
    sql = '''INSERT INTO car_part(name, price, ptype) VALUES(?,?,?);'''
    cursor.execute(sql, vals)

def add_provider(vals):
    sql = '''INSERT INTO car_parts_provider(pid, name, phone, address) VALUES(?,?,?,?);'''
    cursor.execute(sql, vals)

def add_car_uses_charging_station(vals):
    sql = '''INSERT INTO car_uses_charging_station(plate, sid, start_time) VALUES(?,?,?);'''
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

carpart_types = [('Wheel', 300), ('Transmission', 4000), ('Engine', 7000), 
('Door', 1000), ('Window', 1000), ('Bonnet', 200), ('Bumper', 400)]
companies = ['MacMisson', 'Leod', 'Hugh Motors', 'Olle', 'Friendly Steel', 'Voi Segh']
providers = ['Nice & Fast', 'Running Snake', 'Loose Power', 'SNC', 'UrbanS', 'MyFare']

def add_carparts_by(name):
    for parttype in carpart_types:
        partname = "{}'s {}".format(name, parttype[0])
        price = parttype[1] + random.randint(-200, 400)
        add_carpart((partname, price, parttype[0]))

def add_providers():
    pid = 0
    for provider in providers:
        location = create_random_location()
        phone = create_unique_phone()
        add_provider((pid, provider, phone, location))
        pid += 1

def get_stations():
    sql = ''' SELECT * FROM charging_station; '''
    cursor.execute(sql)
    return cursor.fetchall()

def get_providers():
    sql = ''' SELECT * FROM car_parts_provider; '''
    cursor.execute(sql)
    return cursor.fetchall()

def get_cars():
    sql = ''' SELECT * FROM car; '''
    cursor.execute(sql)
    return cursor.fetchall()

def get_parts():
    sql = "SELECT * FROM car_part;"
    cursor.execute(sql)
    return cursor.fetchall()

def get_parts_of_car(plate):
    sql = "SELECT * FROM car_part_used_in_car WHERE plate='{}';".format(plate)
    cursor.execute(sql)
    return cursor.fetchall()

def get_workshops():
    sql = "SELECT * FROM workshop;"
    cursor.execute(sql)
    return cursor.fetchall()

def fill_car_uses_charging_station():
    allcars = get_cars()
    for station in get_stations():
        now = datetime.datetime.now()
        while now < datetime.datetime.now() + datetime.timedelta(days=40):
            cars = []
            car = None
            for i in range(random.randint(0, station[4])):
                while car == None or car in cars:
                    car = random.choice(allcars)
                cars.append(car)
                add_car_uses_charging_station((car[0], station[0], now))
            now += datetime.timedelta(hours=random.randint(1, 4))

def get_parts_of_type(parttype):
    sql = "SELECT name FROM car_part WHERE ptype='{0}';".format(parttype)
    cursor.execute(sql)
    return cursor.fetchall()

def add_car_part_used_in_car(vals):
    sql = '''INSERT INTO car_part_used_in_car(pname, plate) VALUES(?,?)'''
    cursor.execute(sql, vals)

def add_car_part_provided_by(vals):
    sql = '''INSERT INTO car_part_provided_by(pname, prid) VALUES(?,?)'''
    cursor.execute(sql, vals)

def add_car_part_available_in_workshop(vals):
    sql = '''INSERT INTO car_part_available_in_workshop(pname, wid) VALUES(?,?)'''
    cursor.execute(sql, vals)

def add_workshop_repaired_car(vals):
    sql = '''INSERT INTO workshop_repaired_car(wid, plate, pname, start_time, duration) VALUES(?,?,?,?,?)'''
    cursor.execute(sql, vals)

def fill_car_part_used_in_car():
    cars = get_cars()
    for car in cars:
        for part in carpart_types:
            used_part = random.choice(get_parts_of_type(part[0]))
            add_car_part_used_in_car((used_part[0], car[0]))

def fill_car_part_provided_by():
    parts = get_parts()
    providers = get_providers()
    for part in parts:
        provided_for = []
        for i in range(random.randint(1, len(providers))):
            provider = None
            while provider == None or provider in provided_for:
                provider = random.choice(providers)
            provided_for.append(provider)
            add_car_part_provided_by((part[0], provider[0]))
    
def fill_car_part_available_in_workshop():
    parts = get_parts()
    workshops = get_workshops()
    for part in parts:
        provided_for = []
        for i in range(random.randint(1, len(workshops))):
            workshop = None
            while workshop == None or workshop in provided_for:
                workshop = random.choice(workshops)
            provided_for.append(workshop)
            add_car_part_available_in_workshop((part[0], workshop[0]))

def fill_workshop_repaired_car():
    end = datetime.datetime.now() + datetime.timedelta(days=40)
    cars = get_cars()
    workshops = get_workshops()
    parts = get_parts()
    for car in cars:
        carparts = get_parts_of_car(car[0])
        now = datetime.datetime.now() + datetime.timedelta(days=random.randint(0, 41))
        while now < end:
            duration = 1
            workshop = random.choice(workshops)
            time = [a.strip() for a in workshop[1].split('-')]
            start = random.randint(int(time[0]), int(time[1]))
            now.replace(hour=start-duration, minute=random.randint(0, 59))
            no = random.randint(1, len(carparts))
            while no > 0:
                now += datetime.timedelta(hours=duration)
                part = random.choice(carparts)
                add_workshop_repaired_car((workshop[0], car[0], part[0], now, duration))
                duration = random.randint(1, 4)
                no-=1
            now += datetime.timedelta(days=random.randint(0, 41))









connection.commit()
connection.close()
