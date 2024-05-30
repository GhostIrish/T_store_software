# import customtkinter as ctk

# window = ctk.CTk()

# # learning_2
# window.title("T-store")
# window.geometry("1280x720")
# window.configure(bg='#0d0d0d')
# window.maxsize(width=1366, height=768)
# window.minsize(width=800, height=600)
# window.resizable(width=False, height=False) # -> Lock window in choosed size, can't increase width and height
# window._set_appearance_mode("dark")

# textbox = ctk.CTkTextbox(window, width=500, height=350)
# textbox.pack()

# textbox.insert("0.0", "Title of you text" + "\nlorem" * 100)


# window.mainloop()

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
    
    report_button = ctk.CTkButton(frame_nav, text="Reports", command=lambda: show_frame(report_frame))
    report_button.grid(row=1, column=0, pady=10, padx=20, sticky="ew")
    
    config_button = ctk.CTkButton(frame_nav, text="Configs", command=lambda: show_frame(config_frame))
    config_button.grid(row=2, column=0, pady=10, padx=20, sticky="ew")

    # Create the main content frame
    content_frame = ctk.CTkFrame(window, width=1080, height=720, corner_radius=10, border_width=1, border_color='green')
    content_frame.grid(row=0, column=1, sticky="nswe", padx=(10, 5), pady=(10))
    
    # Create a centered frame inside the content frame
    center_frame = ctk.CTkFrame(content_frame, width=1080, height=720, corner_radius=10, fg_color="transparent")
    center_frame.pack(fill="both", expand=True, padx=20, pady=20)
    
    # Create subframes for different sections within the center frame
    add_frame = ctk.CTkFrame(center_frame, corner_radius=10, fg_color="transparent")
    report_frame = ctk.CTkFrame(center_frame, corner_radius=10, fg_color="transparent")
    config_frame = ctk.CTkFrame(center_frame, corner_radius=10, fg_color="transparent")
    
    # Position the subframes to cover the entire center frame
    for frame in (add_frame, report_frame, config_frame):
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    # Add content to the add_frame
    label_add = ctk.CTkLabel(add_frame, text="Add new item", text_color="white", font=("Arial", 20))
    label_add.pack(pady=20, padx=20)

    # Create labels and entry fields for the add_frame
    labels = ["Field 1", "Field 2", "Field 3", "Field 4", "Field 5"]
    entries = []

    for label in labels:
        # Create a frame for each label-entry pair
        field_frame = ctk.CTkFrame(add_frame, fg_color="transparent")
        field_frame.pack(fill="x", pady=5, padx=20)
        
        # Add the label
        lbl = ctk.CTkLabel(field_frame, text=label, text_color="white")
        lbl.pack(side="left", padx=(0, 10))
        
        # Add the entry field
        entry = ctk.CTkEntry(field_frame, placeholder_text=f"Digite {label.lower()}", width=600)
        entry.pack(side="left", fill="x", expand=True)
        entries.append(entry)

    # Add the send button to the add_frame
    botao_enviar = ctk.CTkButton(add_frame, text="Enviar")
    botao_enviar.pack(pady=20, padx=20)

    # Add content to the report_frame
    label_reports = ctk.CTkLabel(report_frame, text="Relatórios disponíveis", text_color="white")
    label_reports.pack(pady=20, padx=20)

    # Add content to the config_frame
    label_configs = ctk.CTkLabel(config_frame, text="Configurações do sistema", text_color="white")
    label_configs.pack(pady=20, padx=20)

    # Show the add_frame by default when the application starts
    show_frame(add_frame)

    # Run the main event loop of the application
    window.mainloop()

# Call the function to create and start the main window
create_main_window()
