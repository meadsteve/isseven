from typing import Callable

from pydantic import BaseModel


class IsSevenResult(BaseModel):
    isseven: bool
    explanation: str


def yep(because: str) -> IsSevenResult:
    return IsSevenResult(isseven=True, explanation=because)


def nope(because: str) -> IsSevenResult:
    return IsSevenResult(isseven=False, explanation=because)


SevenChecker = Callable[[str], IsSevenResult]
