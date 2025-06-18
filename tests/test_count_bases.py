from assertpy import assert_that

from src import count_bases


class TestDna:
    def test_count_bases(self):
        test_string = (
            "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
        )
        expected_output = "20 12 17 21"
        actual = str(count_bases(test_string))

        assert_that(actual).is_equal_to(expected_output)
