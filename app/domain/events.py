from dataclasses import dataclass
from datetime import datetime

from app.domain.email import Email
from app.domain.user_id import UserId
from app.domain.username import Username


class DomainEvent:
    pass

@dataclass
class UserRegistered(DomainEvent):
    user_id: UserId
    email: Email
    username: Username
    occurred_at: datetime

@dataclass
class UserBioUpdated(DomainEvent):
    user_id: UserId
    new_bio: str
    occurred_at: datetime