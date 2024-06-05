import customtkinter as ctk

class SearchProductFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        def print_entry_text():
            text = search_bar.get()
            textbox.insert('1.0', text=(text + ' ') * 1000, tags='highlight')

            search_bar.delete(first_index=0, last_index=len(text))


        label_search = ctk.CTkLabel(self, text="Search Product", text_color="white", font=("Arial", 20))
        label_search.pack(pady=20, padx=20)

        search_frame = ctk.CTkFrame(self, fg_color="transparent")
        search_frame.pack(pady=10)

        search_bar = ctk.CTkEntry(search_frame, width=600, placeholder_text='Product to search')
        search_bar.pack(side="left", padx=5)

        btn = ctk.CTkButton(search_frame, width=100, text='Print', command=print_entry_text)
        btn.pack(side="left", padx=5)

        textbox = ctk.CTkTextbox(self, width=800, height=450, scrollbar_button_color="green", fg_color="black",
                                 border_width=1, border_color="green", border_spacing=20, activate_scrollbars=True, scrollbar_button_hover_color='black')
        textbox.pack(pady=10)

        textbox.tag_config("highlight", wrap='word', foreground="green", background="black")
        #textbox.insert('1.0', text='test' * 1000)