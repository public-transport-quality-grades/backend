from typing import Dict
from flask import Flask, request, jsonify
from flasgger import APISpec, Swagger
from werkzeug.exceptions import NotFound, InternalServerError
from backend import initializer
from backend.schemas import AvailableGradingSchema
from backend.model.availablegrading import AvailableGrading
from backend import geojson_loader


OEVGK_ARE_PATH = 'data/Oev_Gueteklassen_ARE.json'

DATA_PATH = 'data'

app = Flask(__name__)

spec = APISpec(
    title='OeVGK18 Backend',
    version='1.0',
    plugins=[
        'apispec.ext.flask',
        'apispec.ext.marshmallow',
    ],
)


@app.route('/api/gradings', methods=['GET'])
def get_available_gradings():
    """
    Get all available gradings for a specific type of day (e.g. "Working Day", "Saturday", ...).
    ---
    parameters:
      - name: typeOfDay
        description: Type of day to filter for, e.g. Working Day, Saturday
        in: query
        type: string
        required: false
    responses:
        200:
            description: An available grading
            schema:
                $ref: '#/definitions/AvailableGrading'
    """
    type_of_day = request.args.get('typeOfDay')
    gradings = available_gradings.keys()
    if type_of_day:
        gradings = list(filter(lambda grading: grading.type_of_day == type_of_day, gradings))

    result_schema = AvailableGradingSchema(only=('id', 'due_date', 'type_of_day', 'time_interval'))

    result = list([result_schema.dump(grading).data for grading in gradings])
    return jsonify(result)


@app.route('/api/typesOfDays', methods=['GET'])
def get_available_days():
    """
       Get all types of days (working day, saturday, sunday, etc.) for which there are gradings
       ---
       responses:
           200:
               description: A list of types of days for which there are gradings
               schema:
                   type: array
                   items:
                     type: string
       """
    unique_days = set([grading.type_of_day for grading in available_gradings.keys()])

    return jsonify(list(unique_days))


@app.route('/api/gradings/<int:grading_id>', methods=['GET'])
def get_grading(grading_id: int):
    """
    file: yaml_schemas/grading.yml
    """
    if grading_id < 1 or grading_id > len(available_gradings):
        print("Erorr not found")
        print(len(available_gradings))
        raise NotFound("Grading not found")
    try:
        found_grading = list(filter(lambda g: g.id == grading_id, available_gradings.keys()))
        if not found_grading:
            raise InternalServerError(f"No grading with ID {grading_id} registered")
        geojson_data = geojson_loader.load_geojson(available_gradings[found_grading[0]])
        return jsonify(geojson_data)
    except ValueError as ex:
        print(ex)
        raise InternalServerError("GeoJSON could not be loaded")


@app.route('/api/oevkgARE', methods=['GET'])
def get_oevgk_are_data():
    """
    file: yaml_schemas/oevgkARE.yml
    """
    try:
        geojson_data = geojson_loader.load_geojson(OEVGK_ARE_PATH)
        geojson_data['features'].sort(key=lambda feature: feature['properties']['KLASSE'], reverse=True)
        return jsonify(geojson_data)
    except ValueError as ex:
        print(ex)
        raise InternalServerError("GeoJSON could not be loaded")


available_gradings: Dict[AvailableGrading, str] = initializer.load_available_gradings(DATA_PATH)

initializer.check_oevgk_are_data(OEVGK_ARE_PATH)

template = spec.to_flasgger(
    app,
    definitions=[AvailableGradingSchema],
    paths=[get_available_gradings, get_available_days, get_grading, get_oevgk_are_data]
)

swag = Swagger(app, template=template)

if __name__ == "__main__":
    app.run(debug=True)
