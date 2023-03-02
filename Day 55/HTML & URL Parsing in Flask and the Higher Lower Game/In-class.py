from flask import Flask

app = Flask(__name__)


@app.route('/')  # Python Decorator
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
           "<p>This is a paragraph</p>" \
           "<img src='https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif' alt='kitten_gif' width='200px'>"


@app.route('/bye')
def bye():
    return "Bye!"


@app.route('/username/<path:name>/<number>')
def greet(name, number):
    return f"Hello there, {name}, you're {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)


####################################################
#       Advanced Python Decorator Functions
####################################################
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)
