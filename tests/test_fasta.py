from src import parse_fasta
from assertpy import assert_that

from tests.conftest import CONTENT


class TestFasta:
    def test_parse_fasta_creates_correct_output(self, fasta_file):
        filled_file = fasta_file(CONTENT)
        actual = parse_fasta(filled_file)

        expected = {
            "Rosalind_6404": "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG",
            "Rosalind_5959": "CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC",
            "Rosalind_0808": "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT",
        }

        assert_that(actual).is_equal_to(expected)

    def test_parse_fasta_handles_empty_file(self, fasta_file):
        filled_file = fasta_file("")
        actual = parse_fasta(filled_file)

        expected = {}

        assert_that(actual).is_equal_to(expected)
