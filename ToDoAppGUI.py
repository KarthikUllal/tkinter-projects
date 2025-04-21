import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")
root.geometry("450x450")
root.configure(bg="#2C3E50")

tk.Label(root,text="Enter Your Task Here",fg="white",bg="#2C3E50", font=("Arial",12)).pack(pady=5)
task_entry = tk.Entry(root,width=40,font=("Arial",12))
task_entry.pack(pady=10)
listbox = tk.Listbox(root,width=40,height=10,font=("Arial",12))
listbox.pack(pady=10)



todo_list = []

#function to add task 
def add_task():
    task = task_entry.get()
    if task : 
        todo_list.append(task)
        listbox.insert(tk.END,task) #add task to the listbox
        task_entry.delete(0,tk.END) #clears entry box from 0 to end
    else :
        messagebox.showwarning("Warning","Task Cannot be Empty!")

#function to mark task as done
def mark_done():
        selection = listbox.curselection()
        if selection:
            selected_index = selection[0]
            listbox.delete(selected_index)
            todo_list.pop(selected_index)
        else :
            messagebox.showwarning("Warning","No Task Selected")

#function to delete task
def delete_task() :
    selection = listbox.curselection()
    if selection:
        selected_index = selection[0]
        listbox.delete(selected_index)
        todo_list.pop(selected_index)
    else :
        messagebox.showwarning("Warning","No Task Selected")


#function to exit
def exit_app() :
    root.destroy()
    #ui elements

button_frame = tk.Frame(root)
button_frame.pack(pady=10)
button_frame.config(bg="#2C3E50")

add_button = tk.Button(button_frame,text="Add Task",command=add_task,width=10,height=2,font=("Arial",10),
                       bg="green",fg="white",activebackground="#2980B9")
add_button.grid(row=0,column=0,padx=5)

done_button = tk.Button(button_frame,text="Mark As Done",command=mark_done,width=10,height=2,font=("Arial",10),
                       bg="green",fg="white",activebackground="#2980B9")
done_button.grid(row=0,column=1,padx=5)

delete_button = tk.Button(button_frame,text="Delete Task",command=delete_task,width=10,height=2,font=("Arial",10),
                       bg="green",fg="white",activebackground="#2980B9")
delete_button.grid(row=0,column=2,padx=5)

exit_button = tk.Button(button_frame,text="Exit",command=exit_app,width=10,height=2,font=("Arial",10),
                       bg="green",fg="white",activebackground="#2980B9")
exit_button.grid(row=0,column=3,padx=5)

root.mainloop()