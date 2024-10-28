import numpy
from .interfaces.driver_handler_interface import DriverHandlerInterface


class NumpyHandler(DriverHandlerInterface):
    def __init__(self):
        self.__np = numpy

    def standard_derivation(self, numbers: list[float]) -> float:
        return self.__np.std(numbers)

    def variance(self, numbers: list[float]) -> float:
        return self.__np.var(numbers)