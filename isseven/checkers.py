# -*- coding: utf-8 -*-
import datetime
import re
from typing import Dict

from .models import IsSevenResult, yep, nope


def is_numeric_seven(possible_seven: str) -> IsSevenResult:
    try:
        if float(possible_seven) == 7:
            return yep("According to python this casts to 7")
    except:
        pass

    return nope("This doesn't seem to be 7 or 7.0")


sevens: Dict[str, str] = {
    "seven": "That was seven in english",
    "sju": "That was seven in swedish",
    "sept": "That was seven in french",
    "sieben": "That was seven in german",
    "7️⃣": "That was an emoji seven",
    "sewe": "That was seven in Afrikaans",
    "isikhombisa": "That was seven in Zulu",
    "sette": "That was seven in Italian",
    "siete": "That was seven in Spanish",
    "sete": "That was seven in Portuguese",
}


def is_the_word_seven(possible_seven: str) -> IsSevenResult:
    tidied_possible_seven = possible_seven.strip().lower()
    if tidied_possible_seven in sevens:
        return yep(sevens[tidied_possible_seven])
    reversed_word = tidied_possible_seven[::-1]
    if reversed_word in sevens:
        return yep(sevens[reversed_word] + " backwards")
    return nope("Not the word seven")


def is_roman_numeral_for_seven(possible_seven: str) -> IsSevenResult:
    tidied_possible_seven = possible_seven.strip().lower()
    if tidied_possible_seven == "vii":
        return yep("Roman numeral for 7!")
    return nope("Minimē")


repeated_seven_times = re.compile(r"^(.)\1{6}$")


def is_seven_of_something_repeated(possible_seven: str) -> IsSevenResult:
    match = repeated_seven_times.match(possible_seven)
    if match:
        return yep(f"It was {match[1]} repeated 7 times")
    return nope("sorry")


seven_am = datetime.time(hour=7)
seven_pm = datetime.time(hour=19)


def is_the_time_seven(possible_seven: str) -> IsSevenResult:
    time = _attempt_to_parse_out_time(possible_seven)
    if time == seven_am:
        return yep("That's 7 am")
    if time == seven_pm:
        return yep("That's 7 pm")
    return nope("Not 0700 or 1900")


def _attempt_to_parse_out_time(possible_seven):
    try:
        return datetime.time.fromisoformat(possible_seven.strip())
    except:
        pass
    try:
        full_datetime = datetime.datetime.fromisoformat(possible_seven.strip())
        return full_datetime.time()
    except:
        pass
    return None


def _clean_reference(raw: str):
    return (
        raw.strip().lower().replace(" ", "").replace("-", "").replace("thenumberof", "")
    )


references = set(
    [
        _clean_reference(reference)
        for reference in [
            "dwarves in snow white",
            "rings for the dwarf-lords in their halls of stone",
            "rings for the dwarf-lords",
            "deadly sins",
        ]
    ]
)


def is_it_a_pop_culture_reference(possible_seven: str) -> IsSevenResult:
    cleaned = _clean_reference(possible_seven)
    if cleaned in references:
        return yep("I know that reference")
    return nope("I don't know that reference for 7")


maths_expression = re.compile(r"^[0-9\-+*./()]+$")


def is_it_maths_with_the_answer_seven(possible_seven: str) -> IsSevenResult:
    cleaned_statement = possible_seven.replace(" ", "")
    match = maths_expression.match(cleaned_statement)
    try:
        if match:
            # Here be dragons
            possible_seven = eval(match[0])
            if possible_seven == 7:
                return yep("According to the power of maths that is 7")
    except:
        pass
    return nope("That doesn't seem to work out as 7")
