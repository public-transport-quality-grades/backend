from .model.availablerating import AvailableRating


# TODO import from some config file
available_ratings = [
    {
        'dueDate': '2018-04-12',
        'typeOfDay': 'Wochentag',
        'timeIntervalDescription': 'Tag',
        'start_time': '06:00',
        'end_time': '20:00',
        'pathToGeoJson': 'data/rapperswil.geojson'
    },
    {
        'dueDate': '2018-04-10',
        'typeOfDay': 'Wochentag',
        'timeIntervalDescription': 'Abend',
        'start_time': '20:00',
        'end_time': '00:00',
        'pathToGeoJson': 'data/uster.geojson'
    },
    {
        'dueDate': '2018-04-14',
        'typeOfDay': 'Samstag',
        'timeIntervalDescription': 'Tag',
        'start_time': '06:00',
        'end_time': '20:00',
        'pathToGeoJson': 'data/hardbruecke.geojson'
    },
    {
        'dueDate': '2018-04-15',
        'typeOfDay': 'Sonntag',
        'timeIntervalDescription': 'Nacht',
        'start_time': '00:00',
        'end_time': '04:00',
        'pathToGeoJson': 'data/zurich.geojson'
    },
]


def load_available_ratings() -> list:
    numbered_ratings = zip(range(len(available_ratings)), available_ratings)
    ratings = map(lambda rating: AvailableRating.create_from_config(*rating), numbered_ratings)
    return list(ratings)
