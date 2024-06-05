import customtkinter as ctk

class UpdateProductFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        label_update = ctk.CTkLabel(self, text="Update Product", text_color="white", font=("Arial", 20))
        label_update.pack(pady=20, padx=20)

        fields_frame = ctk.CTkFrame(self, fg_color="transparent")
        fields_frame.pack(pady=20, padx=20, fill="both", expand=True)

        labels = ["Product ", "Type ", "Size ", "Gender ", "Brand ", "Buying price ", "Selling price ", "Quantity "]
        self.entries = []

        for i, label in enumerate(labels):
            lbl = ctk.CTkLabel(fields_frame, text=label, text_color="white")
            lbl.grid(row=i, column=0, padx=10, pady=5, sticky="e")

            entry = ctk.CTkEntry(fields_frame, placeholder_text=f"Write {label.lower()}", width=800)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="ew")
            self.entries.append(entry)

        send_button = ctk.CTkButton(self, text="Update")
        send_button.pack(pady=20, padx=20)
