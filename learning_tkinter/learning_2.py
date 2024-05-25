import customtkinter as ctk

window = ctk.CTk()

window.title("T-store")
window.geometry("1280x720")
window.maxsize(width=1366, height=768)
window.minsize(width=800, height=600)
#window.resizable(width=False, height=False) -> Lock window in choosed size, can't increasewidth and height
#window.iconify() -> close the window
#window.deiconfiy() -> throw back the closed window

window.mainloop()