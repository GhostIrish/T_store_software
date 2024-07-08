import customtkinter as ctk
import tkinter as tk

class UpdateProductFrame(ctk.CTkFrame):
    def __init__(self, master, product_data, **kwargs):
        super().__init__(master, **kwargs)
        self.product_data = product_data
        self.setup_ui()
        
    def setup_ui(self):
        label_update = ctk.CTkLabel(self, text="Update Product", text_color="white", font=("Arial", 20))
        label_update.pack(pady=20, padx=20)
        
        self.fields_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.fields_frame.pack(pady=10, padx=100, fill="both", expand=True)
        
        labels = ["Product", "Buying price", "Selling price", "Quantity", "Type", "Size", "Gender", "Brand"]
        self.entries = []

        for i, label in enumerate(labels):
            lbl = ctk.CTkLabel(self.fields_frame, text=label, text_color="white")
            lbl.grid(row=i, column=0, padx=10, pady=5, sticky="e")

            entry = ctk.CTkEntry(self.fields_frame, placeholder_text=f"Write {label.lower()}", width=400)
            entry.insert(0, self.product_data.get(label.lower().replace(' ', '_'), ''))
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="ew")
            self.entries.append(entry)
            
        self.save_button = ctk.CTkButton(self.fields_frame, text="Save", command=self.save_product)
        self.save_button.grid(row=len(labels), column=0, columnspan=2, pady=20, padx=20, sticky="ew")
        
    def save_product(self):
        # Implementar a lógica para salvar as alterações do produto na base de dados
        pass

class ProductTable(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.setup_ui()
        
    def setup_ui(self):
        self.search_bar = ctk.CTkEntry(self, placeholder_text="Product to search")
        self.search_bar.pack(pady=10, padx=10, fill="x")

        self.search_button = ctk.CTkButton(self, text="Search", command=self.search_product)
        self.search_button.pack(pady=10, padx=10)
        
        columns = ["ID", "PRODUCT", "PRODUCT TYPE", "SIZES", "GENDER PRODUCT", "BRAND", "BUYING PRICE", "SELLING PRICE", "QUANTITY"]
        self.table = tk.ttk.Treeview(self, columns=columns, show="headings")
        for col in columns:
            self.table.heading(col, text=col)
        self.table.pack(pady=20, padx=20, fill="both", expand=True)
        
        self.table.bind("<Double-1>", self.on_double_click)
        
        # Carregar dados na tabela (exemplo de dados)
        self.load_data()
        
    def load_data(self):
        # Dados de exemplo para a tabela
        data = [
            (1, "Air Max 2024", "T-shirt", "P", "Female", "Nike", 200, 300, 50),
            (2, "Jaqueta", "Jacket", "P", "Female", "Nike", 200, 300, 10),
            # Adicionar mais produtos aqui
        ]
        for item in data:
            self.table.insert("", "end", values=item)
            
    def on_double_click(self, event):
        item_id = self.table.focus()
        item = self.table.item(item_id)
        product_data = dict(zip(["id", "product", "product_type", "sizes", "gender_product", "brand", "buying_price", "selling_price", "quantity"], item["values"]))
        
        # Abrir o frame de atualização com os dados do produto
        update_frame = UpdateProductFrame(self.master, product_data)
        update_frame.pack(fill="both", expand=True)
        
    def search_product(self):
        # Implementar a lógica de busca do produto
        pass

# Exemplo de como usar
root = ctk.CTk()
root.geometry("800x600")

table_frame = ProductTable(root)
table_frame.pack(fill="both", expand=True)

root.mainloop()
