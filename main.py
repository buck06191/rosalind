import argparse
from enum import StrEnum
from pathlib import Path

from src import run_dna, run_fib, run_gc, run_hamm, run_revc, run_rna, run_iprb


class ID(StrEnum):
    DNA = "DNA"
    RNA = "RNA"
    REVC = "REVC"
    FIB = "FIB"
    GC = "GC"
    HAMM = "HAMM"
    IPRB = "IPRB"


data_path = Path(__file__).parent / "data"


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
        case ID.IPRB:
            run_iprb(data_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("rosalind")
    parser.add_argument(
        "id", help="The ID from Rosalind. Used to select data file and code", type=str
    )

    args = parser.parse_args()

    run_rosalind(args.id)
