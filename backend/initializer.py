from typing import List
from datetime import datetime
from os.path import splitext, basename
from .model.availablegrading import AvailableGrading
from . import geojson_loader, json_loader


def load_available_gradings(oevgk18_metadata_path) -> List[AvailableGrading]:
    oevgk18_metadata = json_loader.load_json(oevgk18_metadata_path)
    available_gradings = []
    for generated_grading in oevgk18_metadata['generated-gradings']:
        available_gradings.append(_parse_grading_data(generated_grading))
    return available_gradings


def check_oevgk_are_data(path):
    try:
        geojson_loader.load_geojson(path)
    except ValueError:
        print(f"WARNING: Gradings from ARE not found or invalid, path {path}")


def _parse_grading_data(generated_grading: dict) -> AvailableGrading:
    time_interval = {
        'time_description': generated_grading['type-of-interval'],
        'start': datetime.strptime(generated_grading['lower-bound'], '%H:%M').time(),
        'end': datetime.strptime(generated_grading['upper-bound'], '%H:%M').time()
    }

    grading = {
        'id': generated_grading['id'],
        'due_date': datetime.strptime(generated_grading['due-date'], '%Y-%m-%dT%H:%M:%S').date,
        'type_of_day': generated_grading['type-of-day'],
        'tile_name': _parse_tile_name_out_of_geojson_path(generated_grading['filename']),
        'time_interval': time_interval
    }
    return AvailableGrading(**grading)


def _parse_tile_name_out_of_geojson_path(geojson_path: str) -> str:
    filename_w_ext = basename(geojson_path)
    return splitext(filename_w_ext)[0]
