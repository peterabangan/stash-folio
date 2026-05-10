import tkinter as tk
from tkinter import ttk, messagebox
from database import Database
import bcrypt

db = Database()

root = tk.Tk()
root.title("STASH-FOLIO")
root.geometry("600x600")

#form frame
form_frame = tk.LabelFrame(root, text="Login Details")
form_frame.pack(fill='x', padx=10, pady=5)

#input variables
username_var = tk.StringVar()
password_var = tk.StringVar()

#input fields
#name
tk.Label(form_frame, text="Username:").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(form_frame, textvariable=username_var).grid(row=0, column=1)

tk.Label(form_frame, text="Password:").grid(row=0, column=2, padx=10, pady=5)
password_entry = tk.Entry(form_frame, textvariable=password_var, show="*")
password_entry.grid(row=0, column=3)


























































# When registering - hashing the password
password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# When logging in - checking the password
bcrypt.checkpw(password.encode('utf-8'), stored_hash)