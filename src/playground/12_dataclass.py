from dataclasses import dataclass, field


@dataclass
class Task:
    title: str
    done: bool = False
    tags: list[str] = field(default_factory=lambda: ["a", "b", "c", "d"])


a = Task("x")

print(a.tags)
