from flask import request as flask_request
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.http_bad_request import HttpBadRequestError


class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: flask_request) -> dict:
        body = request.json
        input_data = self.__validate_body(body)

        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)

        self.__verify_results(variance, multiplication)
        response = self.__format_response(variance)
        return response

    def __validate_body(self, body: dict) -> list[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body bad formatted")

        numbers = body["numbers"]
        return numbers

    def __calculate_variance(self, numbers: list[float]) -> float:
        return self.__driver_handler.variance(numbers)

    def __calculate_multiplication(self, numbers: list[float]) -> float:
        multiplication = 1
        for num in numbers:
            multiplication *= num
        return multiplication

    def __verify_results(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise HttpBadRequestError("Process failed: Variance is less than multiplication")

    def __format_response(self, variance: float) -> dict:
        return {
            "data": {
                "Calculator": 3,
                "value": variance,
                "success": True
            }
        }