from typing import Collection

import pytest
from hypothesis import strategies, given, example
from lagom import FunctionCollection

from isseven.app_definition import check, container
from isseven.models import IsSevenResult, SevenChecker


def test_with_no_checkers_the_result_is_no_seven():
    assert check("something", FunctionCollection()).isseven is False


def test_if_a_checker_returns_a_success_that_result_is_returned():
    success_result = IsSevenResult(isseven=True, explanation="testing")
    assert (
        check("something", FunctionCollection(lambda _s: success_result))
        == success_result
    )


@pytest.mark.parametrize("checker", container[Collection[SevenChecker]])  # type: ignore
def test_all_the_checkers_in_the_container_behave_well_with_an_empty_string(checker):
    assert isinstance(checker(""), IsSevenResult)


@given(strategies.text())
@example("seven")
@example("neves")
@example("")
def test_it_works_for_any_sensible_text(text):
    result = check(text, container[Collection[SevenChecker]])  # type: ignore
    assert isinstance(result, IsSevenResult)


@given(strategies.integers())
@example(-1)
@example(7)
@example(0)
def test_it_works_for_integers(number):
    result = check(str(number), container[Collection[SevenChecker]])  # type: ignore
    assert isinstance(result, IsSevenResult)


@given(strategies.decimals())
@example(7.0)
def test_it_works_for_decimals(number):
    result = check(str(number), container[Collection[SevenChecker]])  # type: ignore
    assert isinstance(result, IsSevenResult)


@given(strategies.datetimes())
def test_it_works_for_dates(datetime):
    result = check(str(datetime), container[Collection[SevenChecker]])  # type: ignore
    assert isinstance(result, IsSevenResult)
