from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


with app.app_context():
    all_books = db.session.query(Book).all()


@app.route('/', methods=["GET", "POST"])
def home():
    if request.args.get('type') == 'edit':
        book_to_update = Book.query.get(request.args.get('id'))
        book_to_update.rating = float(request.form.get("rating"))
        db.session.commit()
        return redirect(location=url_for("home"))
    elif request.args.get('type') == 'del':
        book_to_delete = Book.query.get(request.args.get('id'))
        db.session.delete(book_to_delete)
        db.session.commit()
        return redirect(location=url_for("home"))
    return render_template("index.html", books=db.session.query(Book).all())


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book_title = request.form.get("title")
        book_author = request.form.get("author")
        book_rating = request.form.get("rating")
        with app.app_context():
            db.create_all()
            first_book = Book(title=book_title, author=book_author, rating=book_rating)
            db.session.add(first_book)
            db.session.commit()
        return redirect(location=url_for('home'))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    book_number = request.args.get('id')
    book_to_edit = None
    for book in db.session.query(Book).all():
        if book.id == int(book_number):
            book_to_edit = book
    return render_template('edit.html', book=book_to_edit)


if __name__ == "__main__":
    app.run(debug=True)
