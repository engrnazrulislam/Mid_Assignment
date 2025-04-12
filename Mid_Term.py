# Mid Term Exam: Student Database Management System
class StudentDatabase:
    student_lists=[]

    def add_student(self,student):
        self.student_lists.append(student)

    def find_student(self, student_id):
        for student in self.student_lists:
            if student.get_student_id() == student_id:
                return student
        return None
    
    def view_all_students(self):
        for student in self.student_lists:
            student.view_student_info()

class Student:
    def __init__(self,student_id, name, department):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = False

    def enroll_student(self):
        if not self.__is_enrolled:
            self.__is_enrolled = True
            print(f'{self.__name} has been enrolled')
        else:
            print(f'{self.__name} is already enrolled')

    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled = False
            print(f'{self.__name} has been dropped.')
        else:
            print(f'{self.__name} is not currently enrolled.')
      
    def view_student_info(self):
        if self.__is_enrolled:
            status='Enrolled'
        else:
            status='Not Enrolled'
        print(f'Student_ID: {self.__student_id}, Name: {self.__name}, Department: {self.__department}, Enrollment Status: {self.__is_enrolled} ')

    def get_student_id(self):
        return self.__student_id

def menu(database):
    while True:
        print(f'----Student Database Menu----')
        print('1. View All Students')
        print('2. Enroll Student')
        print('3. Drop Student')
        print('4. Exit')

        option=input("Enter your option: ")
    
        if option == "1":
            database.view_all_students()

        elif option == "2":
            try:
                std_id = int(input("Enter Student ID to Enroll: "))
                student = database.find_student(std_id)
                if student:
                    student.enroll_student()
                else:
                    print("Student ID not found.")
            except:
                print("Invalid student ID!!. Please enter a valid student ID.")

        elif option == "3":
            try:
                std_id = int(input("Enter Student ID to Drop: "))
                student = database.find_student(std_id)
                if student:
                    student.drop_student()
                else:
                    print("Student ID not found.")
            except:
                print("Invalid student ID!!!. Please enter a valid student ID.")

        elif option == "4":
            print("Ending the program.")
            break
        else:
            print("Your option is not correct. Try again.")


std_db = StudentDatabase()

student1 = Student(1, "Nazrul", "Algorithm")
student2 = Student(2, "Rahim", "Python")
student3 = Student(3, "Karim", "C")
student4 = Student(4, "Salam", "CPP")
student5 = Student(5, "Kayum", "Database")
student6 = Student(6, "Jabber", "Data Structure")

std_db.add_student(student1)
std_db.add_student(student2)
std_db.add_student(student3)
std_db.add_student(student4)
std_db.add_student(student5)
std_db.add_student(student6)

menu(std_db)


