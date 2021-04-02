import os
from typing import Collection, Callable

from fastapi import FastAPI
from lagom import Container
from lagom.integrations.fast_api import FastApiIntegration
from pydantic import BaseModel
from starlette.staticfiles import StaticFiles


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


app = FastAPI(title="Isseven")

container = Container()
deps = FastApiIntegration(container)


class IsSevenResult(BaseModel):
    isseven: bool
    explanation: str


SevenChecker = Callable[[str], IsSevenResult]


def is_integer_seven(possible_seven: str) -> IsSevenResult:
    try:
        if int(possible_seven) == 7:
            return IsSevenResult(isseven=True, explanation="According to python this casts to 7")
    except:
        pass

    return IsSevenResult(isseven=False, explanation="Not an integer seven")


container[Collection[SevenChecker]] = [
    is_integer_seven
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
