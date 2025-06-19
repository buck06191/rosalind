from dataclasses import dataclass
from collections import Counter
from pathlib import Path


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


def run_dna(data_path: Path):
    print("***** Running DNA task *****")
    with open(f"{data_path}/rosalind_dna.txt", "r") as f:
        base_string = f.readline()
    base_count = count_bases(base_string)

    print(f"Base count:\t{base_count}")
