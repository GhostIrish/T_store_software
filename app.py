import os
from flask import Flask, jsonify, request
import pymysql
import pymysql.cursors
from dotenv import load_dotenv

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
    cursorclass=pymysql.cursors.SSDictCursor
)

@app.route('/api/products', methods=['GET'])
def get_products():
    model_product = request.args.get('model_product')
    id = request.args.get('id')
    
    query = 'SELECT * FROM product'
    
    if model_product:
        query += ' WHERE model_product = %s'
    if id:
        query += ' WHERE id = %s'
        
    with connection.cursor() as cursor:
        if model_product:
            cursor.execute(query, (model_product,))
            
        elif id:
            cursor.execute(query, (id,))
            
        else:
            cursor.execute(query)
            
        products = cursor.fetchall()
        
    return jsonify(products)



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
        
if __name__ == '__main__':
    app.run()
    get_products()