from abc import ABC, abstractmethod
from typing import Optional, List
from uuid import UUID

from app.domain.user import User

class UserRepository(ABC):

    @abstractmethod
    def save(self, user: User) -> None:
        pass

    @abstractmethod
    def get_by_id(self, user_id: UUID) -> Optional[User]:
        pass

    def get_by_email(self, email):
        pass