import functions
import time

print(time.strftime("%d-%m-%Y %H:%M:%S"))
while True:
    user_action = input("Type add, show, edit, complete or exit")
    user_action = user_action.strip()
    if "add" in user_action:
            todo = user_action[4:] + "\n"
            todos=functions.read_todos()
            todos.append(todo)
            functions.write_todos(todos)

    elif "show" in user_action:
            todos = functions.read_todos()
            if len(todos)==0:
                print("There is no work item in todos. Please add some todo first.")
                continue
            for index, item in enumerate(todos):
                row = f"{index+1} - {item}"
                print(row,end ="")

    elif "edit" in user_action:
        try:
            todos = functions.read_todos()
            if len(todos)==0:
                print("There is no work item in todos. Please add some todo first.")
                continue
            n=int(user_action[5:])
            todos[n-1]=input("Enter a todo: ") + "\n"
            functions.write_todos(todos)
        except :
            print("Your command is not valid. Kindly try again.")
            continue

    elif "complete" in user_action:
        try :
             todos = functions.read_todos()
             if len(todos) == 0:
                  print("There is no work item in todos. Please add some todo first.")
                  continue
             n = int(user_action[9:])
             del todos[n-1]
             functions.write_todos(todos)
        except :
            print("Your command is not valid. Kindly try again.")
            continue

    elif "exit" in user_action:
            break

    else :
        print("Please enter valid action.")

print("Bye!")
