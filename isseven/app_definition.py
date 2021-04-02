import os
from typing import Collection, Callable

from fastapi import FastAPI
from lagom import Container
from lagom.integrations.fast_api import FastApiIntegration
from starlette.staticfiles import StaticFiles


from .checkers import is_integer_seven, is_the_word_seven
from .models import IsSevenResult

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


app = FastAPI(title="Isseven")

container = Container()
deps = FastApiIntegration(container)

SevenChecker = Callable[[str], IsSevenResult]

container[Collection[SevenChecker]] = [
    is_integer_seven,
    is_the_word_seven
]


@app.get("/", include_in_schema=False)
def root():
    return "isseven?"


@app.get("/{possible_seven}")
def check(possible_seven: str, checkers: Collection[SevenChecker] = deps.depends(Collection[SevenChecker])):
    for checker in checkers:
        result = checker(possible_seven)
        if result.isseven:
            return result
    return IsSevenResult(isseven=False, explanation="We tried. This doesn't seem to be seven")


# If no other route matches assume that it might be a static file
app.mount("/", StaticFiles(directory="static_assets"), name="static")
