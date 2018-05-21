from typing import Dict, List
from datetime import datetime
from os import listdir
from os.path import isfile, join, splitext
from .model.availablegrading import AvailableGrading
from . import geojson_loader


def load_available_gradings(data_folder: str) -> Dict[AvailableGrading, str]:
    geojson_paths = _get_geojson_paths(data_folder)
    numbered_geojson_paths = zip(range(1, len(geojson_paths) + 1), geojson_paths)
    return {_load_grading_from_geojson(*numbered_file): numbered_file[1] for numbered_file in numbered_geojson_paths}


def check_oevgk_are_data(path):
    try:
        geojson_loader.load_geojson(path)
    except ValueError:
        print(f"WARNING: Gradings from ARE not found or invalid, path {path}")


def _get_geojson_paths(data_folder: str) -> List[str]:
    all_files = [f for f in listdir(data_folder) if isfile(join(data_folder, f))]
    geojson_files = filter(_is_oevgk18_file, all_files)
    return list(map(lambda filename: join(data_folder, filename), geojson_files))


def _is_oevgk18_file(file_path: str) -> bool:
    file_name, file_ext = splitext(file_path)
    if not (file_ext == '.json' or file_ext == '.geojson'):
        return False
    return file_name.startswith('oevgk18')


def _load_grading_from_geojson(identifier: int, geojson_path: str) -> AvailableGrading:
    grading_data = geojson_loader.load_geojson(geojson_path)
    time_interval = {
        'time_description': _get_grading_attribute(geojson_path, grading_data, 'type-of-interval'),
        'start': datetime.strptime(_get_grading_attribute(geojson_path, grading_data, 'lower-bound'), '%H:%M').time(),
        'end': datetime.strptime(_get_grading_attribute(geojson_path, grading_data, 'upper-bound'), '%H:%M').time()
    }

    due_datetime = datetime.strptime(
        _get_grading_attribute(geojson_path, grading_data, 'due-date'), '%Y-%m-%dT%H:%M:%S')
    grading = {
        'id': identifier,
        'due_date': due_datetime.date,
        'type_of_day': _get_grading_attribute(geojson_path, grading_data, 'type-of-day'),
        'time_interval': time_interval,
    }

    return AvailableGrading(**grading)


def _get_grading_attribute(filename: str, grading_data: dict, attribute: str) -> str:
    if attribute not in grading_data:
        raise AttributeError(f"Attribute {attribute} not found in OeVGK18 file {filename}")
    return grading_data[attribute]