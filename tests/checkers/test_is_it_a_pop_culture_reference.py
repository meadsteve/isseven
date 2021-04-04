import pytest

from isseven.checkers import is_it_a_pop_culture_reference

references = ["dwarves in snow white", "rings for the dwarf-lords in their halls of stone"]


@pytest.mark.parametrize("reference", references)
def test_the_plain_reference(reference):
    assert is_it_a_pop_culture_reference(reference).isseven


@pytest.mark.parametrize("reference", references)
def test_the_reference_prefix_with_the_number_of(reference):
    assert is_it_a_pop_culture_reference("the number of " + reference).isseven


@pytest.mark.parametrize("reference", references)
def test_the_reference_without_spaces(reference):
    assert is_it_a_pop_culture_reference(reference.replace(" ", "")).isseven
