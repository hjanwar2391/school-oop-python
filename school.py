class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                break

    def display_students(self):
        for student in self.students:
            print(f"Name: {student.name}, Roll Number: {student.roll_number}, Grade: {student.grade}")

# Example usage:
if __name__ == '__main__':
    school = School("My School")

    while True:
        print("\nSchool Management System")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Display Students")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            roll_number = input("Enter roll number: ")
            grade = input("Enter grade: ")
            student = Student(name, roll_number, grade)
            school.add_student(student)

        elif choice == '2':
            roll_number = input("Enter roll number of student to remove: ")
            school.remove_student(roll_number)

        elif choice == '3':
            print("List of Students:")
            school.display_students()

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")
