import json
from pathlib import Path
from dataclasses import asdict

from app.models.student import Student
from app.storage.storage import Storage

class JsonStorage(Storage):
    def __init__(self, file_path: str | Path = 'students.json') -> None:
        self.file_path: str | Path = file_path
        
    def save(self, students: list[Student]) -> None:
        serialized_students = [asdict(student) for student in students]
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(serialized_students, file, indent=4)
            
    def load(self) -> list[Student]:
        try:    
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Student(**student) for student in data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []