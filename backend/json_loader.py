from os import path
import json


def load_json(file_path: str) -> dict:
    if not path.exists(file_path):
        raise ValueError(f"Json file at {file_path} not found")
    with open(file_path, 'r') as fd:
        try:
            data = json.load(fd)
            return data
        except ValueError as ex:
            raise ex
