from datetime import date, timedelta
from seasons import calculate_difference as c
import pytest

def test_one_year_ago():
    assert c("2023-02-13", "2024-02-13") == "Five hundred twenty-five thousand, six hundred minutes"


def test_two_years_ago():
    assert c("2022-02-13", "2024-02-13") == "One million, fifty-one thousand, two hundred minutes"


