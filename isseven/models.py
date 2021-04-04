import inspect
from typing import Callable, Collection, List, Optional

from pydantic import BaseModel


class IsSevenResult(BaseModel):
    isseven: bool
    explanation: str
    matching_method: Optional[str] = None


def yep(because: str) -> IsSevenResult:
    matching_method = None
    try:
        # hacky reflection to find out what made this decision
        matching_method = inspect.stack()[1].function
    except:
        pass
    return IsSevenResult(
        isseven=True, explanation=because, matching_method=matching_method
    )


def nope(because: str) -> IsSevenResult:
    return IsSevenResult(isseven=False, explanation=because)


SevenChecker = Callable[[str], IsSevenResult]


class CheckerCollection:
    """
    Represents a collection of functions that can check if something is 7
    implements Collection[SevenChecker] and is hashable.
    """

    def __init__(self, *checkers: SevenChecker):
        self._checkers = checkers
        self.hash = hash(tuple(self._checkers))

    def __len__(self):
        return len(self._checkers)

    def __contains__(self, item):
        return item in self._checkers

    def __iter__(self):
        return iter(self._checkers)

    def __hash__(self):
        return self.hash
