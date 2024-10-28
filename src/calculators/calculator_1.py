from flask import request as flask_request
from typing import Dict
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator1:
    """
    Um número é divido em 3 partes
    1ª Parte: é divida por 4 e seu resultado somado a 7
    Após isso, o resultado é elevado ao quadrado e multiplicado por 0.257
    2ª Parte: é elevado a potência de 2.121, divida por 5 e somado a 1
    3ª Parte: mantém o valor original
    4ª Parte: é somado o resultado das 3 partes anteriores
    """
    def calculate(self, request: flask_request) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        split_number = input_data / 3
        first_process_result = self.__first_process(split_number)
        second_process_result = self.__second_process(split_number)
        final_result = first_process_result + second_process_result + split_number
        response = self.__format_process(final_result)
        return response

    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise HttpUnprocessableEntityError("body bad formatted")

        input_data = body["number"]
        return input_data

    def __first_process(self, number: float) -> float:
        first_part = (number / 4) + 7
        second_part = (first_part ** 2) * 0.257
        return second_part

    def __second_process(self, number: float) -> float:
        first_part = number ** 2.121
        second_part = (first_part / 5) + 1
        return second_part

    def __format_process(self, number: float) -> Dict:
        return {
            "data": {
                "Calculator": 1,
                "result": round(number, 2)
            }
        }