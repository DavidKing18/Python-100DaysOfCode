from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORRECT_API_KEY = "TopSecretAPIKey"


# Café TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=True)
    img_url = db.Column(db.String(500), nullable=True)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=True)
    has_wifi = db.Column(db.Boolean, nullable=True)
    has_sockets = db.Column(db.Boolean, nullable=True)
    can_take_calls = db.Column(db.Boolean, nullable=True)
    coffee_price = db.Column(db.String(250), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def random():
    cafe_database = db.session.query(Cafe).all()
    random_cafe = choice(cafe_database)
    return jsonify(cafe={
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
        "has_sockets": random_cafe.has_sockets,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "id": random_cafe.id,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "map_url": random_cafe.map_url,
        "name": random_cafe.name,
        "seats": random_cafe.seats
    })


@app.route("/all")
def all_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route("/search")
def search_cafe():
    query_location = request.args.get("loc")
    cafes = Cafe.query.filter_by(location=query_location).all()
    if cafes is None or cafes == []:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})
    else:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add():
    with app.app_context():
        db.create_all()
        new_cafe = Cafe(id=request.args.get("id"),
                        name=request.args.get("name"),
                        map_url=request.args.get("map_url"),
                        img_url=request.args.get("img_url"),
                        location=request.args.get("loc"),
                        seats=request.args.get("seats"),
                        has_toilet=bool(request.args.get("has_toilet")),
                        has_wifi=bool(request.args.get("has_wifi")),
                        has_sockets=bool(request.args.get("has_sockets")),
                        can_take_calls=bool(request.args.get("calls")),
                        coffee_price=request.args.get("coffee_price"))
        db.session.add(new_cafe)
        db.session.commit()
    return jsonify(response={"Success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=["GET", "POST", "PATCH"])
def update_price(cafe_id):
    new_price = request.args.get('new_price')
    cafe_to_update = Cafe.query.get(cafe_id)
    try:
        cafe_to_update.coffee_price = new_price
    except AttributeError:
        # 404 -> NOT FOUND
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        db.session.commit()
        # 200 -> OK
        return jsonify(success="Successfully updated the price."), 200


# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["GET", "DELETE"])
def remove_cafe(cafe_id):
    user_key = request.args.get("api_key")
    cafe_to_delete = Cafe.query.get(cafe_id)
    if cafe_to_delete is not None:
        if user_key == CORRECT_API_KEY:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(success="Successfully removed cafe"), 200
        elif user_key is None:
            return jsonify(error="Sorry,no API Key found."), 403
        else:
            return jsonify(error="Sorry, that's not allowed. Make sure you have the correct API Key."), 403
    else:
        return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found in the database."}), 404


if __name__ == '__main__':
    app.run(debug=True)
