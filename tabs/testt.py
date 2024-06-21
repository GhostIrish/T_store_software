import customtkinter as ctk
from tkinter import ttk
import requests

class SearchProductFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        label_search = ctk.CTkLabel(self, text="Search Product", text_color="white", font=("Arial", 20))
        label_search.pack(pady=20, padx=20)

        search_frame = ctk.CTkFrame(self, fg_color="transparent")
        search_frame.pack(pady=10)

        self.search_bar = ctk.CTkEntry(search_frame, width=600, placeholder_text='Product to search')
        self.search_bar.pack(side="left", padx=5)

        btn = ctk.CTkButton(search_frame, width=100, text='Search', command=self.search_products)
        btn.pack(side="left", padx=5)

        self.tree_view_frame = ctk.CTkFrame(self, width=850, height=400)
        self.tree_view = ttk.Treeview(self.tree_view_frame, columns=('id', 'product', 'product_type', 'sizes', 'gender_product', 'brand', 'buying_price', 'selling_price', 'quantity'), show='headings')
        self.tree_view.column('id', minwidth=50, width=50)
        self.tree_view.column('product', minwidth=100, width=100)
        self.tree_view.column('product_type', minwidth=100, width=100)
        self.tree_view.column('sizes', minwidth=100, width=100)
        self.tree_view.column('gender_product', minwidth=100, width=100)
        self.tree_view.column('brand', minwidth=100, width=100)
        self.tree_view.column('buying_price', minwidth=100, width=100)
        self.tree_view.column('selling_price', minwidth=100, width=100)
        self.tree_view.column('quantity', minwidth=100, width=100)
        
        self.tree_view.heading('id', text='ID')
        self.tree_view.heading('product', text='PRODUCT')
        self.tree_view.heading('product_type', text='TYPE PRODUCT')
        self.tree_view.heading('sizes', text='SIZE')
        self.tree_view.heading('gender_product', text='GENDER')
        self.tree_view.heading('brand', text='BRAND')
        self.tree_view.heading('buying_price', text='PAY PRICE')
        self.tree_view.heading('selling_price', text='SELL PRICE')
        self.tree_view.heading('quantity', text='QUANTITY')

        style = ttk.Style()
    
        style.theme_use("default")

        style.configure("Treeview",
                        background="black",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="black",
                        borderwidth=0)
        style.map('Treeview', background=[('selected', '#006400')])

        style.configure("Treeview.Heading",
                        background="#565b5e",
                        foreground="white",
                        relief="flat")
        style.map("Treeview.Heading",
                    background=[('active', 'green')])

        
        self.tree_view.pack(expand=True, fill='both')
        
        # Create and pack the frame for the Treeview, with fixed size
        self.tree_view_frame.pack()
        self.tree_view_frame.pack_propagate(False)
        
        self.search_products()
    
    def search_products(self):
        global tree_view
        query = self.search_bar.get()
        # Fazer a requisição e inserir os produtos no Textbox
        try:
            if query:
                url = f'http://localhost:5000/api/products?query={query}'
            else:
                url = 'http://localhost:5000/api/products'
            
            reponse = requests.get(url)
            products = response.json()
            print(products)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        
        for item in self.tree_view.get_children():
            self.tree_view.delete(item)
        
        for product in products:
            products = response.json()
            product_values = (
                product['id'], product['model_product'], product['product_type'], 
                product['size'], product['gender'], product['brand'], 
                product['buying_price'], product['selling_price'], product['quantity']
            )
            self.tree_view.insert("", "end", values=product_values)

        
        
        # def print_search_query(self):
        #     search_query = self.search_bar.get()
        #     print(f"Search query: {search_query}")
        
        
        
      