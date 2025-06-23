from src import probability_dominant
from assertpy import assert_that


class TestAlleleCombinations:
    def test_probability_dominant(self):
        actual = probability_dominant(2, 2, 2)
        expected = 0.78333
        assert_that(actual).is_close_to(expected, 0.00001)
