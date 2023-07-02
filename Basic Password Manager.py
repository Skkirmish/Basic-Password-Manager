import tkinter as tk
from tkinter import messagebox

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning("Error", "Please fill in all fields.")
    else:
        with open("passwords.txt", "a") as file:
            file.write(f"Website: {website} | Username: {username} | Password: {password}\n")
        messagebox.showinfo("Success", "Password saved successfully.")
        clear_entries()

def clear_entries():
    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

window = tk.Tk()
window.title("Password Manager")

# Labels
website_label = tk.Label(window, text="Website:")
website_label.grid(row=0, column=0)
username_label = tk.Label(window, text="Username:")
username_label.grid(row=1, column=0)
password_label = tk.Label(window, text="Password:")
password_label.grid(row=2, column=0)

# Entry fields
website_entry = tk.Entry(window, width=30)
website_entry.grid(row=0, column=1)
username_entry = tk.Entry(window, width=30)
username_entry.grid(row=1, column=1)
password_entry = tk.Entry(window, width=30, show="*")
password_entry.grid(row=2, column=1)

# Buttons
save_button = tk.Button(window, text="Save", command=save_password)
save_button.grid(row=3, column=0, columnspan=2, pady=10)
clear_button = tk.Button(window, text="Clear", command=clear_entries)
clear_button.grid(row=4, column=0, columnspan=2)

window.mainloop()