from pathlib import Path


def parse_fasta(fpath: Path) -> dict[str, str]:
    parsed_fasta = dict()
    with open(fpath, "r") as f:
        id = ""
        for line in f:
            if line.startswith(">"):
                id = line.lstrip(">").rstrip()
                parsed_fasta[id] = ""
            else:
                parsed_fasta[id] += line.strip()
    return parsed_fasta
