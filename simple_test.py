import os
import requests


# this part is a playground, where i test the connection and API functions before i create the real GUI for my project
# i don't make the update method yet, because i'm waiting to finish development my GUI. In this menu, create a way to make this possible,
# it's a waste of time.

running = True

def show_products(response_):
    print('Products found: ')
    print()
    if response_.status_code == 200:
        products = response_.json() 
        for dicionary in products:  
            for key, product in dicionary.items():
                print(f'{key}: {product}')
            print('----------------------------------')
    else:
            print('Error fetching products.')
            
while running:
    menu = '''
[1] Add cloth
[2] Search
[3] Delete Product
[4] Exit
    '''
    print(menu)
    # the inputs returns a dict 'product'
    product = {}
    option = str(input('Option: ')).strip()
    print()
    if option == '1':
        product["model_product"] = str(input('Product: ')).strip().capitalize()
        product["product_type"] = int(input('Product Type: '))
        product["size"] = int(input('Size: '))
        product["gender_product"] = int(input('Gender: '))
        product["brand"] = int(input('Brand: '))
        product["buying_price"] = int(input('Price you pay: '))
        product["selling_price"] = int(input('Price you sell: '))
        product["quantity"] = int(input('Product Quantity: '))
        print()
        
        print(f'You really want to add this cloth -> {product}')
        # after create, if you really want to put the dict in db, write Y.
        confirm = str(input('Y/N: ')).strip().upper()
        if confirm == 'Y':
            response = requests.post('http://localhost:5000/api/add_product', json=product)
            if response.status_code == 201:
                print('The product has been uploaded sucessfully!')
            else:
                print('Error to upload product.')
                
        elif confirm == 'N':
            print('Ok, returning to menu. . .')
            os.system('cls')



    if option == '2':
        # if you choose the second option, you want to show db infos.
        choice = str(input('Show all or specify products[All/Spe]: ')).strip().capitalize() 
        print()
        if choice == 'All':
            response_ = requests.get(f'http://localhost:5000/api/products')
        elif choice == 'Spe':
            search = str(input('Product name to search: ')).strip().capitalize()
            response_ = requests.get(f'http://localhost:5000/api/products?model_product={search}')
            
        show_products(response_)

        
        

    
    if option == '3':
        # it's to test delete in project, i did not leave the user delete all database in this case.
        response_ = requests.get(f'http://localhost:5000/api/products')
        show_products(response_)
        
        print()
        print()
        id_product = int(input('Product to delete[id]: '))
        response_2 = requests.get(f'http://localhost:5000/api/products?id={id_product}')
        show_products(response_2)
        print()
        last_chance = str(input('You really want to delete this product?[Y/N]')).strip().upper()
        
        if last_chance == 'Y':
            response = requests.delete(f'http://localhost:5000/api/delete_product?id={id_product}')
            print()
            print('Product deleted sucessfully!')
            
        elif last_chance == 'N':
            print('Ok, returning to menu. . .')
           
        else:
            print('Error.')
        
        
    if option == '4':
        running = False
        




