import customtkinter as ctk

class ReportProductFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        label_reports = ctk.CTkLabel(self, text="Available Reports", text_color="white", font=("Arial", 20))
        label_reports.pack(pady=20, padx=20)
