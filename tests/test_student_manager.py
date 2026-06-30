import pytest

from app.models.student import Student
from app.services.student_manager import StudentManager
from app.storage.memory_storage import MemoryStorage

@pytest.fixture
def manager() -> StudentManager:
    
    return StudentManager(MemoryStorage())

def test_add_student(manager: StudentManager):
    manager.add_student(Student("Ali", 20, 'test@test.com'))

    assert len(manager.students) == 1
    
def test_add_duplicate_student(manager: StudentManager):
    manager.add_student(Student("Ali", 20, 'test@test.com'))
    with pytest.raises(ValueError) as exc_info:
        manager.add_student(Student("Ali", 20, 'test@test.com'))
        
    assert "Student already exist" in str(exc_info.value)
    
def test_remove_student(manager: StudentManager):
    manager.add_student(Student("Ali", 20, 'test@test.com'))
    manager.remove_student("test@test.com")
    assert len(manager.students) == 0
    
def test_remove_non_existing_student(manager: StudentManager):
    with pytest.raises(ValueError) as exc_info:
        manager.remove_student("test@test.com")
    assert "Student not found" in str(exc_info.value)
    
def test_find_student(manager:StudentManager):
    manager.add_student(Student("Ali", 20, 'test@test.com'))

    result = manager.find_student("test@test.com")
    assert result is not None
    assert result.name == "Ali"
        
def test_load_empty_student_list(manager:StudentManager):
    assert len(manager.list_students()) == 0