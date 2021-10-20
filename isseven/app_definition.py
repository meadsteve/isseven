import os
from functools import lru_cache
from typing import Collection

from fastapi import FastAPI
from lagom import Container, Singleton
from lagom.integrations.fast_api import FastApiIntegration
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from .checkers import (
    is_numeric_seven,
    is_the_word_seven,
    is_roman_numeral_for_seven,
    is_seven_of_something_repeated,
    is_the_time_seven,
    is_it_a_pop_culture_reference,
    is_it_maths_with_the_answer_seven,
    is_binary_for_seven,
)
from .hacky_hosting import get_homepage_html
from .models import SevenChecker, nope, IsSevenResult, CheckerCollection

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


app = FastAPI(title="Isseven", version="7")

container = Container()
deps = FastApiIntegration(container)

container[Jinja2Templates] = Singleton(
    lambda: Jinja2Templates(directory=__location__ + "/../templates")
)

container[Collection[SevenChecker]] = CheckerCollection(  # type: ignore
    is_numeric_seven,
    is_the_word_seven,
    is_roman_numeral_for_seven,
    is_seven_of_something_repeated,
    is_the_time_seven,
    is_it_a_pop_culture_reference,
    is_it_maths_with_the_answer_seven,
    is_binary_for_seven,
)

homepage_html = get_homepage_html(__location__ + "/../")


@app.get("/", include_in_schema=False)
def root(request: Request, templates=deps.depends(Jinja2Templates)):
    return templates.TemplateResponse(
        "page.html",
        {
            "content": homepage_html,
            "request": request,
        },
    )


@app.get(
    "/is/{possible_seven}",
    response_model=IsSevenResult,
    description="Checks if the input isseven",
    name="isseven",
)
@lru_cache(maxsize=128)
def check(possible_seven: str, checkers=deps.depends(Collection[SevenChecker])):  # type: ignore
    for checker in checkers:
        result = checker(possible_seven)
        if result.isseven:
            return result
    return nope("We tried. This doesn't seem to be seven")


# If no other route matches assume that it might be a static file
app.mount("/", StaticFiles(directory=__location__ + "/../static_assets"), name="static")
