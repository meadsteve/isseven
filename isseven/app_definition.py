import os
from typing import Collection

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


class SevenChecker:
    def is_seven(self, possible_seven: str) -> IsSevenResult:
        return IsSevenResult(isseven=False, explanation="shrug")


container[Collection[SevenChecker]] = []


@app.get("/", include_in_schema=False)
def root():
    return "isseven?"


@app.get("/{possible_seven}")
def check(possible_seven: str, checkers:Collection[SevenChecker] = deps.depends(Collection[SevenChecker])):
    for checker in checkers:
        result = checker.is_seven(possible_seven)
        if result.isseven:
            return result
    return IsSevenResult(isseven=False, explanation="We tried. This doesn't seem to be seven")


# If no other route matches assume that it might be a static file
app.mount("/", StaticFiles(directory="static_assets"), name="static")
