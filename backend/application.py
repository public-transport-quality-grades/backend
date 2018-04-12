from flask import Flask, jsonify
from datetime import datetime
from model.availablerating import AvailableRating, TimeInterval
import initializer

app = Flask(__name__)

available_ratings = list()


@app.route('/api/availableratings', methods=['GET'])
def get_available_ratings():
    return jsonify([r.serialize() for r in available_ratings])


@app.route('/api/rating/<int:rating_id>', methods=['GET'])
def get_rating(rating_id: int):
    # TODO get geojson
    return jsonify(available_ratings[rating_id].serialize())


if __name__ == "__main__":
    available_ratings = initializer.load_available_ratings()
    app.run(debug=True)
