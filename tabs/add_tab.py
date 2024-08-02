import customtkinter as ctk
import requests, threading

class AddProductFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.setup_ui()

    def setup_ui(self):
        # Sets up the entire user interface for the Add Product frame
        self.setup_label()
        self.setup_field()
        self.setup_option_widget()
        self.setup_entries()
        self.setup_textbox()
        self.setup_buttons()
        self.fetch_option_data()

    def setup_label(self):
        # Creates and positions the main label
        label_add = ctk.CTkLabel(self, text="Add New Product", text_color="white", font=("Arial", 20))
        label_add.pack(pady=20, padx=20)

    def setup_field(self):
        # Creates a frame for input fields
        self.fields_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.fields_frame.pack(pady=10, padx=100, fill="both", expand=True)

    def setup_entries(self):
        # Defines labels for input fields
        labels = ["Product ", "Buying price ", "Selling price ", "Quantity "]
        self.entries = []
        self.entry_labels = labels

        # Creates and positions the input fields
        for i, label in enumerate(labels):
            lbl = ctk.CTkLabel(self.fields_frame, text=label, text_color="white")
            lbl.grid(row=i, column=0, padx=10, pady=5, sticky="e")

            entry = ctk.CTkEntry(self.fields_frame, placeholder_text=f"Write {label.lower()}", width=400)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="ew")
            self.entries.append(entry)

        # Adds an empty column for spacing
        self.fields_frame.grid_columnconfigure(2, minsize=50)  # Adjust minsize as needed

    def setup_option_widget(self):
        # Creates dropdown menus for selecting options
        self.option_widgets = []
        titles = ["Type ", "Size ", "Gender ", "Brand "]
        self.option_endpoints = ["/api/types", "/api/sizes", "/api/genders", "/api/brands"]
        self.opt_labels = titles

        # Creates and positions the dropdown menus
        for i, title in enumerate(titles):
            lbl = ctk.CTkLabel(self.fields_frame, text=title, text_color="white")
            lbl.grid(row=i, column=3, padx=10, pady=5, sticky="e")

            option_var = ctk.StringVar(value=f"{title}")
            option_box = ctk.CTkOptionMenu(master=self.fields_frame, values=[], width=150, variable=option_var)
            option_box.grid(row=i, column=4, padx=10, pady=5, sticky="ew")
            self.option_widgets.append((option_var, option_box))

    def fetch_option_data(self):
        # Fetches option data for dropdown menus from the API
        base_url = 'http://127.0.0.1:5000'

        def fetch_data(endpoint, option_box):
            try:
                response = requests.get(base_url + endpoint)
                response.raise_for_status()
                data = response.json()
                print(f"Data received from {endpoint}: {data}")

                # Extracts names from the response
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

        # Starts data fetching for each dropdown menu in a separate thread
        for endpoint, (_, option_box) in zip(self.option_endpoints, self.option_widgets):
            threading.Thread(target=fetch_data, args=(endpoint, option_box)).start()

    def setup_textbox(self):
        # Creates and configures the textbox to display product details
        self.textbox = ctk.CTkTextbox(self.fields_frame, width=100, height=250, scrollbar_button_color="green", fg_color="black",
                                      border_width=1, border_color="green", border_spacing=20, activate_scrollbars=True,
                                      scrollbar_button_hover_color='black', state="disabled")
        self.textbox.grid(row=5, column=0, columnspan=5, padx=10, pady=20, sticky="ew")

    def insert_into_box(self, text):
        # Inserts text into the textbox
        self.textbox.configure(state="normal")  # Enable text insertion
        self.textbox.insert("end", text + "\n")
        self.textbox.configure(state="disabled")  # Disable after insertion

    def clear_textbox(self):
        # Clears the content of the textbox
        self.textbox.configure(state="normal")  # Enable text clearing
        self.textbox.delete("1.0", "end")
        self.textbox.configure(state="disabled")  # Disable after clearing

    def collect_data(self):
        # Clears the textbox and collects new data
        self.clear_textbox()
        data = """
You really want to insert this product in database?
Press the new button if yes or "Cancel" to try again. \n \n"""
        # Gets data from the entries
        for label, entry in zip(self.entry_labels, self.entries):
            data += f'{label}: {entry.get()}\n'

        # Gets data from the dropdown menus
        for label, (option_var, _) in zip(self.opt_labels, self.option_widgets):
            data += f'{label}: {option_var.get()}\n'

        # Inserts the data into the textbox
        self.insert_into_box(data)

    def send_db_data(self):
        # Sends the data to the database in a separate thread to avoid blocking the UI
        threading.Thread(target=self._send_db_data).start()

    def _send_db_data(self):
        self.show_loading_screen()

        base_url = 'http://127.0.0.1:5000'
        print("send_db_data called")

        total_steps = 10
        current_step = 0

        def update_progress(step_increment=1):
            nonlocal current_step
            current_step += step_increment
            self.loading_screen.after(0, lambda: self.progress_var.set((current_step / total_steps)))

        update_progress(1)

        # Function to get ID from name
        def get_id_from_name(endpoint, name):
            print(f"Fetching ID for {name} from {endpoint}")
            try:
                response = requests.get(base_url + endpoint)
                response.raise_for_status()
                data = response.json()
                update_progress(2)
                for item in data:
                    if 'type_name' in item and item['type_name'] == name:
                        return item['id']
                    elif 'size_name' in item and item['size_name'] == name:
                        return item['id']
                    elif 'gender' in item and item['gender'] == name:
                        return item['id']
                    elif 'brand_name' in item and item['brand_name'] == name:
                        return item['id']
                return None
            except requests.RequestException as e:
                print(f"Error fetching data from {endpoint}: {e}")
                return None

        # Collects data and maps names to IDs
        product_data = {
            'model_product': self.entries[0].get(),
            'buying_price': self.entries[1].get(),
            'selling_price': self.entries[2].get(),
            'quantity': self.entries[3].get(),
            'product_type': get_id_from_name('/api/types', self.option_widgets[0][0].get()),
            'size': get_id_from_name('/api/sizes', self.option_widgets[1][0].get()),
            'gender_product': get_id_from_name('/api/genders', self.option_widgets[2][0].get()),
            'brand': get_id_from_name('/api/brands', self.option_widgets[3][0].get())
        }
        update_progress(2)

        # Sends the data to the database
        try:
            response = requests.post(base_url + '/api/add_product', json=product_data)
            response.raise_for_status()
            print(f"Data sent to database: {response.json()}")
            self.update_loading_screen("Data sent successfully!", True)
        except requests.RequestException as e:
            print(f"Error sending data to the database: {e}")
            self.update_loading_screen("Error sending data.", False)
        
        update_progress(total_steps - current_step)

    def update_loading_screen(self, message, success):
        # Uses the `after` method to ensure updates are made on the main thread
        self.loading_screen.after(0, lambda: self.loading_screen_message.set(message))
        if success:
            self.loading_screen.after(0, lambda: self.progress_var.set(1.0))
            self.loading_screen.after(0, lambda: self.loading_screen_button.configure(state="normal"))

    def show_loading_screen(self):
        # Creates a loading pop-up window
        self.loading_screen = ctk.CTkToplevel(self)
        self.loading_screen.title("Loading")

        # Centers the pop-up window
        self.loading_screen.geometry("300x200+{}+{}".format(
            self.loading_screen.winfo_screenwidth() // 2 - 150,
            self.loading_screen.winfo_screenheight() // 2 - 100
        ))
        self.loading_screen.transient(self)
        self.loading_screen.grab_set()
        self.loading_screen.resizable(False, False)

        # Message and button for the loading window
        self.loading_screen_message = ctk.StringVar(value="Sending data to the database...")
        message_label = ctk.CTkLabel(self.loading_screen, textvariable=self.loading_screen_message)
        message_label.pack(pady=20)
        
        self.progress_var = ctk.DoubleVar(value=0)
        self.progress_bar = ctk.CTkProgressBar(self.loading_screen, variable=self.progress_var)
        self.progress_bar.pack(pady=10)
        self.progress_bar.set(0)

        self.loading_screen_button = ctk.CTkButton(self.loading_screen, text="OK", command=self.close_loading_screen, state="disabled")
        self.loading_screen_button.pack(pady=20)

        # Updates the loading window to ensure it is displayed before sending data
        self.loading_screen.update()

    def close_loading_screen(self):
        # Closes the loading window and clears the entries
        self.loading_screen.destroy()
        for entry in self.entries:
            entry.delete(0, "end")
        self.clear_textbox()

    def show_send_btn(self):
        # Collects data and displays the send button
        self.collect_data()
        send_button = ctk.CTkButton(self.fields_frame, text="Send to database", command=self.send_db_data, fg_color="#2A6CB7", hover_color="blue")
        send_button.grid(row=8, column=0, columnspan=5, pady=5, padx=20, sticky="ew")

    def setup_buttons(self):
        # Creates preview and cancel buttons
        preview_button = ctk.CTkButton(self.fields_frame, text="Preview", command=self.show_send_btn)
        preview_button.grid(row=6, column=0, columnspan=5, pady=5, padx=20, sticky="ew")

        cancel_button = ctk.CTkButton(self.fields_frame, text="Cancel", command=self.clear_textbox, fg_color="#FF6961", hover_color="red")
        cancel_button.grid(row=7, column=0, columnspan=5, pady=10, padx=20, sticky="ew")
