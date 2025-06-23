from assertpy import assert_that
from src import hamming_distance


class TestHammingDistance:
    def test_hamming_distance(self):
        str1 = "GAGCCTACTAACGGGAT"
        str2 = "CATCGTAATGACGGCCT"
        actual = hamming_distance(str1, str2)
        expected = 7
        assert_that(actual).is_equal_to(expected)
