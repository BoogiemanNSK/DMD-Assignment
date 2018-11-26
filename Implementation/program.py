import sqlite3

sql_1 = """
SELECT plate
FROM car
WHERE plate LIKE 'AN%' AND color = 'Red'
"""

# for each hour (0-23)
sql_2 = """
SELECT COUNT(*) FROM car_uses_charging_station
WHERE date(start_time) = date('[given_date]') AND CAST(strftime('%H', start_time) AS INTEGER) < [given_time] + 1 AND
CAST(strftime('%H', end_time) AS INTEGER) > [given_time]"""

sql_3_1 = """
SELECT 100 * ((
	SELECT COUNT(*)
	FROM customer_uses_car
	WHERE datetime(start_time, '+7 day') > datetime('now') AND
	 CAST(strftime('%H', start_time) AS INTEGER) > 7 AND
	 CAST(strftime('%H', start_time) AS INTEGER) < 10
) * 1.0) / ((SELECT COUNT(*) FROM car) * 7.0)
"""

sql_3_2 = """
SELECT 100 * ((
	SELECT COUNT(*)
	FROM customer_uses_car
	WHERE datetime(start_time, '+7 day') > datetime('now') AND
	 CAST(strftime('%H', start_time) AS INTEGER) > 12 AND
	 CAST(strftime('%H', start_time) AS INTEGER) < 14
) * 1.0) / ((SELECT COUNT(*) FROM car) * 7.0)
"""

sql_3_3 = """
SELECT 100 * ((
	SELECT COUNT(*)
	FROM customer_uses_car
	WHERE datetime(start_time, '+7 day') > datetime('now') AND
	 CAST(strftime('%H', start_time) AS INTEGER) > 17 AND
	 CAST(strftime('%H', start_time) AS INTEGER) < 19
) * 1.0) / ((SELECT COUNT(*) FROM car) * 7.0)
"""

sql_4 = """
SELECT customer, start_time, cost
FROM customer_uses_car
WHERE customer = '[given_name]'
GROUP BY start_time
HAVING COUNT(*) > 1
"""

sql_5_1 = """
SELECT AVG(distance)
FROM customer_uses_car
WHERE date(start_time) = date('[given_date]') AND type = 'order'
"""

sql_5_2 = """
SELECT AVG(duration)
FROM customer_uses_car
WHERE date(start_time) = date('[given_date]') AND type = 'trip'
"""

sql_6_1 = """
SELECT destination
FROM (
	SELECT destination, COUNT (*) AS c
	FROM customer_uses_car
	WHERE type = 'trip' AND CAST(strftime('%H', start_time) AS INTEGER) > 7 AND CAST(strftime('%H', start_time) AS INTEGER) < 10
	GROUP BY destination
)
ORDER BY c
LIMIT 3
"""

sql_6_2 = """
SELECT destination
FROM (
	SELECT destination, COUNT (*) AS c
	FROM customer_uses_car
	WHERE type = 'trip' AND CAST(strftime('%H', start_time) AS INTEGER) > 12 AND CAST(strftime('%H', start_time) AS INTEGER) < 14
	GROUP BY destination
)
ORDER BY c
LIMIT 3
"""

sql_6_3 = """
SELECT destination
FROM (
	SELECT destination, COUNT (*) AS c
	FROM customer_uses_car
	WHERE type = 'trip' AND CAST(strftime('%H', start_time) AS INTEGER) > 17 AND CAST(strftime('%H', start_time) AS INTEGER) < 19
	GROUP BY destination
)
ORDER BY c
LIMIT 3
"""

sql_6_4 = """
SELECT destination
FROM (
	SELECT destination, COUNT (*) AS c
	FROM customer_uses_car
	WHERE type = 'order' AND CAST(strftime('%H', start_time) AS INTEGER) > 7 AND CAST(strftime('%H', start_time) AS INTEGER) < 10
	GROUP BY destination
)
ORDER BY c
LIMIT 3
"""

sql_6_5 = """
SELECT destination
FROM (
	SELECT destination, COUNT (*) AS c
	FROM customer_uses_car
	WHERE type = 'order' AND CAST(strftime('%H', start_time) AS INTEGER) > 12 AND CAST(strftime('%H', start_time) AS INTEGER) < 14
	GROUP BY destination
)
ORDER BY c
LIMIT 3
"""

sql_6_6 = """
SELECT destination
FROM (
	SELECT destination, COUNT (*) AS c
	FROM customer_uses_car
	WHERE type = 'order' AND CAST(strftime('%H', start_time) AS INTEGER) > 17 AND CAST(strftime('%H', start_time) AS INTEGER) < 19
	GROUP BY destination
)
ORDER BY c
LIMIT 3
"""

sql_7 =  """
SELECT car, c
FROM (
	SELECT car, count(*) as c
	FROM customer_uses_car
	WHERE datetime(start_time, '+3 month') > datetime('now')
	GROUP BY car
)
ORDER BY c ASC
LIMIT (SELECT (SELECT COUNT(*) FROM car) / 10)
"""

sql_8 = """
SELECT customer, COUNT(*) AS charges
FROM (
	SELECT customer_uses_car.car, customer_uses_car.customer, customer_uses_car.start_time
	FROM customer_uses_car INNER JOIN car_uses_charging_station ON customer_uses_car.car = car_uses_charging_station.plate
	WHERE strftime('%m', car_uses_charging_station.start_time) = strftime('%m', customer_uses_car.start_time)
)
GROUP BY customer
ORDER BY charges
"""

sql_9 = """ 
SELECT wid, pname, c
FROM (
    SELECT wid, pname, (SELECT CAST (strftime('%Y', start_time) AS INTEGER) * 53 + CAST (strftime('%W', start_time) AS INTEGER)) AS week, COUNT (*) AS c
    FROM workshop_repaired_car
    GROUP BY week
    ORDER BY c DESC
	LIMIT 1
)
"""

sql_10 = """
SELECT plate, AVG(cost) as cost
FROM (
	SELECT car_uses_charging_station.plate, charging_station.cost
	FROM charging_station INNER JOIN car_uses_charging_station ON charging_station.sid = car_uses_charging_station.sid
	UNION ALL
	SELECT workshop_repaired_car.plate, car_part.price AS cost
	FROM car_part INNER JOIN workshop_repaired_car ON car_part.name = workshop_repaired_car.pname
	GROUP BY plate
)
ORDER BY cost DESC
LIMIT 1
"""

sql_table = """ SELECT * FROM [table_name] """

tables = (['car', 'plate', 'battery', 'location', 'type', 'color'],
['car_part', 'name', 'price', 'ptype'],
['car_part_available_in_workshop', 'pname', 'wid'],
['car_part_provided_by', 'pname', 'prid'],
['car_part_used_in_car', 'pname', 'plate'],
['car_parts_provider', 'pid', 'name', 'phone', 'address'],
['car_uses_charging_station', 'plate', 'sid', 'start_time', 'end_time'],
['charging_station', 'sid', 'location', 'soc_shape', 'soc_size', 'soc_count', 'cost', 'charging_time'],
['customer', 'username', 'fullname', 'address', 'phone', 'email'],
['customer_uses_car', 'uid', 'type', 'customer', 'car', 'destination', 'distance', 'start_time', 'duration', 'cost'],
['workshop', 'wid', 'availability', 'location'],
['workshop_repaired_car', 'wid', 'plate', 'pname', 'start_time', 'duration'])

conn = sqlite3.connect('db.db')
cur = conn.cursor()

def select_rows(sql, vals):
	if len(vals) == 0:
		cur.execute(sql)
	else:
		for val in vals:
			sql = sql.replace("[{}]".format(str(val[0])), str(val[1]))
		cur.execute(sql)
	return cur.fetchall()

def print_rows(rows, header='', counter=True):
	incr = 0
	print(header)
	for row in rows:
		if counter == True:
			print('{} ->'.format(incr), end='')
		for i in range(len(row)):
			print('\t{}'.format(row[i]), end='')
		print('')
		incr += 1
 	
def print_menu():
	print('Hello, dear user. In this menu you can execute one of the specified queries.')
	print('\n(0) Print a table.')
	print('\n(1) 3.1 A customer claims she forgot her bag in a car and asks to help. '
	'She was using cars severaltimes this day, but she believes the right car was red and its plate starts with “AN”. '
	'Find all possible cars that match the description.')
	print('\n(2) 3.2 Company management wants to get a statistics on the efficiency of charging stations utilization. '
	'Given a date, compute how many sockets were occupied each hour.')
	print('\n(3) 3.3 Company management considers using price increasing coefficients. '
	'They need to gather statistics for one week on how many cars are busy ' 
	'(% to the total amount of taxis) during the morning (7AM - 10 AM), afternoon '
	'(12AM - 2PM) and evening (5PM - 7PM) time.')
	print("\n(4) 3.4 A customer claims that he was charged twice for the trip, but he can’t say exactly what day it "
	"happened (he deleted notification from his phone and he is too lazy to ask the bank), so you "
	"need to check all his payments for the last month to be be sure that nothing was doubled.")
	print('\n(5) 3.5 The department of development has requested the following statistics:\n'
	'- Average distance a car has to travel per day to customer’s order location\n'
	'- Average trip duration\n'
	'Given a date as an input, compute the statistics above')
	print('\n(6) 3.6 In order to accommodate traveling demand, the company decided to distribute cars according '
	'to demand locations. Your task is to compute top-3 most popular pick-up locations and travel '
	'destination for each time of day: morning (7am-10am), afternoon (12am-2pm) and evening (5pm-7pm).')
	print('\n(7) 3.7 Despite the wise management, the company is going through hard times and can’t afford '
	'anymore to maintain the current amount of self-driving cars. The management decided to stop '
	'using 10% of all self-driving cars, which take least amount of orders for the last 3 months.')
	print("\n(8) 3.8 The company management decided to participate in the research on 'does customer location "
	'of residence depend on how many charging station the self-driving cars was using the same '
	"day'. Now you as DB developer need to provide this data. You've decided to collect the data "
	'for each day within one month and then sum them up.')
	print('\n(9) 3.9 The company management decided to optimize repair costs by buying parts in bulks from '
	'providers for every workshop. Help them decide which parts are used the most every week by '
	'every workshop and compute the necessary amount of parts to order.')
	print('\n(10) 3.10 The company management decided to cut costs by getting rid of the most expensive car to '
	'maintain. Find out which car type has had the highest average (per day) cost of repairs and '
	'charging (combined).')
	print('\nPlease do not insert SQL injections, they might cause irrevertible damage to the database!')
	print('\n(q) Exit.\n')
	
def get_choice():
	try:
		choice = input('Choice: ')
		if choice == 'q':
			exit()
		elif choice == 'm':
			print_menu()
			choice = -2
		else:
			choice = int(choice)
	except ValueError:
		return -1
	return choice
	
def process_choice(choice):
	if choice == -1:
		print("Input is not a number. Type 'q' to exit or 'm' to print the menu.")
	elif choice == -2:
		return
	elif choice > 10 or choice < 0:
		print('No such option available.')
	elif choice == 0:
		print('Choose one of the following tables:')
		for table in tables:
			print('- {}'.format(table[0]))
		chosen_table = input('Table name: ')
		for table in tables:
			if chosen_table == table[0]:
				print_table(table[0], table[1:-1])
				return
		print('No such table.')
	elif choice == 1:
		rows = select_rows(sql_1, [])
		print_rows(rows)
	elif choice == 2:
		date = input("Enter date in format 'YYYY-MM-DD': ")
		for hour in range(0, 24):
			rows = select_rows(sql_2, [('given_date', date), ('given_time', hour)])
			print_rows(rows, '{}:00 - {}:00'.format(str(hour), str(hour+1)), counter=False)
	elif choice == 3:
		rows = select_rows(sql_3_1, [])
		print_rows(rows, 'Morning', counter=False)
		rows = select_rows(sql_3_2, [])
		print_rows(rows, 'Afternoon', counter=False)
		rows = select_rows(sql_3_3, [])
		print_rows(rows, 'Evening', counter=False)
	elif choice == 4:
		username = input('Type username: ')
		rows = select_rows(sql_4, [('given_name', username)])
		print_rows(rows, 'Result')
	elif choice == 5:
		date = input("Enter date in format 'YYYY-MM-DD': ")
		rows = select_rows(sql_5_1, [('given_date', date)])
		print_rows(rows, 'Avg. Distance', counter=False)
		rows = select_rows(sql_5_2, [('given_date', date)])
		print_rows(rows, 'Avg. Duration', counter=False)
	elif choice == 6:
		rows = select_rows(sql_6_1, [])
		print_rows(rows, 'Trips (7 - 10)', counter=False)
		rows = select_rows(sql_6_2, [])
		print_rows(rows, 'Trips (12 - 14)', counter=False)
		rows = select_rows(sql_6_3, [])
		print_rows(rows, 'Trips (17 - 19)', counter=False)
		rows = select_rows(sql_6_4, [])
		print_rows(rows, 'Orders (7 - 10)', counter=False)
		rows = select_rows(sql_6_5, [])
		print_rows(rows, 'Orders (12 - 14)', counter=False)
		rows = select_rows(sql_6_6, [])
		print_rows(rows, 'Orders (17 - 19)', counter=False)
	elif choice == 7:
		rows = select_rows(sql_7, [])
		print_rows(rows, '\tplate\tcount')
	elif choice == 8:
		rows = select_rows(sql_8, [])
		print_rows(rows, '\tcustomer\tcount')
	elif choice == 9:
		rows = select_rows(sql_9, [])
		print_rows(rows, '\twid\tpname\tcount', counter=False)
	elif choice == 10:
		rows = select_rows(sql_10, [])
		print_rows(rows, '\tplate\tavg(cost)', counter=False)

def print_table(table_name, columns):
	rows = select_rows(sql_table, [('table_name', table_name)])
	header = ''
	for column in columns:
		header += '\t{}'.format(column)
	print_rows(rows, header)
		
def loop():
	print_menu()
	while True:
		choice = get_choice()
		process_choice(choice)

loop()
