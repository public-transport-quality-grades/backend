from flask import Flask, jsonify, request
from werkzeug.exceptions import NotFound, InternalServerError
from backend import geojson_loader
from backend import initializer


app = Flask(__name__)


@app.route('/api/availableRatings', methods=['GET'])
def get_available_ratings():
    type_of_day = request.args.get('typeOfDay')
    ratings = list(available_ratings)
    if type_of_day:
        ratings = list(filter(lambda rating: rating.type_of_day == type_of_day, ratings))

    return jsonify([r.serialize() for r in ratings])


@app.route('/api/availableDays', methods=['GET'])
def get_available_days():
    unique_days = set([rating.type_of_day for rating in available_ratings])
    return jsonify({'days':list(unique_days)})


@app.route('/api/rating/<int:rating_id>', methods=['GET'])
def get_rating(rating_id: int):
    if rating_id < 0 or rating_id >= len(available_ratings):
        raise NotFound("Rating not found")
    try:
        geojson_data = geojson_loader.load_geojson(available_ratings[rating_id].data_path)
        return jsonify(geojson_data)
    except ValueError as ex:
        print(ex)
        raise InternalServerError("GeoJSON could not be loaded")


available_ratings = initializer.load_available_ratings()

if __name__ == "__main__":
    app.run(debug=True)
