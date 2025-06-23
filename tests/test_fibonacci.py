from src import fibonacci
from assertpy import assert_that


class TestFibonacci:
    def test_fibonacci(self):
        actual = fibonacci(n=5, k=3)

        assert_that(actual).is_equal_to(19)
