from typing import Tuple, Collection

from .models import IsSevenResult, yep, nope


def is_integer_seven(possible_seven: str) -> IsSevenResult:
    try:
        if int(possible_seven) == 7:
            return yep("According to python this casts to 7")
    except:
        pass

    return nope("Not an integer seven")


sevens: Collection[Tuple[str, str]] = [
    ("seven", "That was seven in english"),
    ("sju", "That was seven in swedish"),
]


def is_the_word_seven(possible_seven: str) -> IsSevenResult:
    tidied_possible_seven = possible_seven.strip().lower()
    for (actual_seven, description) in sevens:
        if actual_seven == tidied_possible_seven:
            return yep(description)
    return nope("Not the word seven")
