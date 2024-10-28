from .calculator_1 import Calculator1
from typing import Dict
from pytest import raises


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculator_1():
    mock_request = MockRequest(body={"number": 1})
    calculator = Calculator1()

    response = calculator.calculate(mock_request)

    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    assert response["data"]["Calculator"] == 1
    assert response["data"]["result"] == 2.57


def test_calculator_1_with_invalid_body():
    mock_request = MockRequest(body={})
    calculator = Calculator1()

    with raises(Exception) as e:
        calculator.calculate(mock_request)

    assert str(e.value) == "number is required"


def test_calculator_1_with_invalid_number():
    mock_request = MockRequest(body={"number": "invalid"})
    calculator = Calculator1()

    with raises(Exception) as e:
        calculator.calculate(mock_request)

    assert str(e.value) == "number must be a number"
