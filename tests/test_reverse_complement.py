from src import reverse_complement
from assertpy import assert_that


class TestReverseComplement:
    def test_reverse_complement(self):
        test_dna = "AAAACCCGGT"
        expected = "ACCGGGTTTT"
        actual = reverse_complement(test_dna)
        assert_that(actual).is_equal_to(expected)
