from typing import Callable

from pydantic import BaseModel


class IsSevenResult(BaseModel):
    isseven: bool
    explanation: str


SevenChecker = Callable[[str], IsSevenResult]
