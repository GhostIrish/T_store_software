import customtkinter as ctk
import ctypes


# C:\\Users\\harie\\project_t_store\\stylehub_icon.ico -> path where the icon stay
# pyinstaller --onefile --windowed --icon=C:\\Users\\harie\\project_t_store\\icon_1.ico tkinterfront.py -> transform code in exe where icon logo is applyed.

# Custom configs
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Function to be called and set an icon in window and in windows nav bar
def set_app_icon(icon_path):
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
    window.iconbitmap(icon_path)


# Function to create main window
def create_main_window():
    global window
    
    # Config main window
    window = ctk.CTk()
    window.geometry("1280x720")
    window.title("StyleHub - DashBoard")

    # locate path where your icon is save and call function to set him.
    icon_path = "C:\\Users\\harie\\project_t_store\\icon_1.ico"
    set_app_icon(icon_path)
    
    # Config lines to expand window if you prefer size it up or down.
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)

    # Config lateral nav bar
    frame_nav = ctk.CTkFrame(window, width=200, height=720, corner_radius=10)
    frame_nav.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)

    # Buttons to navigate into software
    add_button = ctk.CTkButton(frame_nav, text="Add", command=lambda: show_frame(add_frame))
    add_button.grid(row=0, column=0, pady=10, padx=20, sticky="ew")
    
    report_button = ctk.CTkButton(frame_nav, text="Reports", command=lambda: show_frame(report_frame))
    report_button.grid(row=1, column=0, pady=10, padx=20, sticky="ew")
    
    config_button = ctk.CTkButton(frame_nav, text="Configs", command=lambda: show_frame(config_frame))
    config_button.grid(row=2, column=0, pady=10, padx=20, sticky="ew")

    # main content about the window
    content_frame = ctk.CTkFrame(window, width=1080, height=720, corner_radius=10)
    content_frame.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)
    
    # buttons subframes, content you see if you click in buttom
    add_frame = ctk.CTkFrame(content_frame, corner_radius=10, fg_color="transparent")
    report_frame = ctk.CTkFrame(content_frame, corner_radius=10, fg_color="transparent")
    config_frame = ctk.CTkFrame(content_frame, corner_radius=10, fg_color="transparent")
    
    for frame in (add_frame, report_frame, config_frame):
        frame.grid(row=0, column=0, sticky="nswe")
    
    # Content inside frame_add.
    label_add = ctk.CTkLabel(add_frame, text="Add new item", text_color="white", font=("Arial", 20))
    label_add.grid(row=0, column=0, pady=20, padx=20, columnspan=2)

    # Forms fields
    labels = ["Field 1", "Field 2", "Field 3", "Field 4", "Field 5"]
    entries = []

    for i, label in enumerate(labels):
        lbl = ctk.CTkLabel(add_frame, text=label, text_color="white")
        lbl.grid(row=i+1, column=0, pady=10, padx=20, sticky="e")

        entry = ctk.CTkEntry(add_frame, placeholder_text=f"Digite {label.lower()}")
        entry.grid(row=i+1, column=1, pady=10, padx=20, sticky="w")
        entries.append(entry)

    # Button send
    botao_enviar = ctk.CTkButton(add_frame, text="Enviar")
    botao_enviar.grid(row=6, column=0, columnspan=2, pady=20, padx=20)

    # Button Reports
    label_relatorios = ctk.CTkLabel(report_frame, text="Relatórios disponíveis", text_color="white")
    label_relatorios.grid(row=0, column=0, pady=20, padx=20)

    # Content about frames.
    label_configuracoes = ctk.CTkLabel(config_frame, text="Configurações do sistema", text_color="white")
    label_configuracoes.grid(row=0, column=0, pady=20, padx=20)

    # Function to show right frame
    def show_frame(frame):
        frame.tkraise()

    # at start, the software show add frame
    show_frame(add_frame)

    # Execute app
    window.mainloop()

# Call the launch function to start window
create_main_window()
