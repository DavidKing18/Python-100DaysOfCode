from flask import Flask
from random import randint

app = Flask(__name__)
random_number = randint(0, 9)
print(random_number)


@app.route('/')
def homepage():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='gif'>"


@app.route('/<int:choice>')
def check_choice(choice):
    if choice > random_number:
        return "<h1 style='color:purple'>Too high, try again!👀</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' alt='gif'>"
    elif choice < random_number:
        return "<h1 style='color:red'>Too low, try again!</h1>😏" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' alt='gif'>"
    else:
        return "<h1 style='color:green'>You found me!🎉</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt='gif'>"


@app.route('/<string:char>')
def error_message(char):
    return f"<h1 style='text-align:center'>'{char}' is not a number. Try again!🥴</h1>"


if __name__ == "__main__":
    app.run(debug=True)
