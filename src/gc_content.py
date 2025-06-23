from pathlib import Path

from .fasta import parse_fasta


def gc_content(dna_string: str) -> float:
    return 100 * (dna_string.count("G") + dna_string.count("C")) / len(dna_string)


def fasta_to_content(fasta_dict: dict[str, str]) -> dict[str, float]:
    return {k: gc_content(v) for k, v in fasta_dict.items()}


def get_max_content(gc_content: dict[str, float]):
    max_id = max(gc_content, key=lambda key: gc_content[key])
    return max_id, "{0:.6f}".format(gc_content[max_id])


def run_gc(data_path: Path):
    fasta_dict = parse_fasta(data_path / "rosalind_gc.txt")
    content_dict = fasta_to_content(fasta_dict)
    print(get_max_content(content_dict))
