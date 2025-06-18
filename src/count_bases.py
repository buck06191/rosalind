from dataclasses import dataclass
from collections import Counter


@dataclass
class BaseCount:
    A: int
    C: int
    T: int
    G: int

    def __repr__(self) -> str:
        return f"{self.A} {self.C} {self.G} {self.T}"


def count_bases(base_string: str) -> BaseCount:
    count = Counter(base_string.upper())
    return BaseCount(A=count["A"], C=count["C"], T=count["T"], G=count["G"])
