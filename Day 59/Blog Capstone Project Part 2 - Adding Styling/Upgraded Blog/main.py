from flask import Flask, render_template
import requests

URL_ENDPOINT = "https://api.npoint.io/646db1feed8f58989f98"

response = requests.get(URL_ENDPOINT)
blog_posts = response.json()

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html", posts=blog_posts)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def post_page(index):
    blog_post = blog_posts[index-1]
    return render_template("post.html", post=blog_post)


if __name__ == "__main__":
    app.run(debug=True)
