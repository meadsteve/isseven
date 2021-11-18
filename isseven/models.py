from typing import Callable, Collection, List, Optional

from pydantic import BaseModel


class IsSevenResult(BaseModel):
    isseven: bool
    explanation: str
    valid_for_seconds: Optional[int] = None


def yep(because: str, valid_for_seconds: Optional[int] = None) -> IsSevenResult:
    return IsSevenResult(
        isseven=True, explanation=because, valid_for_seconds=valid_for_seconds
    )


def nope(because: str, valid_for_seconds: Optional[int] = None) -> IsSevenResult:
    return IsSevenResult(
        isseven=False, explanation=because, valid_for_seconds=valid_for_seconds
    )


SevenChecker = Callable[[str], IsSevenResult]
