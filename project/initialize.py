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
		cursor.execute('''SET FOREIGN_KEY_CHECKS = 0''')
		cursor.execute('''DROP TABLE IF EXISTS customers''')
		cursor.execute('''CREATE TABLE customers (
			customer_id int AUTO_INCREMENT,
			customer_name varchar(100),
			street_address varchar(100),
			city varchar(50),
			state varchar(20),
			zip int,
			phone_number varchar(20),
			cc_number int,
			cc_exp_date datetime,
			cc_security_code varchar(10),

			PRIMARY KEY(customer_id)
			)''')

		cursor.execute('''DROP TABLE IF EXISTS merchants''')
		cursor.execute('''CREATE TABLE merchants (
			merchant_id int AUTO_INCREMENT,
			merchant_name varchar(100),
			street_address varchar(100),
			city varchar(50),
			state varchar(20),
			zip int,
			phone_number varchar(20),
			
			PRIMARY KEY(merchant_id)
			)''')

		cursor.execute('''DROP TABLE IF EXISTS developers''')
		cursor.execute('''CREATE TABLE developers (
			developer_id int AUTO_INCREMENT,
			developer_name varchar(100),
			street_address varchar(100),
			city varchar(50),
			state varchar(20),
			zip int,
			phone_number varchar(20),

			PRIMARY KEY(developer_id)
			)''')

		cursor.execute('''DROP TABLE IF EXISTS shopping_cart''')
		cursor.execute('''CREATE TABLE shopping_cart (
			customer_id int,
			product_id int,

			PRIMARY KEY(customer_id, product_id),
			FOREIGN KEY(customer_id) references customers(customer_id),
			FOREIGN KEY(product_id) references products(product_id)
			)''')

		cursor.execute('''DROP TABLE IF EXISTS products''')
		cursor.execute('''CREATE TABLE products (
			product_id int AUTO_INCREMENT,
			product_name varchar(100),
			product_condition varchar(100),
			product_description varchar(400),
			price decimal(20, 2),
			genre varchar(100),
			release_date datetime,
			merchant_id int,
			developer_id int,

			PRIMARY KEY(product_id),
			FOREIGN KEY(merchant_id) references merchants(merchant_id),
			FOREIGN KEY(developer_id) references developers(developer_id)
			)''')

		cursor.execute('''DROP TABLE IF EXISTS transactions''')
		cursor.execute('''CREATE TABLE transactions (
			transaction_id int AUTO_INCREMENT,
			date_time datetime,
			amount_paid decimal(20,2),
			payment_method varchar(20),
			customer_id int,
			merchant_id int,
			product_id int,

			PRIMARY KEY(transaction_id),
			FOREIGN KEY(customer_id) references customers(customer_id),
			FOREIGN KEY(merchant_id) references merchants(merchant_id),
			FOREIGN KEY(product_id) references products(product_id)
			)''')

		cursor.execute('''DROP TABLE IF EXISTS reviews''')
		cursor.execute('''CREATE TABLE reviews (
			review_id int AUTO_INCREMENT,
			review_content varchar(1000),
			review_date_time datetime,
			review_rating int,
			customer_id int,
			merchant_id int,

			PRIMARY KEY(review_id),
			FOREIGN KEY(customer_id) references customers(customer_id),
			FOREIGN KEY(merchant_id) references merchants(merchant_id)
			)''')

		cursor.execute('''DROP TABLE IF EXISTS developer_produces_product''')
		cursor.execute('''CREATE TABLE developer_produces_product (
			product_id int,
			developer_id int,

			PRIMARY KEY(product_id, developer_id),
			FOREIGN KEY(product_id) references products(product_id),
			FOREIGN KEY(developer_id) references developers(developer_id)
			)''')

		cursor.execute('''DROP TABLE IF EXISTS support_tickets''')
		cursor.execute('''CREATE TABLE support_tickets (
			ticket_id int AUTO_INCREMENT,
			ticket_content varchar(1000),
			ticket_date_time datetime,
			customer_id int,

			PRIMARY KEY(ticket_id),
			FOREIGN KEY(customer_id) references customers(customer_id)
			)''')

		cursor.execute('''SET FOREIGN_KEY_CHECKS = 1''')
		
	connection.commit()

finally: 
	connection.close()

