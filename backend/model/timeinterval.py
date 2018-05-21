from datetime import time


class TimeInterval:
    def __init__(self, time_description: str, start: time, end: time):
        self.time_description: str = time_description
        self.start: time = start
        self.end: time = end
