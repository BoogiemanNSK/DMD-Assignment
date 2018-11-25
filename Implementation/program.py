import sqlite3

conn = sqlite3.connect('db.db')
cur = conn.cursor()

def select_rows(sql, vals):
	if len(vals) > 0:
		cur.execute(sql)
	else:
		cur.execute(sql, vals)
	return cur.fetchall()
	
def print_menu():
	print('Hello, dear user. In this menu you can execute one of the specified queries.')
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
	elif choice > 10 or choice < 1:
		print('No such option available.')
	else:
		pass

def loop():
	print_menu()
	while True:
		choice = get_choice()
		process_choice(choice)
		
loop()
