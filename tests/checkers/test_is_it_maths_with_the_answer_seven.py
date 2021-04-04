import pytest

from isseven.checkers import is_it_maths_with_the_answer_seven


@pytest.mark.parametrize("sum_statement", ["3+4", "2+5", "1.1 + 5.9"])
def test_a_few_additions(sum_statement):
    assert is_it_maths_with_the_answer_seven(sum_statement).isseven


@pytest.mark.parametrize("minus_statement", ["8-1", "7.5-0.5", "7-0"])
def test_a_few_subtractions(minus_statement):
    assert is_it_maths_with_the_answer_seven(minus_statement).isseven
