from tkinter import *
tasks = []
menu = """1) Add task
2) Show the tasks
3) Delete a task
4) Mark as Done
5) Mark as Undone
6) Modify a task
7) delete completed tasks
8) Show completed tasks
9) Show unfinished tasks
10) Exit"""

def add_task():
    task = task_entry.get()
    if len(task) == 0:
        print("can't enter an empty task")
        return
    else:
        task = task +" [ ]"
        tasks.append(task)
        tasks_list.insert(END, task)
        task_entry.delete(0, END)
        update_file()
        print("---------Task added!!!!------")
def delete_task():
    if tasks_list.size() ==0:
        print("The list is empty")
        return
    else:
        selected = tasks_list.curselection()
        if len(selected)==0:
            print("please select a task")
        else :
            index = selected[0]
            tasks.pop(index)
            tasks_list.delete(index)
            update_file()
            print("---------Task removed!!!!------")
def mark_as_done():
    if tasks_list.size()==0:
        print("The list is empty")
        return
    else:
        selected = tasks_list.curselection()
        if len(selected)==0:
            print("please select a task")
        else:
            index = selected[0]
            if "[x]" in tasks[index]:
                print("the task is already done")
                return

            tasks[index]=tasks[index].replace("[ ]", "[x]",1)
            tasks_list.delete(index)
            tasks_list.insert(index, tasks[index])
            update_file()
            print("---------Task Marked as done!!!!------")
def mark_as_undone():
    if tasks_list.size()==0:
        print("The list is empty")
        return
    else:
        selected = tasks_list.curselection()
        if not selected:
            print("please select a task")
        else:
            index = selected[0]
            if "[ ]" in tasks[index]:
                print("the task is already undone")
                return
            tasks[index]=tasks[index].replace("[x]", "[ ]",1)
            tasks_list.delete(index)
            tasks_list.insert(index, tasks[index])
            update_file()
            print("---------Task Marked as undone!!!!------")
def clear_completed_tasks():
    global tasks
    if tasks_list.size()==0:
        print("No tasks to clean")
    else:
        co_tasks = []
        for task in tasks:
            if "[ ]" in task:
                co_tasks.append(task)
        if len(tasks)==len(co_tasks):
            print("No completed tasks were found")
        else:
            tasks_list.delete(0,END)
            tasks = co_tasks
            for task in tasks:
                tasks_list.insert(END, task)
            print("---------Completed Tasks Cleaned!!!!------")
            update_file()
def show_completed_tasks():
    if len(tasks)==0:
        print("No completed tasks were found")
        return
    else:
        tasks_list.delete(0, END)
        for task in tasks:
            if "[x]" in task:
                tasks_list.insert(END, task)
def show_unfinished_tasks():
    if len(tasks) == 0:
        print("No Uncompleted tasks were found")
        return
    else:
        tasks_list.delete(0, END)
        for task in tasks:
            if "[ ]" in task:
                tasks_list.insert(END, task)
def load_tasks():
    file = open("TodoList.txt", "r")
    for i in file:
        tasks.append(i.strip())
    if not tasks:
        print("No tasks yet")
    else:
        for task in tasks:
            tasks_list.insert(END, task)
def update_file():
    file = open("TodoList.txt", "w")
    for i in range(len(tasks)):
        file.write(tasks[i]+"\n")
def show_all_tasks():
    if len(tasks)==0:
        print("No tasks yet")
        return
    else:
        tasks_list.delete(0, END)
        for task in tasks:
            tasks_list.insert(END, task)


todo = Tk()
todo.title("Todo-List")
todo.configure(background="#1e1e1e")

to_frame=Frame(todo)
task_entry= Entry(to_frame,bg="#2b2b2b",fg="white",width=50)
task_entry.pack(side="left")
add_button= Button(to_frame,text="Save",font=("Arial",10,"bold"),bg="#4CAF50",fg="black",width=10,height=1,command=add_task)
add_button.pack(side="left",padx=0)
to_frame.pack()

top_frame=Frame(todo)
delete_button = Button(top_frame,text="Delete",font=("Arial",10,"bold"),bg="#e74c3c",fg="black",command=delete_task)
delete_button.pack(side="left",padx=0)
done_button=Button(top_frame,text="Mark as Done",font=("Arial",10,"bold"),bg="#3498db",fg="black",command=mark_as_done)
done_button.pack(side="left",padx=0)
undone_button = Button(top_frame,text="Mark as UnDone",font=("Arial",10,"bold"),bg="#f39c12",fg="black",command=mark_as_undone)
undone_button.pack(side="left",padx=0)
top_frame.pack()

bottom_frame = Frame(todo)
tasks_list = Listbox(todo,bg="#2b2b2b",fg="white",width=50,height=20)
tasks_list.pack()
clear_tasks_button = Button(bottom_frame,text="Clear Completed Tasks",font=("Arial",10,"bold"),bg="#9b59b6",fg="black",command=clear_completed_tasks)
clear_tasks_button.pack(side="left",padx=0)
show_completed_button=Button(bottom_frame,text="Show completed ",font=("Arial",10,"bold"),bg="#9b59b6",fg="black",command=show_completed_tasks)
show_completed_button.pack(side="left",padx=0)
show_uncompleted_button=Button(bottom_frame,text="Show Uncompleted ",font=("Arial",10,"bold"),bg="#9b59b6",fg="black",command=show_unfinished_tasks)
show_uncompleted_button.pack(side="left",padx=0)
show_all = Button(bottom_frame,text="Show All ",font=("Arial",10,"bold"),bg="#9b59b6",fg="black",command=show_all_tasks)
show_all.pack(side="left",padx=0)
bottom_frame.pack()
load_tasks()
todo.mainloop()
"""
first of all Thanks to allah 
after that iam really happy cause this is the first real project that i created , it was hard cause i had to combine between GUI and python coding
if you run this code i am sorry about the colors , i am really bad at picking them 
i created this project with the help of ChatGpt , it didn't give me code , it just helped me with logic

"""