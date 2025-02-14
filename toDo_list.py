tasks = []
def view_task():
    if(len(tasks)==0):
        print("there is no task in list\n")
    else:
        print("\nYour To-Do list:")
        for idx,task in enumerate(tasks,start=1):
            print(f"{idx}. {task}")
        print()    
def add_task():
    task = input("enter your task: ").strip()
    if task:
        tasks.append(task) 
        print("task added succesfully\n")
    else:
        print("task can't be empty\n")
def complete_task():
    view_task()
    try:
        task_num  = int(input("enter the number of task that is completed\n"))  
        if(1<=task_num<=len(tasks)):
                complete_task =tasks.pop(task_num-1) 
                print(f"task '{complete_task}' is completed sucessfully")
        else:
                print("invalid number of task")
    except ValueError:
            print("enter valid number of task")
def delete_task():
     view_task()
     try:
        task_num  = int(input("enter the number of task that you want to delete"))     
        if(1<=task_num<=len(tasks)):
                delete_task =tasks.pop(task_num-1) 
                print(f"task '{delete_task}' is deleted sucessfully\n")
        else:
                print("invalid number of task\n")
     except ValueError:
            print("enter valid number of task\n")
def main():
    while True:
        print("\ntask menu")
        print("************")
        print("1 : add task") 
        print("2 : delete task") 
        print("3 : complete task")
        print("4 :view task") 
        print("5 : exit list")
        num = int(input("enter your choice number from 1 to 4: ")) 
        if(num == 1):
            add_task()
        elif(num == 2):
            delete_task()
        elif(num == 3):
            complete_task()
        elif(num == 4):
            view_task() 
        elif(num == 5):
            print("exit from list")
            break    
        else:
            print("please enter valid number")
if __name__ == "__main__":
    main()                
              
           
                                  
    
                