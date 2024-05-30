import customtkinter as ctk

window = ctk.CTk()

# learning_2
window.title("T-store")
window.geometry("1280x720")
window.configure(bg='#0d0d0d')
window.maxsize(width=1366, height=768)
window.minsize(width=800, height=600)
window.resizable(width=False, height=False) # -> Lock window in choosed size, can't increasewidth and height

window._set_appearance_mode("dark") #-> set theme in software

dialog = ctk.CTkEntry(window, width=600)
dialog.pack(padx=20, pady= 20)
#print(dialog.)

def print_entry_text():
    text = dialog.get()
    print(text)
    
    dialog.delete(first_index=0, last_index=len(text))


btn = ctk.CTkButton(window, text='print text', command=print_entry_text)
btn.pack(pady=10)



window.mainloop()
