import pytest
from deped import calc

@pytest.fixture
def massedge():
    print("\n After test")
    yield
    print("\nBefore test")


def test_calc_sum():
    result = calc(4, 5)
    assert result == 9

def test_calc_sum2(massedge):
    result = calc(4, 5)
    assert result == 4

