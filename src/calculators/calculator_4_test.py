from .calculator_4 import Calculator4

from ..drivers.interfaces.driver_handler_interface import DriverHandlerInterface


class MockRequest:
    def __init__(self, body: dict) -> None:
        self.json = body


class MockDriverHandler(DriverHandlerInterface):
    def standard_derivation(self, numbers: list[float]) -> float:
        pass

    def variance(self, numbers: list[float]) -> float:
        pass

    def mean(self, numbers: list[float]) -> float:
        return 3.0


def test_calculator_4():
    mock_request = MockRequest(body={"numbers": [1, 2, 3, 4, 5]})
    calculator = Calculator4(MockDriverHandler())

    response = calculator.calculate(mock_request)

    assert isinstance(response, dict)
    assert response == {
        "data": {
            "Calculator": 4,
            "result": 3.0
        }
    }
