from abc import ABC, abstractmethod


class PasswordHash(ABC):
    @abstractmethod
    def hash(self, plain_password: str) -> PasswordHash:
        pass

    @abstractmethod
    def verify(self, plain_password: str, hashed_password: PasswordHash) -> bool:
        pass

class EventBus(ABC):
    @abstractmethod
    def publish(self, events: list) -> None:
        pass