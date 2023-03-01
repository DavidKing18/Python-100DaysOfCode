######################################################
#       Create your First Web Server with Flask
######################################################

from flask import Flask

app = Flask(__name__)


@app.route('/')  # Python Decorator
def hello_world():
    return "Hello, World!"
#  Functions are first-class objects, and can be passed as arguments e.g. int/string/float e.t.c.
#  Functions can be nested


if __name__ == "__main__":
    app.run()
