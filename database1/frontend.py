from tkinter import *
import backend

def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in backend.search(titleText.get(), authorText.get()):
        list1.insert(END, row)

def add_command():
    backend.insert(titleText.get(), authorText.get())
    list1.delete(0, END)
    list1.insert(END, (titleText.get(), authorText.get()))

def get_selected_row(event):
    try:
        global selected_row
        index = list1.curselection()[0]
        selected_row = list1.get(index)
        e1.delete(0,END)
        e1.insert(END, selected_row[1])
        e2.delete(0,END)
        e2.insert(END, selected_row[2])
    except IndexError:
        pass

def update_command():
    backend.update(selected_row[0], titleText.get(), authorText.get())

def delete_command():
    backend.delete(selected_row[0])

window = Tk()

window.wm_title("Bookstore Database")

l1 = Label(window, text = "Title")
l1.grid(row = 0, column = 0)

titleText = StringVar()
e1 = Entry(window, textvariable = titleText, width = 16)
e1.grid(row = 0, column = 1)

l2 = Label(window, text = "Author")
l2.grid(row = 0, column = 2)

authorText = StringVar()
e2 = Entry(window, textvariable = authorText, width = 16)
e2.grid(row = 0, column = 3)

list1 = Listbox(window, height =9, width = 28)
list1.grid(row = 1, column = 0, rowspan = 7, columnspan = 2)

list1.bind('<<ListboxSelect>>',get_selected_row)

sb1 = Scrollbar(window)
sb1.grid(row = 1, column = 2, rowspan = 7)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)


b1 = Button(window, text = "View all", width = 12, command = view_command)
b1.grid(row = 1, column = 3)

b2 = Button(window, text = "Search entry", width = 12, command = search_command)
b2.grid(row = 2, column = 3)

b3 = Button(window, text = "Add entry", width = 12, command = add_command)
b3.grid(row = 3, column = 3)

b4 = Button(window, text = "Update selected", width = 12, command = update_command)
b4.grid(row = 4, column = 3)

b5 = Button(window, text = "Delete selected", width = 12, command = delete_command)
b5.grid(row = 5, column = 3)

b6 = Button(window, text = "Close", width = 12, command = window.destroy)
b6.grid(row = 6, column = 3)

window.mainloop()
