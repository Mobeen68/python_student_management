from ..models.student import Student
from ..storage.json_storage import JsonStorage

class StudentManager():
    def __init__(self, storage: JsonStorage):
        self.storage = storage
        self.students = storage.load()
        
    def list_students(self) -> list[Student]:
        return self.students
    
    def add_student(self, student: Student) -> None:
        if student.age < 0:
            raise ValueError('Invalid age')
        
        if self.find_student(student.email):
            raise ValueError('Student already exist')
        
        self.students.append(student)
        self.storage.save(self.students)
        
    def remove_student(self, email: str) -> None:
        student = self.find_student(email)
        if student is None:
            raise ValueError('Student not found')
        
        self.students = [student for student in self.students if student.email != email]
        self.storage.save(self.students)
        
    def find_student(self, email: str) -> Student | None:
        for student in self.students:
            if student.email == email:
                return student
        return None