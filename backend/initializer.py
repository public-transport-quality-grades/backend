from model.availablerating import AvailableRating, TimeInterval


# TODO import from some config file
available_ratings = [
    {
        'dueDate': '2018-04-12',
        'typeOfDay': 'Wochentag',
        'timeIntervalDescription': 'Tag',
        'start_time': '08:00',
        'end_time': '20:00',
        'pathToGeoJson': '/home/robin/Documents/ResidenceConan/backend/tests/resources/test_geojson.geojson'
    },
    {
        'dueDate': '2018-04-14',
        'typeOfDay': 'Samstag',
        'timeIntervalDescription': 'Abend',
        'start_time': '20:00',
        'end_time': '00:00',
        'pathToGeoJson': '/home/robin/osm/oevgk18_samstag_abend.geojson'
    }
]


def load_available_ratings() -> list:
    numbered_ratings = zip(range(len(available_ratings)), available_ratings)
    ratings = map(lambda rating: AvailableRating.create_from_config(*rating), numbered_ratings)
    return list(ratings)
