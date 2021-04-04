import pytest

from isseven.checkers import is_the_time_seven


@pytest.mark.parametrize("time_string", ["07:00", "19:00", "07:00:00", "19:00:00"])
def test_supports_isotime(time_string):
    assert is_the_time_seven(time_string).isseven


@pytest.mark.parametrize("time_string", ["2022-12-13 07:00", "2022-12-13 19:00"])
def test_supports_isodatetime(time_string):
    assert is_the_time_seven(time_string).isseven
