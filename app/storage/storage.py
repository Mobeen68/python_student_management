from abc import ABC, abstractmethod
from app.models.student import Student


class Storage(ABC):
    @abstractmethod
    def save(
        self,
        students: list[Student]
    ) -> None:
        pass

    @abstractmethod
    def load(
        self
    ) -> list[Student]:
        pass