import customtkinter as ctk
import requests

# Função para mostrar produtos e retornar um texto formatado
def show_products(response):
    result = ""
    if response.status_code == 200:
        products = response.json()
        result += "Products found:\n\n"
        for dicionary in products:
            for key, product in dicionary.items():
                result += f'{key}: {product}\n'
            result += '----------------------------------\n'
    else:
        result += 'Error fetching products.\n'
    return result

# Configuração da janela principal
window = ctk.CTk()
window.title("T-store")
window.geometry("1280x720")
window.configure(bg='#0d0d0d')
window.maxsize(width=1366, height=768)
window.minsize(width=800, height=600)
window.resizable(width=False, height=False) # Lock window in chosen size
window._set_appearance_mode("dark")

# Configuração do Textbox
textbox = ctk.CTkTextbox(window, width=500, height=350, scrollbar_button_color="green", fg_color="transparent", border_width=1, border_color="green", border_spacing=20, activate_scrollbars=True)
textbox.pack(pady=20)

# Fazer a requisição e inserir os produtos no Textbox
try:
    response = requests.get('http://localhost:5000/api/products')
    products_text = show_products(response)
    textbox.insert("1.0", products_text)  # Inserir texto no início do Textbox
except requests.exceptions.RequestException as e:
    textbox.insert("1.0", f"An error occurred: {e}")

###
# Executar o loop principal
window.mainloop()

