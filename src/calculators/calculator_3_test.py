from pytest import raises

from src.drivers.numpy_handler import NumpyHandler
from .calculator_3 import Calculator3
from ..drivers.interfaces.driver_handler_interface import DriverHandlerInterface


class MockRequest:
    def __init__(self, body: dict) -> None:
        self.json = body


class MockDriverHandlerError(DriverHandlerInterface):
    def standard_derivation(self, numbers: list[float]) -> float:
        pass

    def variance(self, numbers: list[float]) -> float:
        return 3


class MockDriverHandler(DriverHandlerInterface):
    def standard_derivation(self, numbers: list[float]) -> float:
        pass

    def variance(self, numbers: list[float]) -> float:
        return 1568.16


def test_calculate_with_variance_error():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
    calculator = Calculator3(MockDriverHandlerError())

    with raises(Exception) as e:
        calculator.calculate(mock_request)
        assert str(e.value) == "Process failed: Variance is less than multiplication"


def test_calculate():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
    calculator = Calculator3(MockDriverHandler())

    response = calculator.calculate(mock_request)

    assert response == {
        "data": {
            "Calculator": 3,
            "value": 1568.16,
            "success": True
        }
    }

