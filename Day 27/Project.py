####################################################
#   MILES TO KILOMETERS CONVERTER USING TKINTER
####################################################

from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=20, pady=20)


is_equal_label = Label(text="is equal to", font=("New Times Roman", 16, "normal"))
is_equal_label.grid(column=0, row=1)

miles_label = Label(text="Miles", font=("New Times Roman", 16, "normal"))
miles_label.grid(column=2, row=0)

kilometer_result_label = Label(text="", font=("New Times Roman", 16, "bold"))
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km", font=("New Times Roman", 16, "normal"))
kilometer_label.grid(column=2, row=1)


def miles_to_km():
    miles = int(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text="{:.2f}".format(km))


calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)
window.mainloop()
