from os import path
import geojson


def load_geojson(file_path: str) -> dict:
    if not path.exists(file_path):
        raise ValueError(f"GeoJson file at {file_path} not found")
    with open(file_path, 'r') as fd:
        try:
            geojson_data = geojson.load(fd)
            return geojson_data
        except ValueError as ex:
            # TODO handle exception when geojson is invalid
            raise ex
