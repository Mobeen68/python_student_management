import csv
from pathlib import Path
from dataclasses import asdict

from app.models.student import Student
from app.storage.storage import Storage

fieldnames = ['Name', 'Age', 'Email']

class CSVStorage(Storage):
    def __init__(self, file_path: str | Path = 'students.csv') -> None:
        self.file_path: str | Path = file_path
        
    def save(self, students: list[Student]) -> None:
        serialized_students = [asdict(student) for student in students]
        with open(self.file_path, "w", newline= '', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(serialized_students)
            
    def load(self) -> list[Student]:
        try:    
            with open(self.file_path, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                header = next(reader)
                students: list[Student] = []
                for row in reader:
                    # Manually unpack and convert types based on your CSV structure
                    name = row[0]
                    age = int(row[1])
                    email = row[2]
                
                    # Create the object and append it to your list
                    students.append(Student(name, age, email))
                
                return students
        except (FileNotFoundError, csv.Error, ValueError):
            # Adding ValueError catches issues if int() or float() conversion fails
            return []