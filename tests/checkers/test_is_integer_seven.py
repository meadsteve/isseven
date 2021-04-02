from isseven.checkers import is_integer_seven


def test_the_string_seven_doesnt_pass():
    assert is_integer_seven("seven").isseven is False


def test_the_number_six_doesnt_pass():
    assert is_integer_seven("6").isseven is False


def test_the_number_seven_does_pass():
    assert is_integer_seven("7").isseven
