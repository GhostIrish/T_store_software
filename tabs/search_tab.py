import customtkinter as ctk
from tkinter import ttk

class SearchProductFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        label_search = ctk.CTkLabel(self, text="Search Product", text_color="white", font=("Arial", 20))
        label_search.pack(pady=20, padx=20)

        search_frame = ctk.CTkFrame(self, fg_color="transparent")
        search_frame.pack(pady=10)

        search_bar = ctk.CTkEntry(search_frame, width=600, placeholder_text='Product to search')
        search_bar.pack(side="left", padx=5)

        btn = ctk.CTkButton(search_frame, width=100, text='Print')
        btn.pack(side="left", padx=5)
        
        
        
        # Sample data to be displayed in the Treeview
        list_names = [['0', 'Hariel', 'harie@hotmail.com'], ['1', 'Beatriz', 'bea@gmail.com'], ['2', 'Miguel', 'miguelpatrulha@gmail.com']]


        self.tree_view_frame = ctk.CTkFrame(self, width=800, height=400)
        tree_view = ttk.Treeview(self.tree_view_frame, columns=('id', 'name', 'email'), show='headings')
        tree_view.column('id', minwidth=50, width=200)
        tree_view.column('name', minwidth=50, width=300)
        tree_view.column('email', minwidth=50, width=300)
        tree_view.heading('id', text='ID')
        tree_view.heading('name', text='NAME')
        tree_view.heading('email', text='EMAIL')
        
        for (i, n, e) in list_names:
                tree_view.insert("", "end", values=(i, n, e))
        
        
        
        
        
        tree_view.pack(expand=True, fill='both')
        
        # Create and pack the frame for the Treeview, with fixed size
        self.tree_view_frame.pack()
        self.tree_view_frame.pack_propagate(False)