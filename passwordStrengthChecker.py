import tkinter as tk
from tkinter import messagebox


def password_strength_checker(password): # to check whether is password is strong or weak
    if(len(password) < 8):
        return "Weak.Too Short Password"
    has_upper = has_lower = has_digit = has_specialChar = False #setting all checking variable to false
    special_character ="*/!$#^@_?" 

    for char in password :        # it iterates over the user password and checks for specified conditions.                   
        if 'A' <= char <= 'Z':    #and set true for the check variable if condition satisfies
            has_upper = True
        elif 'a' <= char <= 'z':
            has_lower = True
        elif '0' <= char <='9':
            has_digit = True
        elif char in special_character:
            has_specialChar = True


    
    if not has_upper:                                       # if none of the condition matches it will return some message Accordingly
        return "Weak.UpperCase Character is missing!!!"
    if not has_lower:
        return "Weak.LowerCase Character is missing!!!"
    if not has_digit:
        return "Weak.Digit is Missing!!!"
    if not has_specialChar:
        return "Weak.SpecialCharacter Missing!!!"
    
    return "Strong password!!!"
def show_result():                                     # function to display results through tkiner messageBox
    password = entry.get()
    result = password_strength_checker(password)
    messagebox.showinfo("Password Strength:",result)

root = tk.Tk()                                  
root.title("Password Strength Checker")
root.geometry("300x150")
root.configure(bg="#2C3E50")

tk.Label(root,text="Enter Your Password:",fg="white",bg="#2C3E50", font=("Arial",10)).pack(pady=10)
entry = tk.Entry(root,show="*",width=25,bg="#ECF0F1",highlightthickness=2,highlightbackground="#3498DB")
entry.pack(pady=5)

tk.Button(root,text="Check Strength",command=show_result,bg="green",fg="white",activebackground="#2980B9",borderwidth=5,relief="raised",
          font=("Arial",10)).pack(padx=50,pady=10)
root.mainloop()