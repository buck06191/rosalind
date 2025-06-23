from assertpy import assert_that
from src import get_max_content, gc_content, fasta_to_content
import pytest

FASTA_DICT = {
    "Rosalind_6404": "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG",
    "Rosalind_5959": "CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC",
    "Rosalind_0808": "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT",
}


class TestGcContent:
    @pytest.mark.parametrize(
        "dna_str,expected",
        [
            ("AGCTATAG", 37.5),
            (
                "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT",
                60.919540,
            ),
        ],
        ids=["short_string", "long_string"],
    )
    def test_gc_content(self, dna_str, expected):
        actual = gc_content(dna_str)

        assert_that(actual).is_close_to(expected, 1e-6)

    def test_fasta_to_content(self):
        actual = fasta_to_content(FASTA_DICT)
        expected = {
            "Rosalind_6404": 53.75,
            "Rosalind_5959": 53.57142857142857,
            "Rosalind_0808": 60.91954022988506,
        }

        assert_that(actual).is_equal_to(expected)

    def test_get_max_content(self):
        actual = get_max_content(
            {
                "Rosalind_6404": 53.75,
                "Rosalind_5959": 53.57142857142857,
                "Rosalind_0808": 60.91954022988506,
            }
        )

        expected = "Rosalind_0808", "60.919540"

        assert_that(actual).is_equal_to(expected)
