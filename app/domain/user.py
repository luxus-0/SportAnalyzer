from datetime import datetime
from uuid import UUID

class User:
    id: UUID
    username: str
    password: str
    email: str
    bio: str
    created_at: datetime

    def __init__(self, user_id: str, email: str, name: str, created_at: datetime | None = None):
        self._id = user_id
        self._email = email
        self._name = name
        self._created_at = created_at or datetime.utcnow()
        self._activities = []

    @property
    def id(self) -> str:
        return self._id

    @property
    def email(self) -> str:
        return self._email

    @property
    def name(self) -> str:
        return self._name

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def activities(self):
        return list(self._activities)

    def change_name(self, new_name: str):
        if not new_name:
            raise ValueError("Name cannot be empty")
        self._name = new_name

    def add_activity(self, activity):
        self._activities.append(activity)

    def total_distance(self):
        return sum(activity.distance for activity in self._activities)



