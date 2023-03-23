from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime

# Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
# print(posts)

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    with app.app_context():
        posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    with app.app_context():
        posts = BlogPost.query.all()
    requested_post = None
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post
            print(requested_post)
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/edit-post/<post_id>")
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm()
    post_id = request.args.get("post_id")
    return render_template("make-post.html", title="Edit Post", form=edit_form)


@app.route("/new-post", methods=["GET", "POST"])
def add_post():
    post_form = CreatePostForm()
    if post_form.validate_on_submit():
        today = datetime.now()
        with app.app_context():
            db.create_all()
            new_post = BlogPost(
                date=f"{today.strftime('%B')} {today.strftime('%d')}, {today.strftime('%Y')}",
                title=request.form.get("title"),
                subtitle=request.form.get('subtitle'),
                author=request.form.get("author"),
                img_url=request.form.get("img_url"),
                body=request.form.get("body")
            )
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=post_form, title="New Post")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
print("Refresh")