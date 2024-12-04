import functions

import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do: ")
input_box = sg.InputText(tooltip="Enter todo", key = "todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values = functions.read_todos(), key = "todos",
                      enable_events = True, size = (45, 10))
edit_button = sg.Button("Edit")

complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout = [[label,input_box,add_button],
                             [list_box, edit_button,complete_button],
                             [exit_button]],
                   font = ('Helvetica',10))
while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.read_todos()
            new_todo = values.get("todo") + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case "Edit":
            try:
                todos = functions.read_todos()
                item_index = todos.index(values.get("todos")[0])
                todos[item_index] = values.get("todo") + "\n"
                functions.write_todos(todos)
                window['todos'].update(values = todos)
            except IndexError:
                sg.popup("Please enter a todo first.")
                continue


        case "todos":
            try:
               todo = values.get("todos")[0]
               window['todo'].update(value = todo)
            except IndexError:
                sg.popup("Please enter a todo first.")
                continue


        case "Complete":
            try:
             todos = functions.read_todos()
             item_index = todos.index(values.get("todos")[0])
             del todos[item_index]
             functions.write_todos(todos)
             window['todos'].update(values=todos)
             window['todo'].update(value='')
            except IndexError:
                sg.popup("Please enter a todo first.")
                continue

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break

window.close()