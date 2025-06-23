import argparse
from enum import StrEnum
from pathlib import Path

from count_bases import run_dna
from dna_to_rna import run_rna
from reverse_complement import run_revc
from fibonacci import run_fib
from gc_content import run_gc
from hamming_distance import run_hamm


class ID(StrEnum):
    DNA = "DNA"
    RNA = "RNA"
    REVC = "REVC"
    FIB = "FIB"
    GC = "GC"
    HAMM = "HAMM"


data_path = Path(__file__).parent.parent / "data"


def run_rosalind(id: ID):
    print(id)
    match id:
        case ID.DNA:
            run_dna(data_path)
        case ID.RNA:
            run_rna(data_path)
        case ID.REVC:
            run_revc(data_path)
        case ID.FIB:
            run_fib(data_path)
        case ID.GC:
            run_gc(data_path)
        case ID.HAMM:
            run_hamm(data_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("rosalind")
    parser.add_argument(
        "id", help="The ID from Rosalind. Used to select data file and code", type=str
    )

    args = parser.parse_args()

    run_rosalind(args.id)
