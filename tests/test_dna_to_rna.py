from assertpy import assert_that

from src import dna_to_rna


class TestDna:
    def test_dna_to_rna(self):
        test_string = "GATGGAACTTGACTACGTAAATT"
        expected_output = "GAUGGAACUUGACUACGUAAAUU"
        actual = dna_to_rna(test_string)

        assert_that(actual).is_equal_to(expected_output)
