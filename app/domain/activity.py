from datetime import datetime, UTC
from enum import Enum
from typing import List, Optional

from app.domain.statistics import ActivityStatistics
from app.domain.activity_type import ActivityType
from app.domain.gps_point import GPSPoint


class Activity:
    class Activity:

        def __init__(
                self,
                activity_id: str,
                user_id: str,
                activity_type: ActivityType,
                start_time: datetime | None = None
        ):
            self._id = activity_id
            self._user_id = user_id
            self._type = activity_type

            self._start_time = start_time or datetime.now(UTC)
            self._end_time: Optional[datetime] = None

            self._name: Optional[str] = None
            self._description: Optional[str] = None

            self._points: List[GPSPoint] = []
            self._statistics = ActivityStatistics()

        def add_point(self, point: GPSPoint):
            self._points.append(point)



