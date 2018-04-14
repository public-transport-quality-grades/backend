from datetime import datetime
from .timeinterval import TimeInterval


class AvailableRating:

    def __init__(self, id_: int, day: datetime, type_of_day: str, time_interval: TimeInterval, data_path: str):
        self.id_ = id_
        self.day = day
        self.type_of_day = type_of_day
        self.time_interval = time_interval
        self.data_path = data_path

    def serialize(self) -> dict:
        return {
            'id': self.id_,
            'day': self.day.date(),
            'typeOfDay': self.type_of_day,
            'timeInterval': self.time_interval.serialize()
        }

    @staticmethod
    def create_from_config(id_: int, rating: dict):
        day = datetime.strptime(rating['dueDate'], '%Y-%m-%d')
        time_interval = TimeInterval(rating['timeIntervalDescription'], rating['start_time'], rating['end_time'])
        return AvailableRating(id_, day, rating['typeOfDay'], time_interval, rating['pathToGeoJson'])
