from .model.availablerating import AvailableRating
from . import geojson_loader


# TODO import from some config file
available_ratings = [
    {
        'dueDate': '2018-11-13',
        'typeOfDay': 'Working Day',
        'timeIntervalDescription': 'Day',
        'start_time': '06:00',
        'end_time': '20:00',
        'pathToGeoJson': 'data/oevgk18_2018-11-13_Day.json'
    },
    {
        'dueDate': '2018-11-13',
        'typeOfDay': 'Working Day',
        'timeIntervalDescription': 'Evening',
        'start_time': '20:00',
        'end_time': '00:00',
        'pathToGeoJson': 'data/oevgk18_2018-11-13_Evening.json'
    },
    {
        'dueDate': '2018-11-10',
        'typeOfDay': 'Saturday',
        'timeIntervalDescription': 'Day',
        'start_time': '06:00',
        'end_time': '20:00',
        'pathToGeoJson': 'data/oevgk18_2018-11-10_Day.json'
    },
    {
        'dueDate': '2018-11-10',
        'typeOfDay': 'Saturday',
        'timeIntervalDescription': 'Night',
        'start_time': '01:00',
        'end_time': '04:00',
        'pathToGeoJson': 'data/oevgk18_2018-11-10_Night.json'
    },
    {
        'dueDate': '2018-11-18',
        'typeOfDay': 'Sunday',
        'timeIntervalDescription': 'Day',
        'start_time': '06:00',
        'end_time': '20:00',
        'pathToGeoJson': 'data/oevgk18_2018-11-18_Day.json'
    },

    {
        'dueDate': '2018-11-18',
        'typeOfDay': 'Sunday',
        'timeIntervalDescription': 'Night',
        'start_time': '01:00',
        'end_time': '04:00',
        'pathToGeoJson': 'data/oevgk18_2018-11-18_Night.json'
    }
]


def load_available_ratings() -> list:
    numbered_ratings = zip(range(len(available_ratings)), available_ratings)
    ratings = map(lambda rating: AvailableRating.create_from_config(*rating), numbered_ratings)
    return list(ratings)


def check_oevgk_are_data(path):
    try:
        geojson_loader.load_geojson(path)
    except ValueError:
        print(f"WARNING: Ratings from ARE not found or invalid, path {path}")
