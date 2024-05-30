import pymysql
from dotenv import load_dotenv
import pymysql.cursors
import os

# load your .env file
load_dotenv()

# define table_name in db
TABLE_NAME = 'product'

# making connection with my database
connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database= os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    cursorclass=pymysql.cursors.SSDictCursor
)

# all of this is for create a database and add all rules i need to this project.
with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS product_types ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'type_name VARCHAR(50) NOT NULL, '
            'PRIMARY KEY (id)'
            ')'
        )
        
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS sizes ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'size_name VARCHAR(50) NOT NULL, '
            'PRIMARY KEY (id)'
            ')'
        )
        
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS gender_products ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'gender VARCHAR(50) NOT NULL, '
            'PRIMARY KEY (id)'
            ')'
        )
        
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS brands ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'brand_name VARCHAR(50) NOT NULL, '
            'PRIMARY KEY (id)'
            ')'
        )
        
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'model_product VARCHAR(50) NOT NULL, '
            'product_type VARCHAR(50) NOT NULL, '
            'size VARCHAR(5) NOT NULL, '
            'gender_product VARCHAR(50) NOT NULL, '
            'brand VARCHAR(50) NOT NULL, '
            'buying_price INT NOT NULL, '
            'selling_price INT NOT NULL, '
            'quantity INT NOT NULL, '
            'PRIMARY KEY (id)'
            ')'
        )
        
        #insert into support tables - :)
        # cursor.executemany(
        #     'INSERT INTO product_types (type_name) VALUES (%s)',
        #     [('T-shirt',), ('Pants',), ('Jacket',)]
        # )
        
        
        # cursor.executemany(
        #     'INSERT INTO sizes (size_name) VALUES (%s)',
        #     [('PP'), ('P'), ('M'), ('G'), ('GG'), ('XXG')]
        # )
        
        # cursor.executemany(
        #     'INSERT INTO gender_products (gender) VALUES (%s)',
        #     [('Female'), ('Male',), ('Child',)]
        # )
        
        # cursor.executemany(
        #     'INSERT INTO brands (brand_name) VALUES (%s)',
        #     [('Nike'), ('Adidas'), ('Calvin Klein'), ('Gucci'), ]
        # )
        
        
        # -------------------------------------------------------------------------------------------------------------------------
       
        # add_foreign key -
        # cursor.execute(
        #     f'ALTER TABLE {TABLE_NAME} ADD CONSTRAINT ct_type_id FOREIGN KEY (product_type) REFERENCES product_types(id) '
        # )
        
        # cursor.execute(
        #     f'ALTER TABLE {TABLE_NAME} ADD CONSTRAINT size_ct_id FOREIGN KEY (size) REFERENCES sizes(id) '
        # )
        
        # cursor.execute(
        #     f'ALTER TABLE {TABLE_NAME} ADD CONSTRAINT gender_ct_id FOREIGN KEY (gender_product) REFERENCES gender_products(id) '
        # )
        
        # cursor.execute(
        #     f'ALTER TABLE {TABLE_NAME} ADD CONSTRAINT brand_ct_id FOREIGN KEY (brand) REFERENCES brands(id) '
        # )


        # -------------------------------------------------------------------------------------------------------------------------
        # insert example -  :)
        
        # cursor.execute(
        #     f'INSERT INTO {TABLE_NAME} (model_product, product_type, size, gender_product, brand, buying_price, selling_price) '
        #     'VALUES (%s, %s, %s, %s, %s, %s, %s)',
        #     ('Jaqueta', 1, 2, 1, 1, 200, 300)
        # )
        
    connection.commit()
    
    