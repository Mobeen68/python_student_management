from app.models.student import Student
from app.services.student_manager import StudentManager
from app.storage.json_storage import JsonStorage
from app.exceptions.student_exceptions import DuplicateStudentError

manager = StudentManager(JsonStorage())

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Find Student")
    print("4. List Students")
    print("5. Exit")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Please enter a valid option.")
        continue
    
    match choice:
        case 1:
            name = str(input("Enter Name: "))
            try:
                age = int(input("Enter Age: "))
            except ValueError:
                print('Age must be number')
                continue
            email = str(input("Enter Email: "))
            try:
                manager.add_student(Student(name=name, age=age, email=email))
                print('Student Added successfully')
            except DuplicateStudentError as e:
                print(e)
        case 2:
            email = str(input('Enter the email of student that you want to remove: '))
            try:
                manager.remove_student(email=email)
                print('Student removed successfully')
            except ValueError as e:
                print(e)
        case 3:
            email = str(input('Enter the email of student that you want to find: '))
            student: Student | None = manager.find_student(email=email)
            if student is not None:
                print(f'Name: {student.name}',
                  f'\nAge: {student.age}',
                  f'\nEmail: {student.email}')
            else:
                print('Student not found')
        case 4:
            print('Students:')
            print('--------------------')
            students = manager.list_students()
            if not students:
                print('No students found')
            for student in students:
                print(f'Name: {student.name}',
                  f'\nAge: {student.age}',
                  f'\nEmail: {student.email}\n\n')
            print('--------------------')
        case 5:
            print('Goodbye!')
            break
        case _: 
            print('Invalid option')