import customtkinter as ctk
from tkinter import ttk

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
        
        
        
        # Sample data to be displayed in the Treeview
        list_names = list_names = [
    ['1', 'T-shirt', 'Clothing', 'M', 'Unisex', 'Nike', '$15.00', '$30.00'],
    ['2', 'Jeans', 'Clothing', 'L', 'Male', 'Levi\'s', '$25.00', '$50.00'],
    ['3', 'Dress', 'Clothing', 'S', 'Female', 'Adidas', '$20.00', '$40.00'],
    ['4', 'Shoes', 'Footwear', '42', 'Male', 'Puma', '$30.00', '$60.00'],
    ['5', 'Hat', 'Accessory', 'M', 'Unisex', 'Nike', '$10.00', '$20.00'],
    ['6', 'Skirt', 'Clothing', 'M', 'Female', 'Zara', '$18.00', '$36.00'],
    ['7', 'Jacket', 'Clothing', 'L', 'Unisex', 'H&M', '$35.00', '$70.00'],
    ['8', 'Sandals', 'Footwear', '38', 'Female', 'Gucci', '$22.00', '$44.00'],
    ['9', 'Socks', 'Accessory', 'L', 'Male', 'Puma', '$5.00', '$10.00'],
    ['10', 'Sweater', 'Clothing', 'M', 'Female', 'Adidas', '$28.00', '$56.00'],
    ['11', 'Scarf', 'Accessory', 'One Size', 'Unisex', 'Gucci', '$12.00', '$24.00'],
    ['12', 'Shorts', 'Clothing', 'M', 'Male', 'Nike', '$15.00', '$30.00'],
    ['13', 'Belt', 'Accessory', 'L', 'Male', 'Levi\'s', '$8.00', '$16.00'],
    ['14', 'Blouse', 'Clothing', 'S', 'Female', 'H&M', '$20.00', '$40.00'],
    ['15', 'Boots', 'Footwear', '40', 'Unisex', 'Dr. Martens', '$50.00', '$100.00']
]



        self.tree_view_frame = ctk.CTkFrame(self, width=800, height=400)
        tree_view = ttk.Treeview(self.tree_view_frame, columns=('id', 'product', 'product_type', 'sizes', 'gender_product', 'brand', 'buying_price', 'selling_price'), show='headings')
        tree_view.column('id', minwidth=100, width=100)
        tree_view.column('product', minwidth=100, width=100)
        tree_view.column('product_type', minwidth=100, width=100)
        tree_view.column('sizes', minwidth=100, width=100)
        tree_view.column('gender_product', minwidth=100, width=100)
        tree_view.column('brand', minwidth=100, width=100)
        tree_view.column('buying_price', minwidth=100, width=100)
        tree_view.column('selling_price', minwidth=100, width=100)
        
        tree_view.heading('id', text='ID')
        tree_view.heading('product', text='PRODUCT')
        tree_view.heading('product_type', text='TYPE PRODUCT')
        tree_view.heading('sizes', text='SIZE')
        tree_view.heading('gender_product', text='GENDER')
        tree_view.heading('brand', text='BRAND')
        tree_view.heading('buying_price', text='PAY PRICE')
        tree_view.heading('selling_price', text='SELL PRICE')
        
        for item in list_names:
                tree_view.insert("", "end", values=item)

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