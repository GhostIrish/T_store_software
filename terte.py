import pymysql
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

try:
    connection = pymysql.connect(
        host=os.environ['MYSQL_HOST'],
        user=os.environ['MYSQL_USER'],
        password=os.environ['MYSQL_PASSWORD'],
        database=os.environ['MYSQL_DATABASE'],
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Conexão bem-sucedida!")
    
    with connection.cursor() as cursor:
        cursor.execute('SELECT id, brand_name FROM brands')
        results = cursor.fetchall()
        for row in results:
            print(row)
except pymysql.MySQLError as e:
    print(f"Erro na conexão: {e}")
finally:
    if connection:
        connection.close()
