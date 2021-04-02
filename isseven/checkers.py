from typing import Tuple, Collection

from .models import IsSevenResult


def is_integer_seven(possible_seven: str) -> IsSevenResult:
    try:
        if int(possible_seven) == 7:
            return IsSevenResult(
                isseven=True, explanation="According to python this casts to 7"
            )
    except:
        pass

    return IsSevenResult(isseven=False, explanation="Not an integer seven")


sevens: Collection[Tuple[str, str]] = [
    ("seven", "That was seven in english"),
    ("sju", "That was seven in swedish"),
]


def is_the_word_seven(possible_seven: str) -> IsSevenResult:
    tidied_possible_seven = possible_seven.strip().lower()
    for (actual_seven, description) in sevens:
        if actual_seven == tidied_possible_seven:
            return IsSevenResult(isseven=True, explanation=description)
    return IsSevenResult(isseven=False, explanation="Not the word seven")
