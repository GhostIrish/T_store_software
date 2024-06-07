import customtkinter as ctk
from tkinter import ttk

class SearchProductFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        
        def show_tree():
            # Sample data to be displayed in the Treeview
            list_names = [['0', 'Hariel', 'harie@hotmail.com'], ['1', 'Beatriz', 'bea@gmail.com'], ['2', 'Miguel', 'miguelpatrulha@gmail.com']]
            
            # Create a Treeview widget with specified columns
            tree_view = ttk.Treeview(self.tree_view_frame, columns=('id', 'name', 'email'), show='headings')
            
            # Configure the column widths
            tree_view.column('id', minwidth=0, width=20)
            tree_view.column('name', minwidth=0, width=250)
            tree_view.column('email', minwidth=0, width=300)
            
            # Set the headings of the columns
            tree_view.heading('id', text='ID')
            tree_view.heading('name', text='NAME')
            tree_view.heading('email', text='EMAIL')

            # Insert data into the Treeview
            for (i, n, e) in list_names:
                tree_view.insert("", "end", values=(i, n, e))

            # Style the Treeview to match the customtkinter theme
            style = ttk.Style()
            style.configure("Treeview.Heading", font=("Helvetica", 12, 'bold'), foreground='white', background='black')
            style.configure("Treeview", background='black', foreground='white', fieldbackground='black')
            style.map('Treeview', background=[('selected', 'green')], foreground=[('selected', 'white')])

            # Pack the Treeview with padding, expanding to fill available space
            tree_view.pack(pady=10, padx=10, expand=True, fill='both')

        # Create and pack the label for the search title
        label_search = ctk.CTkLabel(self, text="Search Product", text_color="white", font=("Arial", 20))
        label_search.pack(pady=20, padx=20)

        # Create and pack the frame for the search bar and button
        search_frame = ctk.CTkFrame(self, fg_color="transparent")
        search_frame.pack(pady=10)

        # Create and pack the search bar entry
        search_bar = ctk.CTkEntry(search_frame, width=600, placeholder_text='Product to search')
        search_bar.pack(side="left", padx=5)

        # Create and pack the Print button, with command to show the Treeview
        btn = ctk.CTkButton(search_frame, width=100, text='Print', command=show_tree)
        btn.pack(side="left", padx=5)

        # Create and pack the frame for the Treeview, with fixed size
        self.tree_view_frame = ctk.CTkFrame(self, width=800, height=400)
        self.tree_view_frame.pack(pady=10, expand=True)
        self.tree_view_frame.pack_propagate(False)

if __name__ == "__main__":
    # Create the main application window
    root = ctk.CTk()
    root.geometry("1000x600")
    
    # Create and pack the main frame into the window
    frame = SearchProductFrame(root)
    frame.pack(fill="both", expand=True)
    
    # Run the application's main loop
    root.mainloop()
