import pytest
import func as oe


@pytest.mark.smoke #marker to tag the similar tests
def test_even():
    res = oe.is_even_or_odd(4)
    assert res == "Even", "4 should be even"

@pytest.mark.smoke #marker to tag the similar tests
def test_odd():
    res = oe.is_even_or_odd(3)
    assert res == "Odd", "3 should be odd"

# @pytest.mark.regression
@pytest.mark.skip(reason = "functionality under development") #skip marker to skip the testcase under any situation
def test_odd_neg():
    res = oe.is_even_or_odd(2)
    assert res == "Odd", "2 should be odd"

developed = False

# @pytest.mark.regression
@pytest.mark.skipif(not developed,reason="feature not developed")
def test_even_neg():
    res = oe.is_even_or_odd(7)
    assert res == "Even", "7 should be even"
