from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_posts = blog_response.json()


@app.route('/')
def home():
    print(all_posts)
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:index>')
def get_post(index):
    return render_template("post.html", post=all_posts[index-1])


if __name__ == "__main__":
    app.run(debug=True)
