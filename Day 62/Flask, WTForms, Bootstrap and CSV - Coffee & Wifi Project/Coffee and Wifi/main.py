from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, TimeField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location_URL = URLField(label="Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    open_time = StringField(label="Opening Time e.g. 8AM", validators=[DataRequired()])
    closing_time = StringField(label="Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField(label="Coffee Rating", validators=[DataRequired()],
                                choices=["✘", "☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"])
    wifi_rating = SelectField(label="Wifi Strength Rating", validators=[DataRequired()],
                              choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"])
    power_outlets_rating = SelectField(label="Power Socket Availability", validators=[DataRequired()],
                                       choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"])
    submit = SubmitField(label='Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add')
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="UTF-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = CafeForm()
    if add_form.validate_on_submit():
        cafe_name = add_form.cafe.data
        location = add_form.location_URL.data
        open_time = add_form.open_time.data
        close_time = add_form.closing_time.data
        coffe_rating = add_form.coffee_rating.data
        wifi_rating = add_form.wifi_rating.data
        power_rating = add_form.power_outlets_rating.data
        with open(file="cafe-data.csv", mode="a", encoding="UTF-8") as file:
            file.write(f"\n{cafe_name},{location},{open_time},{close_time},{coffe_rating},{wifi_rating},{power_rating}")
        if request.method == "POST":
            return render_template('success.html')
    return render_template('add.html', form=add_form)


if __name__ == '__main__':
    app.run(debug=True)
