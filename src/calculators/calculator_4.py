from flask import request as flask_request

from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator4:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: flask_request) -> dict:
        body = request.json
        input_data = self.__validate_body(body)

        mean = self.__calculate_mean(input_data)
        response = self.__format_response(mean)
        return response

    def __validate_body(self, body: dict) -> list[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body bad formatted")

        numbers = body["numbers"]
        return numbers

    def __calculate_mean(self, numbers: list[float]) -> float:
        mean = self.__driver_handler.mean(numbers)
        return mean

    def __format_response(self, mean: float) -> dict:
        return {
            "data": {
                "Calculator": 4,
                "result": round(mean, 2)
            }
        }