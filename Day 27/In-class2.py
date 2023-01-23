####################################################
#        Creating Windows and Labels with Tkinter
####################################################

from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

#  Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(expand=True)
my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button
def button_clicked():
    print("I got clicked")
    my_label.config(text=my_input.get())


button = Button(text="Click Me", command=button_clicked)
button.pack()


# Entry
my_input = Entry(width=10)
my_input.pack()
window.mainloop()
