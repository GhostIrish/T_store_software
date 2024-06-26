import os
from flask import Flask, jsonify, request
import pymysql
import pymysql.cursors
from dotenv import load_dotenv


# load your .env file
load_dotenv()
app = Flask(__name__)


# making connection with my database
def get_connection():
    connection = pymysql.connect(
        host=os.environ['MYSQL_HOST'],
        user=os.environ['MYSQL_USER'],
        password=os.environ['MYSQL_PASSWORD'],
        database= os.environ['MYSQL_DATABASE'],
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,
        server_public_key=True,
        autocommit=True,
        connect_timeout=5
    )
    return connection

# create function to get infos from our database.
@app.route('/api/products', methods=['GET'])
def get_products():
    query = request.args.get('query', '')
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            query_sql = ''' 
                    SELECT p.id, p.model_product, pt.type_name as product_type, s.size_name as size, gp.gender, 
                    b.brand_name as brand, p.buying_price, p.selling_price, p.quantity 
                    FROM product p
                    JOIN product_types pt ON p.product_type = pt.id
                    JOIN sizes s ON p.size = s.id
                    JOIN gender_products gp ON p.gender_product = gp.id
                    JOIN brands b ON p.brand = b.id
                    '''
            if query:
                query_sql += "WHERE p.model_product LIKE %s"
                search_query = (query + '%',)
                cursor.execute(query_sql, search_query)
            else:
                cursor.execute(query_sql)
            products = cursor.fetchall()
            
    except pymysql.MySQLError as e:
            print(f"An error occurred: {e}")
            return jsonify({"error": "An error occurred while fetching products"}), 500
    finally:
        connection.close()
        
    return jsonify(products)

# create function to add dict into database
# this function recept the dict from any method, with me, the front send me infos in one dict, i send him to database.
@app.route('/api/add_product', methods=['POST'])
def add_product():
    connection = get_connection()
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

    except pymysql.MySQLError as error:
        return jsonify(error=str(error)), 500
    finally:
        connection.close()

# call specify datas for option menu in add_tab
@app.route('/api/types', methods=['GET'])
def get_product_types():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT id, type_name FROM product_types')
            types = cursor.fetchall()
        return jsonify(types)
    except pymysql.MySQLError as e:
        print(f'Error: {e}')
        return jsonify({'error': 'An error occurred while ftching product types'}), 500
    finally:
        connection.close()
    

@app.route('/api/sizes', methods=['GET'])
def get_sizes():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT id, size_name FROM sizes')
            sizes = cursor.fetchall()
        return jsonify(sizes)
    except pymysql.MySQLError as e:
        print(f'Error: {e}')
        return jsonify({'error': 'An error occurred while ftching product types'}), 500
    finally:
        connection.close()
    
@app.route('/api/genders', methods=['GET'])
def get_genders():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT id, gender FROM gender_products')
            genders = cursor.fetchall()
        return jsonify(genders)
    except pymysql.MySQLError as e:
        print(f'Error: {e}')
        return jsonify({'error': 'An error occurred while ftching product types'}), 500
    finally:
        connection.close()
    
@app.route('/api/brands', methods=['GET'])
def get_brands():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT id, brand_name FROM brands')
            brands = cursor.fetchall()
        return jsonify(brands)
    except pymysql.MySQLError as e:
        print(f'Error: {e}')
        return jsonify({'error': 'An error occurred while ftching product types'}), 500
    finally:
        connection.close()

# delete product from database using the id.
@app.route('/api/delete_product', methods=['DELETE'])
def delete_product():
    connection = get_connection()
    product_id = request.args.get('id')
    try:
        if product_id:
            with connection.cursor() as cursor:
                sql = 'DELETE FROM product WHERE id = %s'
                cursor.execute(sql, (product_id,))
            connection.commit()
            return jsonify(message=f'Product with id {product_id} deleted sucessfully')
        else:
            return jsonify(message='Product id is required to delete'), 400
        
    except pymysql.MySQLError as error:
        return jsonify(error=str(error)), 500
    
    finally:
        connection.close()
        

# it's for tests, just ignore
if __name__ == '__main__':
    app.run()
    get_products()