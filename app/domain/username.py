from dataclasses import dataclass


@dataclass(frozen=True)
class Username:
    username: str