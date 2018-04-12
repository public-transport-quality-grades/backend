from datetime import datetime


class TimeInterval:
    def __init__(self, time_description: str, start: str, end: str):
        self.time_description = time_description
        self.start = start
        self.end = end

    def serialize(self) -> dict:
        return {
            'timeDescription': self.time_description,
            'start': self.start,
            'end': self.end
        }


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
