import pymysql.cursors
from utils import print2

connection = pymysql.connect(host='localhost',
							 user='Alex',
							 password='',
							 db='db_project2',
							 charset='utf8mb4',
							 cursorclass=pymysql.cursors.DictCursor)

try:
	with connection.cursor() as cursor:

		guy = ["John Smith", "123 Street Road", "Charlottesville", "Virginia", "22903", "123-456-7890", "1234123412", "2017-09-01", "456"]
		sql = '''INSERT INTO customers (customer_name, street_address, city, state, zip, phone_number, cc_number, cc_exp_date, cc_security_code) VALUES ("{}", "{}", "{}", "{}", {}, "{}", {}, "{}", "{}")'''.format(guy[0], guy[1], guy[2], guy[3], guy[4], guy[5], guy[6], guy[7], guy[8])
		cursor.execute(sql)


		m = ["Harold Hill", "456 Address Drive", "Seattle", "Washington", "98765", "135-792-4680"]
		sql = '''INSERT INTO merchants (merchant_name, street_address, city, state, zip, phone_number) VALUES ("{}", "{}", "{}", "{}", {}, "{}")'''.format(m[0], m[1], m[2], m[3], m[4], m[5])
		cursor.execute(sql)


		d = ["Placeholder Developer", "135 Avenue Road", "New York", "New York", "13579", "456-789-0123"]
		sql = '''INSERT INTO developers (developer_name, street_address, city, state, zip, phone_number) VALUES ("{}", "{}", "{}", "{}", {}, "{}")'''.format(d[0], d[1], d[2], d[3], d[4], d[5])
		cursor.execute(sql)


		p = ["Placeholder Game", "Used", "This is a fun game where you do things", "45", "Action", "2017-04-01", "1", "1"]
		sql = '''INSERT INTO products (product_name, product_condition, product_description, price, genre, release_date, merchant_id, developer_id)  VALUES ("{}", "{}", "{}", "{}", "{}", "{}", {}, {})'''.format(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7])
		cursor.execute(sql)


		t = ["2017-08-23", 45, "Credit Card", 1, 1, 1]
		sql = '''INSERT INTO transactions (date_time, amount_paid, payment_method, customer_id, merchant_id, product_id) VALUES ("{}", {}, "{}", {}, {}, {})'''.format(t[0], t[1], t[2], t[3], t[4], t[5])
		cursor.execute(sql)


		r = ["This merchant is a cool guy", "2017-09-1", "2", "1", "1"]
		sql = '''INSERT INTO reviews (review_content, review_date_time, review_rating, customer_id, merchant_id) VALUES ("{}", "{}", {}, {}, {})'''.format(r[0], r[1], r[2], r[3], r[4])
		cursor.execute(sql)


		dpp = [1, 1]
		sql = '''INSERT INTO developer_produces_product (product_id, developer_id) VALUES ({}, {})'''.format(dpp[0], dpp[1])
		cursor.execute(sql)


		s = ["There is an issue with the thing", "2017-09-01", 1]
		sql = '''INSERT INTO support_tickets (ticket_content, ticket_date_time, customer_id) VALUES ("{}", "{}", {})'''.format(s[0], s[1], s[2])
		cursor.execute(sql)


	connection.commit()

finally: 
	connection.close()

