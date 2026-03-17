from dataclasses import dataclass


@dataclass(frozen=True)
class Bio:
    value: str