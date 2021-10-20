from isseven.checkers import time_contains_seven
import datetime


def test_all():
    datetime_now = datetime.datetime.now()
    if (
        datetime_now.hour == 7
        or datetime_now.hour == 19
        or str(datetime_now.minute)[-1] == "7"
        or str(datetime_now.second)[-1] == "7"
    ):
        assert time_contains_seven("now").isseven
    else:
        assert not time_contains_seven("now").isseven
