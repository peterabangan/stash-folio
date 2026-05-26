import tkinter as tk
from tkinter import ttk, messagebox
from database import Database 

db = Database()

root = tk.Tk()
root.title("Stash-Folio")
root.geometry("1600x1600")
root.configure(bg="#F1EFE8")

#form frame and border
top_bar = tk.Frame(root, bg="#534AB7", padx=10, pady=8)
top_bar.pack(fill='x')

form_frame = tk.Frame(root, bg="#FFFFFF", padx=20, pady=20)
form_frame.pack()

#variables






#widgets
tk.Label(top_bar, text="Welcome!", bg="#534AB7", fg="#EEEDFE", font=("Arial", 11)).pack(side='left')


#buttons
tk.Button(top_bar, text="Logout", bg="#3C3489", fg="#EEEDFE", relief="flat", borderwidth=0).pack(side='right')

root.mainloop()

