import json
from typing import Collection

import pytest
from hypothesis import strategies, given, example
from lagom import FunctionCollection
from starlette.responses import JSONResponse

from isseven.app_definition import check, container
from isseven.models import IsSevenResult, SevenChecker


def test_with_no_checkers_the_result_is_no_seven():
    json_response = check("something", FunctionCollection())
    assert json.loads(json_response.body)["isseven"] is False


def test_if_a_checker_returns_a_success_that_result_is_returned():
    success_result = IsSevenResult(isseven=True, explanation="testing")
    json_response = check("something", FunctionCollection(lambda _s: success_result))
    assert json.loads(json_response.body) == success_result.dict()


def test_by_default_results_are_valid_for_an_hour():
    success_result = IsSevenResult(isseven=True, explanation="testing")
    json_response = check("something", FunctionCollection(lambda _s: success_result))
    assert json_response.headers["Cache-Control"] == "max-age=3600"


def test_non_seven_results_are_cacheable_for_an_hour_by_default():
    json_response = check("something", FunctionCollection())
    assert json_response.headers["Cache-Control"] == "max-age=3600"


def test_checkers_can_control_their_cache_validity():
    success_result = IsSevenResult(
        isseven=True, explanation="testing", valid_for_seconds=30
    )
    json_response = check("something", FunctionCollection(lambda _s: success_result))
    assert json_response.headers["Cache-Control"] == "max-age=30"


def test_when_everything_returns_false_the_shortest_cache_is_honoured():
    success_result = IsSevenResult(isseven=False, explanation="1", valid_for_seconds=30)
    success_result = IsSevenResult(isseven=False, explanation="2", valid_for_seconds=15)
    json_response = check("something", FunctionCollection(lambda _s: success_result))
    assert json_response.headers["Cache-Control"] == "max-age=15"


@pytest.mark.parametrize("checker", container[Collection[SevenChecker]])  # type: ignore
def test_all_the_checkers_in_the_container_behave_well_with_an_empty_string(checker):
    assert isinstance(checker(""), IsSevenResult)


@given(strategies.text())
@example("seven")
@example("neves")
@example("")
def test_it_works_for_any_sensible_text(text):
    result = check(text, container[Collection[SevenChecker]])  # type: ignore
    assert isinstance(result, JSONResponse)


@given(strategies.integers())
@example(-1)
@example(7)
@example(0)
def test_it_works_for_integers(number):
    result = check(str(number), container[Collection[SevenChecker]])  # type: ignore
    assert isinstance(result, JSONResponse)


@given(strategies.decimals())
@example(7.0)
def test_it_works_for_decimals(number):
    result = check(str(number), container[Collection[SevenChecker]])  # type: ignore
    assert isinstance(result, JSONResponse)


@given(strategies.datetimes())
def test_it_works_for_dates(datetime):
    result = check(str(datetime), container[Collection[SevenChecker]])  # type: ignore
    assert isinstance(result, JSONResponse)
