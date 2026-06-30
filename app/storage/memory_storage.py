from app.storage.storage import Storage
from app.models.student import Student

class MemoryStorage(Storage):
    def __init__(self) -> None:
        self.students: list[Student] = []

    def save(
        self,
        students: list[Student]
    ):
        self.students = students

    def load(self):
        return self.students