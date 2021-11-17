# -*- coding: utf-8 -*-
import datetime
import re
from typing import Dict
from decimal import Decimal

from lagom import FunctionCollection

from .models import IsSevenResult, yep, nope


def is_numeric_seven(possible_seven: str) -> IsSevenResult:
    try:
        if Decimal(possible_seven) == 7:
            return yep("According to python this casts to 7")
    except:
        pass

    return nope("This doesn't seem to be 7 or 7.0")


sevens: Dict[str, str] = {
    "sewe": "That was seven in Afrikaans",
    "shtatë": "That was seven in Albanian",
    "ሰባት": "That was seven in Amharic",
    "سبعة": "That was seven in Arabic",
    "յոթ": "That was seven in Armenian",
    "yeddi": "That was seven in Azerbaijani",
    "সাত": "That was seven in Bangla",
    "zazpi": "That was seven in Basque",
    "сем": "That was seven in Belarusian",
    "sedam": "That was seven in Bosnian & Croatian",
    "седем": "That was seven in Bulgarian",
    "ခုနှစ်": "That was seven in Burmese",
    "set": "That was seven in Catalan",
    "pito": "That was seven in Cebuano",
    "七": "That was seven in Chinese",
    "sette": "That was seven in Corsican & Italian",
    "sedm": "That was seven in Czech",
    "syv": "That was seven in Danish & Norwegian",
    "zeven": "That was seven in Dutch",
    "seven": "That was seven in English",
    "sep": "That was seven in Esperanto",
    "seitse": "That was seven in Estonian",
    "pitong": "That was seven in Filipino",
    "seitsemän": "That was seven in Finnish",
    "sept": "That was seven in French",
    "sete": "That was seven in Galician & Portuguese",
    "შვიდი": "That was seven in Georgian",
    "sieben": "That was seven in German",
    "εφτά": "That was seven in Greek",
    "સાત": "That was seven in Gujarati",
    "sèt": "That was seven in Haitian Creole",
    "bakwai": "That was seven in Hausa",
    "ʻehiku": "That was seven in Hawaiian",
    "שבעה": "That was seven in Hebrew",
    "सात": "That was seven in Hindi & Marathi & Nepali",
    "xya": "That was seven in Hmong",
    "hét": "That was seven in Hungarian",
    "sjö": "That was seven in Icelandic",
    "Asaa": "That was seven in Igbo",
    "tujuh": "That was seven in Indonesian & Malay & Sundanese",
    "seacht": "That was seven in Irish",
    "セブン": "That was seven in Japanese",
    "pitung": "That was seven in Javanese",
    "ಏಳು": "That was seven in Kannada",
    "Жеті": "That was seven in Kazakh",
    "ប្រាំពីរ": "That was seven in Khymer",
    "karindwi": "That was seven in Kinyarwanda",
    "일곱": "That was seven in Korean",
    "heft": "That was seven in Kurdish",
    "жети": "That was seven in Kyrgyz",
    "ເຈັດ": "That was seven in Lao",
    "septem": "That was seven in Latin",
    "septiņi": "That was seven in Latvian",
    "septyni": "That was seven in Lithuanian",
    "siwen": "That was seven in Luxembourgish",
    "седум": "That was seven in Macedonian",
    "Fito": "That was seven in Malagasy",
    "ഏഴ്": "That was seven in Malayalam",
    "sebgħa": "That was seven in Maltese",
    "whitu": "That was seven in Maori",
    "Долоо": "That was seven in Mongolian",
    "Zisanu ndi ziwiri": "That was seven in Nyanja",
    "ସାତ": "That was seven in Odia",
    "اووه": "That was seven in Pashto",
    "هفت": "That was seven in Persian",
    "siedem": "That was seven in Polish",
    "ਸੱਤ": "That was seven in Punjabi",
    "șapte": "That was seven in Romanian",
    "семь": "That was seven in Russian",
    "fitu": "That was seven in Somoan",
    "seachd": "That was seven in Scottish Gaelic",
    "седам": "That was seven in Serbian",
    "minomwe": "That was seven in Shona",
    "ست": "That was seven in Sindhi",
    "හත": "That was seven in Sinhala",
    "sedem": "That was seven in Slovak & Slovenian",
    "toddoba": "That was seven in Somali",
    "supa": "That was seven in Southern Sotho",
    "siete": "That was seven in Spanish",
    "saba": "That was seven in Swahili",
    "sju": "That was seven in Swedish",
    "Ҳафт": "That was seven in Tajik",
    "ஏழு": "That was seven in Tamil",
    "Җиде": "That was seven in Tatar",
    "ఏడు": "That was seven in Telugu",
    "เจ็ด": "That was seven in Thai",
    "yedi": "That was seven in Turkish",
    "ýedi": "That was seven in Turkmen",
    "сім": "That was seven in Ukranian",
    "سات": "That was seven in Urdu",
    "يەتتە": "That was seven in Uyghur",
    "yetti": "That was seven in Uzbek",
    "bảy": "That was seven in Vietnamese",
    "saith": "That was seven in Welsh",
    "sân": "That was seven in Western Frisian",
    "sixhengxe": "That was seven in Xhosa",
    "זיבן": "That was seven in Yiddish",
    "meje": "That was seven in Yoruba",
    "isikhombisa": "That was seven in Zulu",
    "7️⃣": "That was the seven emoji",
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


valid_binary = re.compile(r"^[10]+$")


def is_binary_for_seven(possible_seven: str) -> IsSevenResult:
    tidied_possible_seven = possible_seven.strip()
    match = valid_binary.match(tidied_possible_seven)
    if match and int(tidied_possible_seven, 2) == 7:
        return yep("Binary for 7!")
    return nope("Not seven, sorry")


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


ALL_CHECKERS = FunctionCollection(
    is_numeric_seven,
    is_the_word_seven,
    is_roman_numeral_for_seven,
    is_seven_of_something_repeated,
    is_the_time_seven,
    is_it_a_pop_culture_reference,
    is_it_maths_with_the_answer_seven,
    is_binary_for_seven,
)
