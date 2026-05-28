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

tk.Label(form_frame, text="Category:", bg="#BEBEBE", fg="#000000", font=("Arial", 11)).pack(side='left', padx=5)
category_combo = ttk.Combobox(form_frame, textvariable=category_var, state="readonly", width=20)
category_combo.pack(side='left', padx=5)

tk.Label(form_frame, text="Amount:", bg="#BEBEBE", fg="#000000", font=("Arial", 11)).pack(side='left', padx=5)
tk.Entry(form_frame, textvariable=amount_var, width=15).pack(side='left', padx=5)


#treeview
tree = ttk.Treeview(table_frame, columns=("ID", "Transaction Type", "Category", "Amount", "Date"), show="headings")
for col in ("ID", "Transaction Type", "Category", "Amount", "Date"):
    tree.heading(col, text=col)
#scrollbar for treeview
scrollbar = ttk.Scrollbar(table_frame, orient="vertical")
scrollbar.config(command=tree.yview)
tree.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side='right', fill='y')
tree.pack(fill='both', expand=True)

#functions

def update_categories(*args):
    if transaction_type_var.get() == "Income":
        category_combo["values"] = ["Salary", "Freelance", "Business", "Investment", "Other"]
    else:
        category_combo["values"] = ["Food", "Transport", "Shopping", "Rent", "Utilities", "Entertainment", "Health", "Other"]
    category_var.set("")

transaction_type_var.trace("w", update_categories)

def load_transactions():
    for row in tree.get_children():
        tree.delete(row)
    for record in db.get_all_transactions(user_id):
        tree.insert("", "end", values=record)

def add_transaction():
    if not transaction_type_var.get() or not category_var.get() or not amount_var.get():
        messagebox.showerror("Error", "All fields are required.")
        return
    if not amount_var.get().isdigit():
        messagebox.showerror("Error", "Amount must be a number(s).")
        return
    db.add_transaction(user_id, transaction_type_var.get(), category_var.get(), amount_var.get())
    load_transactions()

def delete_transaction():
    selected = tree.focus()
    if not selected:
        messagebox.showerror("Error", "Select a transaction first.")
        return
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this transaction?")
    if confirm:
        id = tree.item(selected)["values"][0]
        db.delete_transactions(id)
        load_transactions()

def update_transaction():
    selected = tree.focus()
    if not selected:
        messagebox.showerror("Error", "Select a transaction first.")
        return
    id = tree.item(selected)["values"][0]
    db.update_transactions(id, user_id, transaction_type_var.get() , category_var.get() , amount_var.get())
    load_transactions()

def select_transaction(event):
    selected = tree.focus()
    if selected:
        values = tree.item(selected)["values"]
        transaction_type_var.set(values[1])
        category_var.set(values[2])
        amount_var.set(values[3])

def clear_fields():
    transaction_type_var.set("")
    category_var.set("")
    amount_var.set("")

def logout():
    root.destroy()


#buttons
tk.Button(top_bar, text="Logout", command=logout, bg="#3C3489", fg="#EEEDFE", relief="flat", borderwidth=0).pack(side='right')
tk.Button(button_frame, text="Add Transaction", command=add_transaction, bg="#3C3489", fg="#EEEDFE", relief="flat", borderwidth=0).pack(side='left', padx=5)
tk.Button(button_frame, text="Update Transaction", command=update_transaction, bg="#3C3489", fg="#EEEDFE", relief="flat", borderwidth=0).pack(side='left', padx=5)
tk.Button(button_frame, text="Delete Transaction", command=delete_transaction, bg="#3C3489", fg="#EEEDFE", relief="flat", borderwidth=0).pack(side='left', padx=5)
tk.Button(button_frame, text="Clear Fields", command=clear_fields, bg="#3C3489", fg="#EEEDFE", relief="flat", borderwidth=0).pack(side='left', padx=5)




tree.bind("<ButtonRelease-1>", select_transaction)
load_transactions()

root.mainloop()

