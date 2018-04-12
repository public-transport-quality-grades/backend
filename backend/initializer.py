from datetime import datetime
from model.availablerating import AvailableRating, TimeInterval


# TODO import from some config file
available_ratings = [
    {
        'dueDate': '2018-04-12',
        'typeOfDay': 'Wochentag',
        'timeIntervalDescription': 'Tag',
        'start_time': '08:00',
        'end_time': '20:00',
        'pathToGeoJson': '/home/robin/osm/oevgk18_wochentag_tag.json'
    },
    {
        'dueDate': '2018-04-14',
        'typeOfDay': 'Samstag',
        'timeIntervalDescription': 'Abend',
        'start_time': '20:00',
        'end_time': '00:00',
        'pathToGeoJson': '/home/robin/osm/oevgk18_samstag_abend.json'
    }
]


def create_available_rating(id_: int, rating: dict):
    day = datetime.strptime(rating['dueDate'], '%Y-%m-%d')
    time_interval = TimeInterval(rating['timeIntervalDescription'], rating['start_time'], rating['end_time'])
    return AvailableRating(id_, day, rating['typeOfDay'], time_interval, rating['pathToGeoJson'])


def load_available_ratings() -> list:
    numbered_ratings = zip(range(len(available_ratings)), available_ratings)
    ratings = map(lambda r: create_available_rating(r[0], r[1]), numbered_ratings)
    return list(ratings)
