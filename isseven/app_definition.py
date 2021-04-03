import os
from functools import lru_cache
from typing import Collection

from fastapi import FastAPI
from lagom import Container
from lagom.integrations.fast_api import FastApiIntegration
from starlette.staticfiles import StaticFiles


from .checkers import (
    is_integer_seven,
    is_the_word_seven,
    is_roman_numeral_for_seven,
    is_seven_of_something_repeated,
)
from .models import SevenChecker, nope, IsSevenResult, CheckerCollection

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


app = FastAPI(title="Isseven")

container = Container()
deps = FastApiIntegration(container)

container[Collection[SevenChecker]] = CheckerCollection(  # type: ignore
    is_integer_seven,
    is_the_word_seven,
    is_roman_numeral_for_seven,
    is_seven_of_something_repeated,
)


@app.get("/", include_in_schema=False)
def root():
    return "isseven?"


@app.get("/is/{possible_seven}", response_model=IsSevenResult)
@lru_cache(maxsize=128)
def check(possible_seven: str, checkers: Collection[SevenChecker] = deps.depends(Collection[SevenChecker])):  # type: ignore
    for checker in checkers:
        result = checker(possible_seven)
        if result.isseven:
            return result
    return nope("We tried. This doesn't seem to be seven")


# If no other route matches assume that it might be a static file
app.mount("/", StaticFiles(directory=__location__ + "/../static_assets"), name="static")
