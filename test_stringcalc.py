import pytest

import stringcalc


def test_add_empty_string():
    assert stringcalc.add("") == 0


def test_add_zero():
    assert stringcalc.add("0") == 0


def test_add_one_int():
    assert stringcalc.add("4") == 4
    assert stringcalc.add("45") == 45
    assert stringcalc.add("124") == 124


def test_add_two_ints():
    assert stringcalc.add("1,2") == 3
    assert stringcalc.add("0,45,5") == 50
    assert stringcalc.add("672,89") == 761


def test_add_many_ints():
    assert stringcalc.add("1,2,3,4,5,6,7,8,9") == 45


def test_add_with_newline_sep():
    assert stringcalc.add("1\n2,3") == 6


def test_add_with_custom_sep():
    assert stringcalc.add("//;\n1;2") == 3
    assert stringcalc.add("//,\n1,2") == 3


def test_add_mixed_separators():
    assert stringcalc.add("//;\n1\n2,3;4") == 10


def test_add_reject_negatives():
     with pytest.raises(ValueError) as exc:
         stringcalc.add("1,-2,-3")

     assert str(exc.value) == "negatives not allowed: -2 -3"
