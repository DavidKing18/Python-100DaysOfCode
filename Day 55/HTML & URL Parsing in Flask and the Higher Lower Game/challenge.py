from flask import Flask

app = Flask(__name__)


@app.route('/')  # Python Decorator
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
           "<p>This is a paragraph</p>" \
           "<img src='https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif' alt='kitten_gif' width='200px'>"


def make_bold(function):
    def wrapper_function():
        string = function()
        return f"<b>{string}</b>"
    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        string = function()
        return f"<em>{string}</em>"
    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        string = function()
        return f"<u>{string}</u>"
    return wrapper_function


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


@app.route('/username/<path:name>/<number>')
def greet(name, number):
    return f"Hello there, {name}, you're {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)