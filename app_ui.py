import tkinter as tk
from tkinter import ttk, messagebox
from database import Database 

db = Database()

root = tk.Tk()
root.title("Stash-Folio")
root.geometry("1600x1600")
root.configure(bg="#F1EFE8")

#frames
top_bar = tk.Frame(root, bg="#534AB7", padx=10, pady=8)
top_bar.pack(fill='x')

form_frame = tk.LabelFrame(root, text="Add Transaction", bg="#FFFFFF", fg="#26215C", font=("Arial", 10, "bold"))
form_frame.pack(fill='x', padx=10, pady=5)

table_frame = tk.LabelFrame(root, text="Transactions", bg="#FFFFFF", fg="#26215C", font=("Arial", 10, "bold"))
table_frame.pack(fill='x', padx=10, pady=5)

button_frame = tk.LabelFrame(root, text="Actions", bg="#FFFFFF", fg="#26215C", font=("Arial", 10, "bold"))
button_frame.pack(fill='x', padx=10, pady=5)


#variables
user_id = None
transaction_type_var = tk.StringVar()
category_var = tk.StringVar()
amount_var = tk.StringVar()

#widgets
tk.Label(top_bar, text="Welcome!", bg="#534AB7", fg="#EEEDFE", font=("Arial", 11)).pack(side='left')
tk.Label(form_frame, text="Transaction Type:", bg="#BEBEBE", fg="#000000", font=("Arial", 11)).pack(side='left')
ttk.Combobox(form_frame, textvariable=transaction_type_var, values=["Income", "Expense"], state="readonly").pack(side='left')

tk.Label(table_frame, text="Categories:", bg="#BEBEBE", fg="#000000", font=("Arial", 11)).pack(side='left')
ttk.Combobox(table_frame, textvariable=category_var, values=["Salary", "Freelance", "Business", "Investment", "Other"], state="readonly").pack(side='left')
ttk.Combobox(table_frame, textvariable=category_var, values=["Food", "Transport", "Shopping", "Rent", "Utilities", "Entertainment", "Health", "Other"], state="readonly").pack(side='left')


#buttons
tk.Button(top_bar, text="Logout", bg="#3C3489", fg="#EEEDFE", relief="flat", borderwidth=0).pack(side='right')

root.mainloop()

