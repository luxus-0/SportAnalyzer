from datetime import datetime


class GPSPoint:

    def __init__(
        self,
        latitude: float,
        longitude: float,
        timestamp: datetime,
        altitude: float | None = None,
        heart_rate: int | None = None,
        cadence: int | None = None,
        speed: float | None = None
    ):
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp
        self.altitude = altitude
        self.heart_rate = heart_rate
        self.cadence = cadence
        self.speed = speed