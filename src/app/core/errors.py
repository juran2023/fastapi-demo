from dataclasses import dataclass


@dataclass
class Problem:
    type: str
    title: str
    status: int
    detail: str
