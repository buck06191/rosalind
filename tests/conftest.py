import pytest
from pathlib import Path

CONTENT = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT"""


@pytest.fixture
def fasta_file(tmp_path: Path):
    def _create_file(content: str):
        d = tmp_path / "data"
        d.mkdir()
        p = d / "fasta.txt"
        p.write_text(content)
        return p

    return _create_file
