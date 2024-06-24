import customtkinter as ctk

class AddProductFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.setup_ui()
        
    def setup_ui(self):
        self.setup_label()
        self.setup_field()
        self.setup_option_widget()
        self.setup_entrys()
        self.setup_btn()
        
    def setup_label(self):
        label_add = ctk.CTkLabel(self, text="Add New Product", text_color="white", font=("Arial", 20))
        label_add.pack(pady=20, padx=20)
    
    def setup_field(self):
        self.fields_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.fields_frame.pack(pady=20, padx=100, fill="both", expand=True)   
    
    def setup_entrys(self):
        labels = ["Product ", "Buying price ", "Selling price ", "Quantity "]
        self.entries = []

        for i, label in enumerate(labels):
            lbl = ctk.CTkLabel(self.fields_frame, text=label, text_color="white")
            lbl.grid(row=i, column=0, padx=10, pady=5, sticky="e")

            entry = ctk.CTkEntry(self.fields_frame, placeholder_text=f"Write {label.lower()}", width=400)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="ew")
            self.entries.append(entry)
            
                    # Adding an empty column for spacing
            self.fields_frame.grid_columnconfigure(2, minsize=50)  # Adjust the minsize as needed
        
    def setup_option_widget(self):
        titles = ["Type ", "Size ", "Gender ", "Brand "]
        for i, title in enumerate(titles):
            lbl = ctk.CTkLabel(self.fields_frame, text=title, text_color="white")
            lbl.grid(row=i, column=3, padx=10, pady=5, sticky="e")
            
            option_var = ctk.StringVar(value=f"{title}")
            option_box = ctk.CTkOptionMenu(master=self.fields_frame, values=["teste1", "teste2"], width=150,
                                           variable=option_var)
            option_box.grid(row=i, column=4, padx=10, pady=5, sticky="ew")

    def setup_btn(self):
        send_button = ctk.CTkButton(self, text="Send")
        send_button.pack(pady=20, padx=20)

