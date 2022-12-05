from pydantic import BaseModel
from datetime import datetime


class Point(BaseModel):
    type: str
    coordinates: list


class Event(BaseModel):
    command: str
    group: str
    detect: str
    hook: str
    key: str
    time: str
    id: str
    object: Point

    def __str__(self):
        tstamp = datetime.utcfromtimestamp(self.object.coordinates[2]).strftime('%Y-%m-%d %H:%M:%S')
        return 'detect: {}, lat: {}, lon: {}, timestamp: {}'.format(
            self.detect, self.object.coordinates[0], self.object.coordinates[1], tstamp)
