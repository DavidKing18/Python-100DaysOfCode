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


@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
