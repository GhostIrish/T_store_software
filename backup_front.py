import customtkinter as ctk
import ctypes
from PIL import Image, ImageTk

# C:\\Users\\harie\\project_t_store\\stylehub_icon.ico -> path where the icon stay
# pyinstaller --onefile --windowed --icon=C:\\Users\\harie\\project_t_store\\icon_1.ico tkinterfront.py -> transform code in exe where icon logo is applyed.

# Configurações gerais do CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def set_app_icon(icon_path):
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
    window.iconbitmap(icon_path)


# Função para criar a janela principal
def criar_janela_principal():
    global window
    # Configurando a janela principal
    window = ctk.CTk()
    window.geometry("1280x720")
    window.title("Software de Gerenciamento")

    #window.after(201, lambda :window.iconbitmap("C:\\Users\\harie\\project_t_store\\icon_1.ico"))

    icon_path = "C:\\Users\\harie\\project_t_store\\icon_1.ico"
    # window.iconphoto(False, file="icon_3.png")
    
    set_app_icon(icon_path)
    
    # Configurando a linha 0 para expandir
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)

    # Barra de navegação lateral
    frame_nav = ctk.CTkFrame(window, width=200, height=720, corner_radius=10)
    frame_nav.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)

    # Botões de navegação empilhados verticalmente
    add_button = ctk.CTkButton(frame_nav, text="Adicionar", command=lambda: show_frame(add_frame))
    add_button.grid(row=0, column=0, pady=10, padx=20, sticky="ew")
    
    report_button = ctk.CTkButton(frame_nav, text="Relatórios", command=lambda: show_frame(report_frame))
    report_button.grid(row=1, column=0, pady=10, padx=20, sticky="ew")
    
    config_button = ctk.CTkButton(frame_nav, text="Configurações", command=lambda: show_frame(config_frame))
    config_button.grid(row=2, column=0, pady=10, padx=20, sticky="ew")

    # Área de conteúdo principal
    content_frame = ctk.CTkFrame(window, width=1080, height=720, corner_radius=10)
    content_frame.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)
    
    # Subframes para diferentes seções
    add_frame = ctk.CTkFrame(content_frame, corner_radius=10, fg_color="transparent")
    report_frame = ctk.CTkFrame(content_frame, corner_radius=10, fg_color="transparent")
    config_frame = ctk.CTkFrame(content_frame, corner_radius=10, fg_color="transparent")
    
    for frame in (add_frame, report_frame, config_frame):
        frame.grid(row=0, column=0, sticky="nswe")
    
    # Conteúdo do frame "Adicionar"
    label_add = ctk.CTkLabel(add_frame, text="Adicionar Novo Item", text_color="white", font=("Arial", 20))
    label_add.grid(row=0, column=0, pady=20, padx=20, columnspan=2)

    # Fields do formulário
    labels = ["Field 1", "Field 2", "Field 3", "Field 4", "Field 5"]
    entries = []

    for i, label in enumerate(labels):
        lbl = ctk.CTkLabel(add_frame, text=label, text_color="white")
        lbl.grid(row=i+1, column=0, pady=10, padx=20, sticky="e")

        entry = ctk.CTkEntry(add_frame, placeholder_text=f"Digite {label.lower()}")
        entry.grid(row=i+1, column=1, pady=10, padx=20, sticky="w")
        entries.append(entry)

    # Botão de enviar
    botao_enviar = ctk.CTkButton(add_frame, text="Enviar")
    botao_enviar.grid(row=6, column=0, columnspan=2, pady=20, padx=20)

    # Conteúdo do frame "Relatórios"
    label_relatorios = ctk.CTkLabel(report_frame, text="Relatórios disponíveis", text_color="white")
    label_relatorios.grid(row=0, column=0, pady=20, padx=20)

    # Conteúdo do frame "Configurações"
    label_configuracoes = ctk.CTkLabel(config_frame, text="Configurações do sistema", text_color="white")
    label_configuracoes.grid(row=0, column=0, pady=20, padx=20)

    # Função para mostrar o frame correto
    def show_frame(frame):
        frame.tkraise()

    # Inicialmente mostrar o frame "Adicionar"
    show_frame(add_frame)

    # Executando a aplicação
    window.mainloop()

# Chamando a função para criar a janela principal
criar_janela_principal()
