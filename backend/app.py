from typing import List

from flasgger import APISpec, Swagger
from flask import Flask, request, jsonify
from werkzeug.exceptions import NotFound, BadRequest

from backend import initializer
from backend.model.availablegrading import AvailableGrading
from backend.schemas import AvailableGradingSchema

OEVGK18_METADATA_PATH = 'data/oevgk18_metadata.json'

app = Flask(__name__)

spec = APISpec(
    title='OeVGK18 Backend',
    version='1.0',
    plugins=[
        'apispec.ext.flask',
        'apispec.ext.marshmallow',
    ],
)


@app.route('/api/typesOfDays', methods=['GET'])
def get_available_days():
    """
    file: api_schemas/typesOfDays.yml
    """
    unique_days = set([grading.type_of_day for grading in available_gradings])

    return jsonify({'days': list(unique_days)})


@app.route('/api/gradings', methods=['GET'])
def get_available_gradings():
    """
    file: api_schemas/available_gradings.yml
    """
    type_of_day = request.args.get('typeOfDay')
    if not type_of_day:
        raise BadRequest("Missing parameter typeOfDay")

    gradings = list(filter(lambda grading: grading.type_of_day == type_of_day, available_gradings))
    if not gradings:
        raise NotFound("No gradings for this type of day found")

    result_schema = AvailableGradingSchema(only=('id', 'due_date', 'type_of_day', 'tile_name', 'time_interval'))

    result = list([result_schema.dump(grading).data for grading in gradings])
    return jsonify(result)


available_gradings: List[AvailableGrading] = initializer.load_available_gradings(OEVGK18_METADATA_PATH)

template = spec.to_flasgger(
    app,
    definitions=[AvailableGradingSchema],
    paths=[get_available_gradings, get_available_days]
)

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/api/apispec.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/apidocs/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}

swag = Swagger(app, template=template, config=swagger_config)

if __name__ == "__main__":
    app.run(debug=True)
