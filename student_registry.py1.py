#Class student
class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

    def __str__(self):
        return "ID: " + self.student_id + " - Name: " + self.name + " - Age: " + str(self.age)


class StudentRegistry:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        for s in self.students:
            if s.student_id == student.student_id:
                print("Student already registered.")
                return
        self.students.append(student)
        print("Student added.")

    def remove_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)
                print("Student removed.")
                return
        print("Student not found.")

    def find_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                print(s)
                return
        print("Student not found.")

    def list_students(self):
        if not self.students:
            print("No students registered.")
        else:
            for s in self.students:
                print(s)






