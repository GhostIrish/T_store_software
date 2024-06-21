import customtkinter as ctk
from tkinter import ttk
import requests

class SearchProductFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.setup_ui()

    def setup_ui(self):
        self.setup_labels()
        self.setup_search_bar()
        self.setup_treeview()
        self.setup_treeview_styles()

    def setup_labels(self):
        label_search = ctk.CTkLabel(self, text="Search Product", text_color="white", font=("Arial", 20))
        label_search.pack(pady=20, padx=20)

    def setup_search_bar(self):
        search_frame = ctk.CTkFrame(self, fg_color="transparent")
        search_frame.pack(pady=10)

        self.search_bar = ctk.CTkEntry(search_frame, width=600, placeholder_text='Product to search')
        self.search_bar.pack(side="left", padx=5)

        btn = ctk.CTkButton(search_frame, width=100, text='Search', command=self.search_products)
        btn.pack(side="left", padx=5)

    def setup_treeview(self):
        self.tree_view_frame = ctk.CTkFrame(self, width=850, height=400)
        self.tree_view = ttk.Treeview(
            self.tree_view_frame,
            columns=('id', 'product', 'product_type', 'sizes', 'gender_product', 'brand', 'buying_price', 'selling_price', 'quantity'),
            show='headings'
        )
        
        for col in self.tree_view["columns"]:
            self.tree_view.heading(col, text=col.replace("_", " ").upper())
            self.tree_view.column(col, minwidth=100, width=100)

        self.tree_view.column('id', minwidth=50, width=50)
        
        self.tree_view.pack(expand=True, fill='both')
        self.tree_view_frame.pack()
        self.tree_view_frame.pack_propagate(False)

    def setup_treeview_styles(self):
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

    def search_products(self):
        texto = self.search_bar.get()
        query = texto.capitalize()
        
        if query:
            url = f'http://localhost:5000/api/products?query={query}'
        else :
            url = 'http://localhost:5000/api/products'
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            products = response.json()
            print(products)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            self.display_error("An error occurred while fetching products. Please try again later.")
            return

        self.update_treeview(products)

    def update_treeview(self, products):
        for item in self.tree_view.get_children():
            self.tree_view.delete(item)

        for product in products:
            product_values = (
                product['id'], product['model_product'], product['product_type'],
                product['size'], product['gender'], product['brand'],
                product['buying_price'], product['selling_price'], product['quantity']
            )
            self.tree_view.insert("", "end", values=product_values)
    
    def display_error(self, message):
        error_label = ctk.CTkLabel(self, text=message, text_color="red", font=("Arial", 14))
        error_label.pack(pady=10)
