from pathlib import Path


def hamming_distance(str1: str, str2: str) -> int:
    pairs = zip(str1, str2)
    diffs = [p for p in pairs if p[0] != p[1]]
    return len(diffs)


def run_hamm(data_path: Path):
    with open(data_path / "rosalind_hamm.txt", "r") as f:
        strings = f.readlines()

    print(hamming_distance(*strings))
