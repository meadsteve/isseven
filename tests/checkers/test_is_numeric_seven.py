from isseven.checkers import is_numeric_seven


def test_the_string_seven_doesnt_pass():
    assert is_numeric_seven("seven").isseven is False


def test_the_number_six_doesnt_pass():
    assert is_numeric_seven("6").isseven is False


def test_the_number_seven_does_pass():
    assert is_numeric_seven("7").isseven


def test_the_number_seven_point_o_does_pass():
    assert is_numeric_seven("7.0").isseven


def test_that_really_small_differnces_matter():
    assert is_numeric_seven("7.00000000000000000000000000").isseven
    assert not is_numeric_seven("7.00000000000000000000000001").isseven
