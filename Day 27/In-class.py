####################################################
#        Creating Windows and Labels with Tkinter
####################################################

import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

#  Label

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="left", expand=True)

window.mainloop()


########################################################################################
#       Setting Default Values for Optional Arguments inside a Function Header
########################################################################################
# basically, functions with default values

import turtle

tim = turtle.Turtle()
tim.write("Some Text", font=("New Times Roman", 88, "bold"))
screen = turtle.Screen()
screen.exitonclick()


####################################################
#        *args: Many Positional Arguments
####################################################

def add(*args):

    total_sum = 0
    for num in args:
        total_sum += num
    return total_sum
    # OR ---- return sum(args)


print(add(2, 3, 4, 5, 6, 7))


####################################################
#        **kwargs: Many Keyword Arguments
####################################################

def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    sum_ = n + kwargs.get('add')
    product = n * kwargs.get('multiply')
    print(sum_)
    print(product)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.color = kw.get('color')
        self.seats = kw.get('seats')


my_car = Car(make='Nissan')
print(my_car.model)

