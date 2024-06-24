import customtkinter as ctk

window = ctk.CTk()
window.geometry("1280x720")
window.title("StyleHub - DashBoard")
window.resizable(False, False)
    

optionmenu_var = ctk.StringVar(value="option 2")  # set initial value

def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

combobox = ctk.CTkOptionMenu(master=window,
                                       values=["option 1", "option 2"],
                                       command=optionmenu_callback,
                                       variable=optionmenu_var)
combobox.pack(padx=20, pady=10)

window.mainloop()