import customtkinter as ctk

window = ctk.CTk()

# learning_2
window.title("T-store")
window.geometry("1280x720")
window.maxsize(width=1366, height=768)
window.minsize(width=800, height=600)
#window.resizable(width=False, height=False) -> Lock window in choosed size, can't increasewidth and height
#window.iconify() -> close the window
#window.deiconfiy() -> throw back the closed window

#learning_3
window._set_appearance_mode("dark") #-> set theme in software

window.mainloop()