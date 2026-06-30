class StudentError(Exception):
    """Base exception for student system."""
    pass


class StudentNotFoundError(StudentError):
    pass


class DuplicateStudentError(StudentError):
    pass


class InvalidStudentError(StudentError):
    pass