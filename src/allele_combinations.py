from collections import Counter
import itertools
from pathlib import Path

dominant_probs = {
    "kk": 1,
    "km": 1,
    "kn": 1,
    "mk": 1,
    "nk": 1,
    "mm": 0.75,
    "mn": 0.5,
    "nm": 0.5,
    "nn": 0,
}


def probability_dominant(k: int, m: int, n: int) -> float:
    population = "k" * k + "m" * m + "n" * n
    pairs = list(itertools.permutations(population, 2))
    pair_counts = Counter(["".join(pair) for pair in pairs])
    pair_probs = [(v / len(pairs)) * dominant_probs[k] for k, v in pair_counts.items()]
    return sum(pair_probs)


def run_iprb(data_path: Path):
    with open(data_path / "rosalind_iprb.txt", "r") as f:
        k, m, n = f.readline().strip().split(" ")

    print(probability_dominant(int(k), int(m), int(n)))
