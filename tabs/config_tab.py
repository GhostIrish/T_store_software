import customtkinter as ctk

class ConfigProductFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        label_configs = ctk.CTkLabel(self, text="System Configurations", text_color="white", font=("Arial", 20))
        label_configs.pack(pady=20, padx=20)
