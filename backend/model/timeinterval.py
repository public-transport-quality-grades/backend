
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
