import customtkinter as ctk
import requests, threading

class AddProductFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.setup_ui()
        
    def setup_ui(self):
        self.setup_label()
        self.setup_field()
        self.setup_option_widget()
        self.setup_entrys()
        self.setup_textbox()
        self.setup_btn()
        self.fetch_option_data()
        
    def setup_label(self):
        label_add = ctk.CTkLabel(self, text="Add New Product", text_color="white", font=("Arial", 20))
        label_add.pack(pady=20, padx=20)
    
    def setup_field(self):
        self.fields_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.fields_frame.pack(pady=10, padx=100, fill="both", expand=True)   
    
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
        self.option_widgets = []
        titles = ["Type ", "Size ", "Gender ", "Brand "]
        self.option_endpoints = ["/api/types", "/api/sizes", "/api/genders", "/api/brands"]
        
        for i, title in enumerate(titles):
            lbl = ctk.CTkLabel(self.fields_frame, text=title, text_color="white")
            lbl.grid(row=i, column=3, padx=10, pady=5, sticky="e")
            
            option_var = ctk.StringVar(value=f"{title}")
            option_box = ctk.CTkOptionMenu(master=self.fields_frame, values=[], width=150,
                                           variable=option_var)
            option_box.grid(row=i, column=4, padx=10, pady=5, sticky="ew")
            self.option_widgets.append((option_var, option_box))
            
    def fetch_option_data(self):
        base_url = 'http://localhost:5000'
        def fetch_data(endpoint, option_box):
            try:
                response = requests.get(base_url + endpoint)
                response.raise_for_status()
                data = response.json()
                print(f"Data received from {endpoint}: {data}")
                values = []
                for item in data:
                    if 'type_name' in item:
                        values.append(item['type_name'])
                    elif 'size_name' in item:
                        values.append(item['size_name'])
                    elif 'gender' in item:
                        values.append(item['gender'])
                    elif 'brand_name' in item:
                        values.append(item['brand_name'])
                option_box.configure(values=values)

            except requests.RequestException as e:
                print(f"Error fetching data from {endpoint}: {e}")
        for endpoint, (_, option_box) in zip(self.option_endpoints, self.option_widgets):
            threading.Thread(target=fetch_data, args=(endpoint, option_box)).start()

    def setup_textbox(self):
        textbox = ctk.CTkTextbox(self.fields_frame, width=100, height=300, scrollbar_button_color="green", fg_color="black",
                                 border_width=1, border_color="green", border_spacing=20, activate_scrollbars=True, 
                                 scrollbar_button_hover_color='black')
        textbox.grid(row=5, column=0, columnspan=5 , padx=10, pady=20, sticky="ew")

    def setup_btn(self):
        send_button = ctk.CTkButton(self.fields_frame, text="Send")
        send_button.grid(row=6, column=0, columnspan=5, pady=5, padx=20, sticky="ew")
        
        cancel_button = ctk.CTkButton(self.fields_frame, text="Cancel", fg_color="#FF6961", hover_color="red")
        cancel_button.grid(row=7, column=0, columnspan=5, pady=10, padx=20, sticky="ew")
        