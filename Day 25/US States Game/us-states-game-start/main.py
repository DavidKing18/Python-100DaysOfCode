import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=725, height=491)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

correct_guesses = []
total_states = 50

data = pandas.read_csv("50_states.csv")
all_states = data.state
states_list = all_states.to_list()


def write_onto_map(state):
    state_data = data[data.state == state]
    x_coordinate = int(state_data["x"])
    y_coordinate = int(state_data["y"])
    writer.goto(x_coordinate, y_coordinate)
    writer.write(answer_state, True, align="center", font=("Courier", 8, "normal"))


while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/{total_states} States Correct",
                                    prompt="What's the state?").title()
    if (answer_state in states_list) and (answer_state not in correct_guesses):
        write_onto_map(answer_state)
        correct_guesses.append(answer_state)
    elif answer_state == "Exit":
        if len(correct_guesses) != 50:
            missing_states = list(set(states_list) - set(correct_guesses))
            data = pandas.DataFrame(missing_states)
            data.to_csv("states_to_learn.csv")
        break

# states_to_learn.csv michigan


# def get_onclick_coordinate(x, y):
#     print(x, y)
#
#
# screen.onscreenclick(get_onclick_coordinate)

turtle.mainloop()
