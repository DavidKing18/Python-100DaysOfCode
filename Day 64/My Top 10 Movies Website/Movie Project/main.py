from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies-chart.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

MOVIE_DB_API_KEY = os.environ.get("MOVIE_DB_API_KEY")
URL = "https://api.themoviedb.org/3"
MOVIE_DB_IMAGE_UR = "https://image.tmdb.org/t/p/w500/"


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.String(4), unique=False, nullable=False)
    description = db.Column(db.String(1000), unique=False, nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(1000))
    img_url = db.Column(db.String(250), unique=False, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


class RateMovieForm(FlaskForm):
    rating = FloatField(label="Your Rating Out of 10 e.g. 7.5", validators=[DataRequired(), NumberRange(min=1, max=10)])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


class AddMovieForm(FlaskForm):
    movie = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


def sort_key(movies):
    if movies is not []:
        return movies.rating
    else:
        return movies.rating


def sort_movies(movies):
    if movies is not None:
        number_of_movies = len(movies)
        for movie in movies:
            movie = Movie.query.get(movie.id)
            movie.ranking = number_of_movies
            db.session.commit()
            number_of_movies -= 1
        return movies
    else:
        return []


@app.route("/")
def home():
    movies = db.session.query(Movie).all()
    movies.sort(key=sort_key, reverse=True)
    return render_template("index.html", movies=sort_movies(movies))

#       OR

# @app.route("/")
# def home():
#     movies = db.session.query(Movie).order_by(Movie.id).all()
#     return render_template("index.html", movies=sort_movies(movies))


@app.route("/edit", methods=["GET", "POST"])
def edit():
    movie_id = request.args.get('id')
    movie_to_edit = Movie.query.get(movie_id)
    rate_movie_form = RateMovieForm()
    if rate_movie_form.validate_on_submit():
        new_rating = rate_movie_form.rating.data
        new_review = rate_movie_form.review.data
        movie = Movie.query.get(movie_id)
        movie.rating = new_rating
        movie.review = new_review
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie_to_edit, form=rate_movie_form)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    add_movie_form = AddMovieForm()
    if add_movie_form.validate_on_submit():
        movie_title = add_movie_form.movie.data
        parameters = {
            'api_key': MOVIE_DB_API_KEY,
            'query': movie_title
        }
        data = requests.get(url=f"{URL}/search/movie", params=parameters).json()
        print(data)
        return render_template("select.html", options=data['results'])
    return render_template("add.html", form=add_movie_form)


@app.route("/movie_details", )
def movie_details():
    movie_id = request.args.get('id')
    data = requests.get(url=f"{URL}/movie/{movie_id}", params={'api_key': MOVIE_DB_API_KEY}).json()
    print(data)
    movie_title = data['title']
    move_img_path = data['poster_path']
    movie_year = data['release_date'][:4]
    movie_description = data['overview']
    with app.app_context():
        db.create_all()
        new_movie = Movie(
            title=movie_title,
            year=movie_year,
            description=movie_description,
            img_url=f"{MOVIE_DB_IMAGE_UR}{move_img_path}"
        )
        db.session.add(new_movie)
        db.session.commit()
        movie = Movie.query.filter_by(title=movie_title).first()
    return redirect(url_for('edit', id=movie.id))


if __name__ == '__main__':
    app.run(debug=True)
