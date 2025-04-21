import random
import tkinter as tk
from tkinter import messagebox

# Function to generate a password
def generate_password():
    try:
        n_letters = int(entry_letters.get())
        n_numbers = int(entry_numbers.get())
        n_symbols = int(entry_symbols.get())

        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        symbols = "()/$#@&"

        password_list = []
        
        # Generate letters, numbers, and symbols
        password_list += [random.choice(letters) for _ in range(n_letters)]
        password_list += [random.choice(numbers) for _ in range(n_numbers)]
        password_list += [random.choice(symbols) for _ in range(n_symbols)]
        
        # Shuffle and join the password
        random.shuffle(password_list)
        password = "".join(password_list)

        # Show password in entry field and popup
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
        messagebox.showinfo("Generated Password", f"Your Password: {password}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

# Create main GUI window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg="#2C3E50")

# Title Label
tk.Label(root, text="Password Generator", font=("Arial", 14, "bold"), 
         bg="#2C3E50", fg="white").pack(pady=10)

# Labels and Entry Fields
tk.Label(root, text="Number of Letters:", bg="#2C3E50", fg="white", font=("Arial", 10)).pack()
entry_letters = tk.Entry(root, font=("Arial", 12), width=10, bg="#ECF0F1")
entry_letters.pack(pady=2)

tk.Label(root, text="Number of Numbers:", bg="#2C3E50", fg="white", font=("Arial", 10)).pack()
entry_numbers = tk.Entry(root, font=("Arial", 12), width=10, bg="#ECF0F1")
entry_numbers.pack(pady=2)

tk.Label(root, text="Number of Symbols:", bg="#2C3E50", fg="white", font=("Arial", 10)).pack()
entry_symbols = tk.Entry(root, font=("Arial", 12), width=10, bg="#ECF0F1")
entry_symbols.pack(pady=2)

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password, 
          font=("Arial", 12), bg="#3498DB", fg="white", activebackground="#2980B9").pack(pady=10)

# # Output Field
entry_password = tk.Entry(root, font=("Arial", 12), width=25, bg="#ECF0F1", justify="center")
entry_password.pack(pady=5)

# Run the GUI
root.mainloop()