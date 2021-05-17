import pytest
from calweek import CalWeek


def test_cal_week():
    cw = CalWeek('2018-51')
    assert str(cw) == '2018-51', 'Str representation failed'
    assert cw + 2 == '2019-01', 'Add failed'
    assert cw - 3 == '2018-48', 'Sub failed'
    assert CalWeek('2019-04') - cw == 5, 'Sub failed'


if __name__ == '__main__':
    test_cal_week()
