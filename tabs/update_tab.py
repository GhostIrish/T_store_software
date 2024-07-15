import customtkinter as ctk
import requests, threading

class UpdateProductFrame(ctk.CTkFrame):
    def __init__(self, master, product_data, **kwargs):
        super().__init__(master, **kwargs)
        self.product_data = product_data
        self.setup_ui()

    def setup_ui(self):
        self.setup_label()
        self.setup_field()
        self.setup_option_widget()
        self.setup_entries()
        self.fill_entries_with_product_data()
        self.setup_textbox()
        self.setup_buttons()
        self.fetch_option_data()

    def setup_label(self):
        # Cria e posiciona o rótulo principal
        label_add = ctk.CTkLabel(self, text="Update Product", text_color="white", font=("Arial", 20))
        label_add.pack(pady=20, padx=20)

    def setup_field(self):
        # Cria um frame para os campos de entrada
        self.fields_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.fields_frame.pack(pady=10, padx=100, fill="both", expand=True)

    def setup_entries(self):
        # Define rótulos para os campos de entrada
        labels = ["Product ", "Buying price ", "Selling price ", "Quantity "]
        self.entries = []
        self.entry_labels = labels

        # Cria e posiciona os campos de entrada
        for i, label in enumerate(labels):
            lbl = ctk.CTkLabel(self.fields_frame, text=label, text_color="white")
            lbl.grid(row=i, column=0, padx=10, pady=5, sticky="e")

            entry = ctk.CTkEntry(self.fields_frame, placeholder_text=f"Write {label.lower()}", width=400)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="ew")
            self.entries.append(entry)

        # Adiciona uma coluna vazia para espaçamento
        self.fields_frame.grid_columnconfigure(2, minsize=50)  # Ajuste o minsize conforme necessário

    def fill_entries_with_product_data(self):
        # Preenche os campos de entrada com os dados do produto
        self.entries[0].insert(0, self.product_data.get("product", ""))
        self.entries[1].insert(0, self.product_data.get("buying_price", ""))
        self.entries[2].insert(0, self.product_data.get("selling_price", ""))
        self.entries[3].insert(0, self.product_data.get("quantity", ""))
        self.option_widgets[0][0].set(self.product_data.get("product_type", ""))
        self.option_widgets[1][0].set(self.product_data.get("sizes", ""))
        self.option_widgets[2][0].set(self.product_data.get("gender_product", ""))
        self.option_widgets[3][0].set(self.product_data.get("brand", ""))
        #self.collect_data()

    def setup_option_widget(self):
        # Cria menus suspensos para selecionar opções
        self.option_widgets = []
        titles = ["Type ", "Size ", "Gender ", "Brand "]
        self.option_endpoints = ["/api/types", "/api/sizes", "/api/genders", "/api/brands"]
        self.opt_labels = titles

        # Cria e posiciona os menus suspensos
        for i, title in enumerate(titles):
            lbl = ctk.CTkLabel(self.fields_frame, text=title, text_color="white")
            lbl.grid(row=i, column=3, padx=10, pady=5, sticky="e")

            option_var = ctk.StringVar(value=f"{title}")
            option_box = ctk.CTkOptionMenu(master=self.fields_frame, values=[], width=150, variable=option_var)
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

                # Extrai os nomes da resposta
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

        # Inicia a busca de dados para cada menu suspenso em um thread separado
        for endpoint, (_, option_box) in zip(self.option_endpoints, self.option_widgets):
            threading.Thread(target=fetch_data, args=(endpoint, option_box)).start()

    def setup_textbox(self):
        # Cria e configura a caixa de texto para exibir os detalhes do produto
        self.textbox = ctk.CTkTextbox(self.fields_frame, width=100, height=250, scrollbar_button_color="green", fg_color="black",
                                      border_width=1, border_color="green", border_spacing=20, activate_scrollbars=True,
                                      scrollbar_button_hover_color='black', state="disabled")
        self.textbox.grid(row=5, column=0, columnspan=5, padx=10, pady=20, sticky="ew")

    def insert_into_box(self, text):
        # Insere texto na caixa de texto
        self.textbox.configure(state="normal")  # Permitir a inserção de texto
        self.textbox.insert("end", text + "\n")
        self.textbox.configure(state="disabled")  # Desativar novamente após a inserção

    def clear_textbox(self):
        # Limpa o conteúdo da caixa de texto
        self.textbox.configure(state="normal")  # Permitir a limpeza de texto
        self.textbox.delete("1.0", "end")
        self.textbox.configure(state="disabled")  # Desativar novamente após a limpeza

    def collect_data(self):
        # Limpa a caixa de texto antes de inserir novos dados
        self.clear_textbox()
        data = """
You really want to insert this product in database?
Press the new button if yes or "Cancel" to try again. \n \n"""
        # Obtém os dados das entradas
        for label, entry in zip(self.entry_labels, self.entries):
            data += f'{label}: {entry.get()}\n'

        # Obtém os dados dos menus suspensos
        for label, (option_var, _) in zip(self.opt_labels, self.option_widgets):
            data += f'{label}: {option_var.get()}\n'

        # Insere os dados na caixa de texto
        self.insert_into_box(data)

    def _send_db_data(self):
        base_url = 'http://localhost:5000'
        print("send_db_data called")

        # Função para obter ID a partir do nome
        def get_id_from_name(endpoint, name):
            print(f"Fetching ID for {name} from {endpoint}")
            try:
                response = requests.get(base_url + endpoint)
                response.raise_for_status()
                data = response.json()
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

        # Coleta dados e mapeia nomes para IDs
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
        print()
        print(product_data)
        print()
        # Envia os dados para o banco de dados
        try:
            print('trying to connect')
            print()
            url = f"{base_url}/api/update_product/{self.product_data['id']}"
            print('sucessfully')
            print('')
            response = requests.put(url, json=product_data)
            response.raise_for_status()
            print(f"Data sent to database: {response.json()}")
            self.update_loading_screen("Data sent successfully!", True)
        except requests.RequestException as e:
            print(f"Error sending data to the database: {e}")
            self.update_loading_screen("Error sending data.", False)

    def update_loading_screen(self, message, success):
        # Usa o método `after` para garantir que as atualizações sejam feitas na thread principal
        self.loading_screen.after(0, lambda: self.loading_screen_message.set(message))
        if success:
            self.loading_screen.after(0, lambda: self.loading_screen_button.configure(state="normal"))

    def show_loading_screen(self):
        # Cria uma janela pop-up de carregamento
        self.loading_screen = ctk.CTkToplevel(self)
        self.loading_screen.title("Loading")

        # Centraliza a janela pop-up
        self.loading_screen.geometry("300x200+{}+{}".format(
            self.loading_screen.winfo_screenwidth() // 2 - 150,
            self.loading_screen.winfo_screenheight() // 2 - 100
        ))
        self.loading_screen.transient(self)
        self.loading_screen.grab_set()
        self.loading_screen.resizable(False, False)

        # Mensagem e botão da janela de carregamento
        self.loading_screen_message = ctk.StringVar(value="Sending data to the database...")
        message_label = ctk.CTkLabel(self.loading_screen, textvariable=self.loading_screen_message)
        message_label.pack(pady=20)

        self.loading_screen_button = ctk.CTkButton(self.loading_screen, text="OK", command=self.close_loading_screen, state="disabled")
        self.loading_screen_button.pack(pady=20)

        # Atualiza a janela de carregamento para garantir que ela seja exibida antes de enviar os dados
        self.loading_screen.update()

    def send_db_data(self):
        self.show_loading_screen()
        # Envia os dados em um thread separado para não bloquear a UI
        threading.Thread(target=self._send_db_data).start()

    def close_loading_screen(self):
        # Fecha a janela de carregamento e limpa as entradas
        self.loading_screen.destroy()
        for entry in self.entries:
            entry.delete(0, "end")
        self.clear_textbox()

    def close_frame(self):
        self.destroy()

    def delete_product(self):
        self.show_loading_screen()
        # Envia os dados em um thread separado para não bloquear a UI
        threading.Thread(target=self._delete_product).start()

    def _delete_product(self):
        try:
            url = f"http://localhost:5000/api/delete_product/{self.product_data['id']}"
            response = requests.delete(url)
            response.raise_for_status()
            print(f"Product deleted successfully: {response.json()}")
            self.update_loading_screen("Product deleted successfully!", True)
        except requests.RequestException as e:
            print(f"Error deleting product: {e}")
            self.update_loading_screen("Error deleting product.", False)
     
            
    def show_send_btn(self):
        # Coleta os dados e exibe o botão de envio
        self.collect_data()
        send_button = ctk.CTkButton(self.fields_frame, text="Update in database", command=self.send_db_data, fg_color="#2A6CB7", hover_color="blue")
        send_button.grid(row=8, column=0, columnspan=5, pady=5, padx=20, sticky="ew")

    def setup_buttons(self):
        # Cria botões de pré-visualização e cancelamento
        preview_button = ctk.CTkButton(self.fields_frame, text="Preview", command=self.show_send_btn)
        preview_button.grid(row=6, column=0, columnspan=5, pady=5, padx=20, sticky="ew")

        delete_button = ctk.CTkButton(self.fields_frame, text="Delete", command=self.delete_product, fg_color="#FF6961", hover_color="red")
        delete_button.grid(row=7, column=0, columnspan=5, pady=10, padx=20, sticky="ew")
