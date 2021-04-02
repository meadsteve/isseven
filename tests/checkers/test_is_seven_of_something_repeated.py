from isseven.checkers import is_seven_of_something_repeated


def test_it_works_for_seven_chars():
    assert is_seven_of_something_repeated("xxxxxxx").isseven


def test_it_fails_for_six_or_eight():
    assert not is_seven_of_something_repeated("xxxxxx").isseven
    assert not is_seven_of_something_repeated("xxxxxxxx").isseven


def test_the_message_tells_you_what_was_repeated():
    assert is_seven_of_something_repeated("xxxxxxx").explanation == "It was x repeated 7 times"
