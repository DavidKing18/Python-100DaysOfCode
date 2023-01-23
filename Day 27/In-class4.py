from tkinter import *


def button_clicked():
    print("I got clicked")
    my_label.config(text=user_input.get())


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="Some Text", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

# Buttons
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
button.config(padx=5, pady=5)


new_button = Button(text="Click Me Instead", command=button_clicked)
new_button.grid(column=2, row=0)
new_button.config(padx=5, pady=5)

# Entry
user_input = Entry(width=10)
user_input.grid(column=3, row=2)
print(user_input.get())

window.mainloop()
