from typing import TYPE_CHECKING

from pms import math

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


VALUE = 2
EXPECTED = 4

def test_regular_doubler() -> None:
    assert math.doubler(VALUE) == EXPECTED


def test_mocked_doubler(mocker: "MockerFixture") -> None:
    spy = mocker.spy(math, "doubler")
    assert math.doubler(VALUE) == EXPECTED
    spy.assert_called_once_with(VALUE)
