from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)
GENDERIZE_URL = "https://api.genderize.io?"
AGIFY_URL = "https://api.agify.io?"


@app.route("/")
def home():
    current_year = datetime.now().year
    return render_template("index.html", year=current_year)


@app.route("/guess/<user_name>")
def guess(person_name):
    parameters = {
        "name": person_name
    }
    gender_response = requests.get(GENDERIZE_URL, params=parameters)
    gender_data = gender_response.json()
    age_response = requests.get(AGIFY_URL, params=parameters)
    age_data = age_response.json()
    person_gender = gender_data['gender']
    person_age = age_data['age']
    return render_template("guess.html", name=person_name.title(), gender=person_gender, age=person_age)


if __name__ == "__main__":
    app.run(debug=True)
