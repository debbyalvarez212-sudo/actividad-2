#Student_registry 
from student_registry import Student, StudentRegistry

def main():
    registry = StudentRegistry()

    while True:
        print("\n--- Student Registry Menu ---")
        print("1. Add student")
        print("2. Remove student")
        print("3. Search student")
        print("4. List students")
        print("5. Exit")

        option = input("Select an option: ")

        if option == "1":
            sid = input("Enter student ID: ")
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            student = Student(sid, name, age)
            registry.add_student(student)

        elif option == "2":
            sid = input("Enter the ID of the student to remove: ")
            registry.remove_student(sid)

        elif option == "3":
            sid = input("Enter the ID of the student to search: ")
            registry.find_student(sid)

        elif option == "4":
            registry.list_students()

        elif option == "5":
            print("Exiting system...")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()


