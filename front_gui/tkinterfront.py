import customtkinter as ctk
import ctypes

# Set custom appearance and color theme for the app
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Function to set an icon for the application window
def set_app_icon(icon_path):
    # Set the application ID for the taskbar icon
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
    # Set the window icon using the provided icon path
    window.iconbitmap(icon_path)

# Function to bring a specific frame to the front
def show_frame(frame):
    frame.tkraise()

# Function to create the main window of the application
def create_main_window():
    global window, add_frame, report_frame, config_frame
    
    # Initialize the main window
    window = ctk.CTk()
    window.geometry("1280x720")  # Set window size
    window.title("StyleHub - DashBoard")  # Set window title
    window.resizable(False, False)  # Disable window resizing
    #window.minsize(width=800, height=600)
    
    # Set the application icon
    icon_path = "C:\\Users\\harie\\project_t_store\\icons\\icon_1.ico"
    set_app_icon(icon_path)
    
    # Configure the window to expand rows and columns if needed
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)

    # Create the navigation bar frame on the left side
    frame_nav = ctk.CTkFrame(window, width=200, height=720, corner_radius=10, border_width=1, border_color='green')
    frame_nav.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)

    # Buttons to navigate through different sections of the software
    add_button = ctk.CTkButton(frame_nav, text="Add", command=lambda: show_frame(add_frame))
    add_button.grid(row=0, column=0, pady=10, padx=20, sticky="ew")
    
    update_button = ctk.CTkButton(frame_nav, text="Update", command=lambda: show_frame(update_frame))
    update_button.grid(row=1, column=0, pady=10, padx=20, sticky="ew")
    
    search_button = ctk.CTkButton(frame_nav, text="Search", command=lambda: show_frame(search_frame))
    search_button.grid(row=2, column=0, pady=10, padx=20, sticky="ew")
    
    report_button = ctk.CTkButton(frame_nav, text="Reports", command=lambda: show_frame(report_frame))
    report_button.grid(row=3, column=0, pady=10, padx=20, sticky="ew")
    
    config_button = ctk.CTkButton(frame_nav, text="Configs", command=lambda: show_frame(config_frame))
    config_button.grid(row=4, column=0, pady=10, padx=20, sticky="ew")

    # Create the main content frame
    content_frame = ctk.CTkFrame(window, width=1080, height=720, corner_radius=10, border_width=1, border_color='green')
    content_frame.grid(row=0, column=1, sticky="nswe", padx=(10, 5), pady=(10))
    
    # Create a centered frame inside the content frame
    center_frame = ctk.CTkFrame(content_frame, width=1080, height=720, corner_radius=10, fg_color="transparent")
    center_frame.pack(fill="both", expand=True, padx=20, pady=20)
    
    # Create subframes for different sections within the center frame
    add_frame = ctk.CTkFrame(center_frame, corner_radius=10, fg_color="transparent")
    update_frame = ctk.CTkFrame(center_frame, corner_radius=10, fg_color="transparent")
    search_frame = ctk.CTkFrame(center_frame, corner_radius=10, fg_color="transparent")
    report_frame = ctk.CTkFrame(center_frame, corner_radius=10, fg_color="transparent")
    config_frame = ctk.CTkFrame(center_frame, corner_radius=10, fg_color="transparent")
    
    # Position the subframes to cover the entire center frame
    for frame in (add_frame, update_frame, search_frame, report_frame, config_frame):
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    # Add content to the add_frame
    label_add = ctk.CTkLabel(add_frame, text="Add new item", text_color="white", font=("Arial", 20))
    label_add.pack(pady=20, padx=20)

    # Create a frame to hold all the fields
    fields_frame = ctk.CTkFrame(add_frame, fg_color="transparent")
    fields_frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Create labels and entry fields for the add_frame
    labels = ["Product ", "Type ", "Size ", "Gender ", "Brand ", "Buying price ", "Selling price ", "Quantity "]
    entries = []

    for i, label in enumerate(labels):
        # Add the label
        lbl = ctk.CTkLabel(fields_frame, text=label, text_color="white")
        #lbl.pack(side="left", padx=(0, 10))
        lbl.grid(row=i, column=0, padx=10, pady=5, sticky="e")
        
        # Add the entry field
        entry = ctk.CTkEntry(fields_frame, placeholder_text=f"Write {label.lower()}", width=800)
        #entry.pack(fill="x", expand=True, padx=(0, 0))
        entry.grid(row=i, column=1, padx=10, pady=5, sticky="ew")
        entries.append(entry)

    # Add the send button to the add_frame
    botao_enviar = ctk.CTkButton(add_frame, text="Send")
    botao_enviar.pack(pady=20, padx=20)

    # Add content to the update_frame
    label_update = ctk.CTkLabel(update_frame, text="Updates", text_color="white", font=("Arial", 20))
    label_update.pack(pady=20, padx=20)
    
    # Add content to the report_frame
    label_search = ctk.CTkLabel(search_frame, text="Search", text_color="white", font=("Arial", 20))
    label_search.pack(pady=20, padx=20)
    
    # Add content to the report_frame
    label_reports = ctk.CTkLabel(report_frame, text="Future feature reports", text_color="white", font=("Arial", 20))
    label_reports.pack(pady=20, padx=20)

    # Add content to the config_frame
    label_configs = ctk.CTkLabel(config_frame, text="System configs", text_color="white", font=("Arial", 20))
    label_configs.pack(pady=20, padx=20)

    # Show the add_frame by default when the application starts
    show_frame(add_frame)

    print(entries)
    
    # Run the main event loop of the application  
    return window.mainloop()

# Call the function to create and start the main window
create_main_window()
