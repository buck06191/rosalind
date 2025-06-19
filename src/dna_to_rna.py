from pathlib import Path
import re


def dna_to_rna(dna: str) -> str:
    return re.sub("T", "U", dna)


def run_rna(data_path: Path):
    print("***** Running RNA task *****")
    with open(f"{data_path}/rosalind_rna.txt", "r") as f:
        base_string = f.readline()
    rna_string = dna_to_rna(base_string)

    print(f"RNA string:\t{rna_string}")
