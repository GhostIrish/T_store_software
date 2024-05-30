import pymysql
from dotenv import load_dotenv
import pymysql.cursors
import os

# load your .env file
load_dotenv()

TABLE_NAME = 'product'

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database= os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    cursorclass=pymysql.cursors.SSDictCursor
)

with connection:
    with connection.cursor() as cursor:
        date = (
            f'SELECT p.id, p.model_product, ptype.type_name AS product_type, '
            f's.size_name AS size, genderp.gender AS gender_product, '
            f'b.brand_name AS brand, p.buying_price, p.selling_price, p.quantity '
            f'FROM {TABLE_NAME} p '
            f'INNER JOIN product_types ptype ON p.product_type = ptype.id '
            f'INNER JOIN sizes s ON p.size = s.id '
            f'INNER JOIN gender_products genderp ON p.gender_product = genderp.id '
            f'INNER JOIN brands b ON p.brand = b.id' 
            ) 
        
        cursor.execute(date)
    
        results = cursor.fetchall()
        
        for row in results:
            print(row)
       
        