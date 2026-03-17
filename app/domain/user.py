from datetime import datetime, timezone
from typing import List

from app.domain.bio import Bio
from app.domain.email import Email
from app.domain.events import DomainEvent, UserRegistered, UserBioUpdated
from app.domain.password_hash import PasswordHash
from app.domain.user_id import UserId
from app.domain.username import Username


class User:
    def __init__(
            self,
            user_id: UserId,
            email: Email,
            username: Username,
            password_hash: PasswordHash,
            bio: Bio,
            created_at: datetime,
            version: int = 0
    ):
        self._id = user_id
        self._email = email
        self._username = username
        self._password_hash = password_hash
        self._bio = bio
        self._created_at = created_at
        self._version = version
        self._events: List[DomainEvent] = []

    @classmethod
    def register(
            cls,
            user_id: UserId,
            email: Email,
            username: Username,
            password_hash: PasswordHash
    ) -> 'User':

        user = cls(
            user_id=user_id,
            email=email,
            username=username,
            password_hash=password_hash,
            bio=Bio(""),
            created_at=datetime.now(timezone.utc)
        )
        user._add_event(UserRegistered(
            user_id=user._id,
            email=user._email,
            username=user._username,
            occurred_at=user._created_at
        ))
        return user

    def update_bio(self, new_bio: Bio) -> None:
        if self._bio.value == new_bio.value:
            return

        self._bio = new_bio
        self._add_event(UserBioUpdated(
            user_id=self._id,
            new_bio=new_bio.value,
            occurred_at=datetime.now(timezone.utc)
        ))

    def change_password(self, new_password_hash: PasswordHash) -> None:
        self._password_hash = new_password_hash

    def _add_event(self, event: DomainEvent) -> None:
        self._events.append(event)

    def pull_events(self) -> List[DomainEvent]:
        events = self._events.copy()
        self._events.clear()
        return events

    @property
    def id(self) -> UserId:
        return self._id

    @property
    def email(self) -> Email:
        return self._email

    @property
    def username(self) -> Username:
        return self._username

    @property
    def bio(self) -> Bio:
        return self._bio

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, User):
            return False
        return self._id == other._id