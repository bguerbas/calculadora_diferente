from abc import ABC, abstractmethod


class DriverHandlerInterface(ABC):
    @abstractmethod
    def standard_derivation(self, numbers: list[float]) -> float:
        pass

    @abstractmethod
    def variance(self, numbers: list[float]) -> float:
        pass
