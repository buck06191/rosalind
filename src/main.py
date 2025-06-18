import argparse
from enum import StrEnum
from pathlib import Path

from count_bases import count_bases
from dna_to_rna import dna_to_rna


class ID(StrEnum):
    DNA = "DNA"
    RNA = "RNA"


data_path = Path(__file__).parent.parent / "data"


def run_dna():
    print("***** Running DNA task *****")
    with open(f"{data_path}/rosalind_dna.txt", "r") as f:
        base_string = f.readline()
    base_count = count_bases(base_string)

    print(f"Base count:\t{base_count}")


def run_rna():
    print("***** Running RNA task *****")
    with open(f"{data_path}/rosalind_rna.txt", "r") as f:
        base_string = f.readline()
    rna_string = dna_to_rna(base_string)

    print(f"RNA string:\t{rna_string}")


def run_rosalind(id: ID):
    print(id)
    match id:
        case ID.DNA:
            run_dna()

        case ID.RNA:
            run_rna()


if __name__ == "__main__":
    parser = argparse.ArgumentParser("rosalind")
    parser.add_argument(
        "id", help="The ID from Rosalind. Used to select data file and code", type=str
    )

    args = parser.parse_args()

    run_rosalind(args.id)
