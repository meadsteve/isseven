from typing import Collection

import pytest

from isseven.app_definition import check, container
from isseven.models import IsSevenResult, SevenChecker, CheckerCollection


def test_with_no_checkers_the_result_is_no_seven():
    assert check("something", CheckerCollection()).isseven is False


def test_if_a_checker_returns_a_success_that_result_is_returned():
    success_result = IsSevenResult(isseven=True, explanation="testing")
    assert (
        check("something", CheckerCollection(lambda _s: success_result))
        == success_result
    )


@pytest.mark.parametrize("checker", container[Collection[SevenChecker]])  # type: ignore
def test_all_the_checkers_in_the_container_behave_well_with_an_empty_string(checker):
    assert isinstance(checker(""), IsSevenResult)
