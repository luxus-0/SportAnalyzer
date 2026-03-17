from dataclasses import dataclass


@dataclass(frozen=True)
class Email:
    email: str
