from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image

root  = Tk()
root.title("Login Page")
root.geometry("350x500")
root.configure(background='#0096DC')

def checkUser():
    uname = uname_entry.get()
    psw = psw_entry.get()
    if uname =='admin' and psw =='123':
        messagebox.showinfo("Login Message","Login Successfull")
    else:
        messagebox.showerror("Error","Wrong UserName and Password")


label=tk.Label(root,text="Login Form",font=("verdana",24),bg="#0096DC",fg="white")
label.pack(pady=20)
uname_label =tk.Label(root,text="Enter UserName:",font=("verdana",12),bg="#0096DC",fg="white")
uname_label.pack()
uname_entry = tk.Entry(root,width=50)
uname_entry.pack(pady=(10,40),ipady=5)

psw_label = tk.Label(root,text="Enter Password:",font=("verdana",12),bg="#0096DC",fg="white")
psw_label.pack()
psw_entry = tk.Entry(root,width=50,show="*")
psw_entry.pack(pady=(10,40),ipady=5)


login_btn =tk.Button(root,text="Login",bg="green",fg="black",
          width=10,activebackground="lightgreen",activeforeground="black",font=("verdana",12),command=checkUser)
login_btn.pack(pady=10,ipady=5,ipadx=30)




root.mainloop()