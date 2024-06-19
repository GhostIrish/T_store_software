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

        search_bar = ctk.CTkEntry(search_frame, width=600, placeholder_text='Product to search')
        search_bar.pack(side="left", padx=5)

        btn = ctk.CTkButton(search_frame, width=100, text='Print')
        btn.pack(side="left", padx=5)


        # Fazer a requisição e inserir os produtos no Textbox
        try:
            response = requests.get('http://localhost:5000/api/products')
            products = response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            

        self.tree_view_frame = ctk.CTkFrame(self, width=850, height=400)
        tree_view = ttk.Treeview(self.tree_view_frame, columns=('id', 'product', 'product_type', 'sizes', 'gender_product', 'brand', 'buying_price', 'selling_price', 'quantity'), show='headings')
        tree_view.column('id', minwidth=50, width=50)
        tree_view.column('product', minwidth=100, width=100)
        tree_view.column('product_type', minwidth=100, width=100)
        tree_view.column('sizes', minwidth=100, width=100)
        tree_view.column('gender_product', minwidth=100, width=100)
        tree_view.column('brand', minwidth=100, width=100)
        tree_view.column('buying_price', minwidth=100, width=100)
        tree_view.column('selling_price', minwidth=100, width=100)
        tree_view.column('quantity', minwidth=100, width=100)
        
        tree_view.heading('id', text='ID')
        tree_view.heading('product', text='PRODUCT')
        tree_view.heading('product_type', text='TYPE PRODUCT')
        tree_view.heading('sizes', text='SIZE')
        tree_view.heading('gender_product', text='GENDER')
        tree_view.heading('brand', text='BRAND')
        tree_view.heading('buying_price', text='PAY PRICE')
        tree_view.heading('selling_price', text='SELL PRICE')
        tree_view.heading('quantity', text='QUANTITY')
        
        for product in products:
            product_values = (
                product['id'], product['model_product'], product['product_type'], 
                product['size'], product['gender'], product['brand'], 
                product['buying_price'], product['selling_price'], product['quantity']
            )
            tree_view.insert("", "end", values=product_values)

        
        # for item in products:
        #     for key, product in item.items():
        #         product_values = (product['id'], product['product'], product['product_type'], product['sizes'], product['gender_product'], product['brand'], product['buying_price'], product['selling_price'])
        #         tree_view.insert("", "end", values=product_values)

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

        
        tree_view.pack(expand=True, fill='both')
        
        # Create and pack the frame for the Treeview, with fixed size
        self.tree_view_frame.pack()
        self.tree_view_frame.pack_propagate(False)
        
        def print_search_query(self):
            search_query = self.search_bar.get()
            print(f"Search query: {search_query}")