from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

VALID_EMAIL = "admin@email.com"
VALID_PASSWORD = "12345678"


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email(message="Invalid email address")])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8, message="Field must be at "
                                                                                                 "least 8 characters "
                                                                                                 "long.")])
    submit = SubmitField(label="Log In")


def create_app():
    application = Flask(__name__)
    Bootstrap(application)

    return application


app = create_app()
app.secret_key = "You-want-my-secret-key-for-what?"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == VALID_EMAIL and login_form.password.data == VALID_PASSWORD:
            return render_template("success.html")
        else:
            return render_template('denied.html')
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
