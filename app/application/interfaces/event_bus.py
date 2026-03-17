from abc import ABC, abstractmethod


class UserEvent(ABC):
    @abstractmethod
    def publish(self, events: list) -> None:
        pass
