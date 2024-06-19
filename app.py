import os
from flask import Flask, jsonify, request
import pymysql
import pymysql.cursors
from dotenv import load_dotenv
import requests

# load your .env file
load_dotenv()
app = Flask(__name__)


# making connection with my database
connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database= os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    cursorclass=pymysql.cursors.SSDictCursor,
    server_public_key=True,
    ssl=False
)

# create function to get infos from our database.
@app.route('/api/products', methods=['GET'])
def get_products():
    #model_product = request.args.get('model_product')
    #id = request.args.get('id')
    try:
        with connection.cursor() as cursor:
            query = ''' 
                    SELECT p.id, p.model_product, pt.type_name as product_type, s.size_name as size, gp.gender, 
                    b.brand_name as brand, p.buying_price, p.selling_price, p.quantity 
                    FROM product p
                    JOIN product_types pt ON p.id = pt.id
                    JOIN sizes s ON p.id = s.id
                    JOIN gender_products gp ON p.id = gp.id
                    JOIN brands b ON p.id = b.id
                    '''
            cursor.execute(query)
            products = cursor.fetchall()
            
    except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
    
    return jsonify(products)
    
    # if model_product:
    #     query += ' WHERE model_product = %s'
    # if id:
    #     query += ' WHERE id = %s'
        
    # with connection.cursor() as cursor:
    #     if model_product:
    #         cursor.execute(query, (model_product,))
            
    #     elif id:
    #         cursor.execute(query, (id,))
            
    #     else:
    #         cursor.execute(query)
            
    #     products = cursor.fetchall()
        
    #return jsonify(products)


# create function to add dict into database
# this function recept the dict from any method, with me, the front send me infos in one dict, i send him to database.
@app.route('/api/add_product', methods=['POST'])
def add_product():
    try:
        new_product = request.json
        
        with connection.cursor() as cursor:
            sql = '''
            INSERT INTO product (model_product, product_type, size, gender_product, brand, buying_price, selling_price, quantity)
            VALUES (%(model_product)s, %(product_type)s, %(size)s, %(gender_product)s, %(brand)s, %(buying_price)s, %(selling_price)s, %(quantity)s)
            '''
            cursor.execute(sql, new_product)
        connection.commit()
            
        return jsonify(message='Product registered successfully', item=new_product), 201

    except Exception as error:
        return jsonify(error=str(error)), 500



# delete product from database using the id.
@app.route('/api/delete_product', methods=['DELETE'])
def delete_product():
    product_id = request.args.get('id')
    
    if product_id:
        with connection.cursor() as cursor:
            sql = 'DELETE FROM product WHERE id = %s'
            cursor.execute(sql, (product_id,))
        connection.commit()
        return jsonify(message=f'Product with id {product_id} deleted sucessfully')
    else:
        return jsonify(message='Product id is required to delete'), 400
        

# it's for tests, just ignore
if __name__ == '__main__':
    app.run()
    get_products()