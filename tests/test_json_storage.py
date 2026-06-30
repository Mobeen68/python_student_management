import pytest
from pathlib import Path

from app.models.student import Student
from app.storage.json_storage import JsonStorage

@pytest.fixture
def manager(tmp_path: Path) -> JsonStorage:
    # 1. Create a safe, temporary path unique to this test run
    test_file: Path = tmp_path / "test_students.json"
    
    # 2. Inject this temporary path into your storage engine
    return JsonStorage(file_path=str(test_file))

students: list[Student] = [Student(name='Mobeen', age=12, email='mobeene@test.com'), Student(name='mob', age=12, email='mon'), Student(name='Ali', age=20, email='test@test.com')]

def test_save(manager: JsonStorage):
    manager.save(students=students)
    assert len(manager.load()) == 3
    
def test_load(manager: JsonStorage):
    assert len(manager.load()) == 0
    
def test_load_file_not_found(tmp_path: Path) -> None:
    non_existent_file: Path = tmp_path / "missing_database.json"
    
    storage = JsonStorage(file_path=non_existent_file)
    
    result = storage.load()
    
    assert result == []
    
def test_save_and_load_preserves_data(manager:JsonStorage):
    students = [
        Student(
            "Ali",
            20,
            "test@test.com"
        )
    ]

    manager.save(students)

    loaded = manager.load()

    assert loaded == students
     
    
    