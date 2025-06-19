from pathlib import Path


complement_dict = {"A": "T", "T": "A", "C": "G", "G": "C"}


def reverse_complement(dna: str) -> str:
    return "".join([complement_dict[base] for base in dna.strip()[::-1]])


def run_revc(data_path: Path):
    print("***** Running REVC task *****")
    with open(f"{data_path}/rosalind_revc.txt", "r") as f:
        base_string = f.readline()
    revc = reverse_complement(base_string)

    print(f"Reverse complement:\t{revc}")
