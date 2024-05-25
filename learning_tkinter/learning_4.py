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


#learning_4
# create new window

def new_window():
    new_screen = ctk.CTkToplevel(window, fg_color="green")
    new_screen.geometry("500x250")

center_x = (1280 // 2) - (100 // 2)
center_y = (720 // 2) - (30 // 2)

btn_newwindow = ctk.CTkButton(master=window, text="Open new window", command=new_window).place(x=center_x, y=center_y)


window.mainloop()