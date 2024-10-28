from flask import request as flask_request
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator2:
    def __init__(self, driver_handler: DriverHandlerInterface):
        self.__driver_handler = driver_handler

    def calculate(self, request: flask_request) -> dict:
        body = request.json
        input_data = self.__validate_body(body)
        calculated_number = self.__process_data(input_data)
        response = self.__format_process(calculated_number)
        return response

    def __validate_body(self, body: dict) -> list[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body bad formatted")

        input_data = body["numbers"]
        return input_data

    def __process_data(self, input_data: list[float]) -> float:
        first_process_result = [(num * 11) ** 0.95 for num in input_data]
        result = self.__driver_handler.standard_derivation(first_process_result)
        return 1 / result

    def __format_process(self, number: float) -> dict:
        return {
            "data": {
                "Calculator": 2,
                "result": round(number, 2)
            }
        }
