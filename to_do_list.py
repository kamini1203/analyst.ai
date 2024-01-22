import os
tasks=[]
def add_task(task):
    tasks.append(task)
def view_task():
    for task in tasks:
        print(tasks.index(task)+1,".",task)
def delete_task(task):
    for t in tasks:
        if t.lower()==task.lower():
            tasks.remove(t)
            break
    else:
        print("There is no any this type of task")
def mark_as_complete(task):
    for t in tasks:
        if t.lower()==task.lower():
            tasks[tasks.index(t)]="Mark as completed - "+tasks[tasks.index(t)]
            break
    else:
        print("There is any this type of task for mark as completed")

while True:
    print("1.Add Task","\n2.View Task","\n3.Delete Task","\n4.Mark Task As Completed","\n5.Exit")
    n=int(input("enter your choice:"))
    os.system('cls')
    if n==1:
        task=input("Enter a your task:")
        add_task(task)
    elif n==2:
        view_task()
    elif n==3:
        task=input("Enter task to delete:")
        delete_task(task)
    elif n==4:
        task=input('Enter a task wjhich you want to show mark as completed:')
        mark_as_complete(task)
    elif n==5:
        print("Goodbye!")
        break
    else:
        print("You enter invalid choice")