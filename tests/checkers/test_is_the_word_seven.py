# -*- coding: utf-8 -*-
import pytest

from isseven.checkers import is_the_word_seven


def test_it_fails_for_the_number_seven():
    assert is_the_word_seven("7").isseven is False


@pytest.mark.parametrize("word", ["seven", "sju", "sept", "sieben", "7️⃣"])
def test_is_passes_for_words_that_mean_seven(word):
    assert is_the_word_seven(word).isseven
