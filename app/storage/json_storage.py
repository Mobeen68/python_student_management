import json
from ..models.student import Student
from dataclasses import asdict
from pathlib import Path

class JsonStorage:
    def __init__(self, file_path: str | Path = 'students.json') -> None:
        self.file_path: str | Path = file_path
        
    def save(self, students: list[Student]) -> None:
        serialized_students = [asdict(student) for student in students]
        with open(self.file_path, "w") as file:
            json.dump(serialized_students, file, indent=4)
            
    def load(self) -> list[Student]:
        try:    
            with open(self.file_path) as file:
                data = json.load(file)
                return [Student(**student) for student in data]
        except FileNotFoundError:
            return []