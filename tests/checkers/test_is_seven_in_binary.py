from isseven.checkers import is_binary_for_seven


def test_it_works_for_seven():
    assert is_binary_for_seven("111").isseven

def test_it_works_for_seven_with_leading_zeros():
    assert is_binary_for_seven("00000000111").isseven

def test_it_fails_for_six_or_eight():
    assert not is_binary_for_seven("110").isseven
    assert not is_binary_for_seven("1000").isseven

def test_it_fails_for_a_random_binary_number():
    assert not is_binary_for_seven("1010101010").isseven

def test_it_fails_for_a_random_denary_number():
    assert not is_binary_for_seven("1234567").isseven
