import re
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
    ("sept", "That was seven in french"),
    ("sieben", "That was seven in german"),
]


def is_the_word_seven(possible_seven: str) -> IsSevenResult:
    tidied_possible_seven = possible_seven.strip().lower()
    for (actual_seven, description) in sevens:
        if actual_seven == tidied_possible_seven:
            return yep(description)
    return nope("Not the word seven")


def is_roman_numeral_for_seven(possible_seven: str) -> IsSevenResult:
    tidied_possible_seven = possible_seven.strip().lower()
    if tidied_possible_seven == "vii":
        return yep("Roman numeral for 7!")
    return nope("Minimē")


repeated_seven_times = re.compile("^(.){7}$")


def is_seven_of_something_repeated(possible_seven: str) -> IsSevenResult:
    match = repeated_seven_times.match(possible_seven)
    if match:
        return yep(f"It was {match[1]} repeated 7 times")
    return nope("sorry")
