from datetime import date
from .timeinterval import TimeInterval


class AvailableGrading:
    def __init__(self, id: int, due_date: date, type_of_day: str, tile_name: str, time_interval: TimeInterval):
        self.id: int = id
        self.due_date: date = due_date
        self.type_of_day: str = type_of_day
        self.tile_name: str = tile_name
        self.time_interval: TimeInterval = time_interval

    def __repr__(self):
        return str(self.__dict__)
