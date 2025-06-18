import re


def dna_to_rna(dna: str) -> str:
    return re.sub("T", "U", dna)
