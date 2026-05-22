import tkinter as tk
from tkinter import ttk, messagebox
from database import Database
import bcrypt

db = Database()

root = tk.Tk()
root.title("Stash-Folio")
root.geometry("600x600")
root.configure(bg="#F1EFE8")

#form frame and border
card_border = tk.Frame(root, bg="#AFA9EC", padx=1, pady=1)
card_border.place(relx=0.5, rely=0.5, anchor="center")

form_frame = tk.Frame(card_border, bg="#FFFFFF", padx=20, pady=20)
form_frame.pack()

#input variables
username_var = tk.StringVar()
password_var = tk.StringVar()

#widgets

tk.Label(form_frame, text="💸Stash-Folio🙌", bg="#FFFFFF", fg="#26215C", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=4, pady=10)
tk.Label(form_frame, text="Your personal budget tracker", bg="#FFFFFF", fg="#888780", font=("Arial", 9)).grid(row=1, column=0, columnspan=4, pady=2)
tk.Label(form_frame, text="Username:", bg="#FFFFFF", fg="#26215C").grid(row=2, column=1, padx=10, pady=5)
tk.Entry(form_frame, textvariable=username_var, bg="#AA6161", relief="flat", width=25).grid(row=2, column=2)

tk.Label(form_frame, text="Password:", bg="#FFFFFF", fg="#26215C").grid(row=3, column=1, padx=10, pady=5)
password_entry = tk.Entry(form_frame, textvariable=password_var, bg="#AA6161", relief="flat", show="*", width=25)
password_entry.grid(row=3, column=2)

#functions
def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

def login():
    if not username_var.get() or not password_var.get():
        messagebox.showerror("Error", "All fields are required.")
        return
    user = db.get_user(username_var.get())
    if not user:
        messagebox.showerror("Error", "User does not exist.")
        return
    if not bcrypt.checkpw(password_var.get().encode('utf-8'), user[2].encode('utf-8')):
        messagebox.showerror("Error", "Wrong password.")
        return
    else: 
        messagebox.showinfo("Success!", f"Welcome, {username_var.get()}!")
        return
def register():
    if not username_var.get() or not password_var.get():
        messagebox.showerror("Error", "All fields are required.")
        return
    user = db.get_user(username_var.get())
    if user:
        messagebox.showerror("Error", "Username already exists.")
        return
    else:
        password_hash = bcrypt.hashpw(password_var.get().encode('utf-8'), bcrypt.gensalt())
        db.register_user(username_var.get(), password_hash)
        messagebox.showinfo("Success!", f"Account Created! Welcome, {username_var.get()}!")

#Buttons

button_group = tk.Frame(form_frame, bg="#FFFFFF")
button_group.grid(row=4, column=0, columnspan=3, pady=10)

tk.Button(button_group, text="👁", command=toggle_password, bg="#534AB7", fg="#EEEDFE", relief="flat", borderwidth=0, padx=10, pady=5).pack(side='left', padx=5)
tk.Button(button_group, text="Login", command=login, bg="#534AB7", fg="#EEEDFE", relief="flat", borderwidth=0, padx=10, pady=5).pack(side='left', padx=5)
tk.Button(button_group, text="Register", command=register, bg="#534AB7", fg="#EEEDFE", relief="flat", borderwidth=0, padx=10, pady=5).pack(side='left', padx=5)

root.mainloop()

















