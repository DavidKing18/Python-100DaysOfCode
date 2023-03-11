from flask import Flask, render_template, request
import requests
from smtplib import SMTP
import os

URL_ENDPOINT = "https://api.npoint.io/646db1feed8f58989f98"
BLOG_EMAIL = "cornflakeschicago@gmail.com"
PASSWORD = os.environ.get("CHICAGO_MAIL_PASSWORD")

response = requests.get(URL_ENDPOINT)
blog_posts = response.json()


def send_email(name, email, phone, message):
    with SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=BLOG_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=BLOG_EMAIL, to_addrs=email, msg=f"Subject: New Message\n\nName: {name}\nEmail: "
                                                                      f"{email}\nPhone: {phone}\nMessage: {message}")


app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html", posts=blog_posts)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        name = request.form["name"]
        email_address = request.form['email']
        phone = request.form["phone"]
        message = request.form["message"]
        print(f"{name}\n{email_address}\n{phone}\n{message}")
        send_email(name, email_address, phone, message)
        return render_template("contact.html", text="Successfully sent your message")
    return render_template("contact.html", text="Contact Me")


@app.route("/post/<int:index>")
def post_page(index):
    blog_post = blog_posts[index-1]
    return render_template("post.html", post=blog_post)


if __name__ == "__main__":
    app.run(debug=True)
