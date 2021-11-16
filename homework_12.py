# 1. Изучите код программы с сегодняшнего занятия
# 2. Добавьте по 2 homeworks для каждого студента
# 3. Напишите метод для класса Student, который будет изменять status homework для конкретного задания
# 4. Добавьте класс Table, который должен содержать в себе всех студентов
# 5. Реализуйте метод в классе Table, для вывода информации о студентах и статусах homeworks в консоль
# 6. Добавьте 2 студента, проверьте, что метод из задания 5 работает для любого количества студентов
from prettytable import PrettyTable

resultTable = PrettyTable()

class Homework:
    def __init__(self, name, description, complexity, status):
        self.name = name
        self.description = description
        self.complexity = complexity
        self.status = status

    def __repr__(self):
        return f"{self.name} - Status Done = {self.status}"


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.subscribed_courses = []
        self.homeworks = {}

    def __repr__(self):
        return f"{self.name} , {self.homeworks}"

    def add_homework(self, hw_number, homework):
        self.homeworks[hw_number] = homework

    def is_homework_done(self, hw_number):
        if len(self.homeworks) == 0:
            raise Exception("Homeworks is empty")
            current_hw = self.homeworks.get(hw_number)
            return current_hw.status
        return Exception("No such homework")

    def change_homework_status(self, hw_number, status=True):
        current_hw = self.homeworks.get(hw_number)
        if current_hw:
            current_hw.status = status
            return current_hw.status
        return Exception("No such homework for update Status")


class Table:
    def __init__(self, name):
        self.name = name
        self.students = []

    def __str__(self):
        return self.name

    def add_student(self, student_obj):
        self.students.append(student_obj)

    def get_summary(self):
        summary = []
        for student in self.students:
            summary.append(
                [
                    student.name,
                    student.age,
                    student.grade,
                    student.subscribed_courses,
                    student.homeworks,
                ]
            )
        return summary

    def get_summary_table(self):
        resultTable.field_names = [
            "Name",
            "Age",
            "Grade",
            "Subscribed courses",
            "Homeworks",
        ]
        for student in self.students:
            resultTable.add_row(
                [
                    student.name,
                    student.age,
                    student.grade,
                    student.subscribed_courses,
                    student.homeworks,
                ]
            )
        return resultTable


school = [Student("Ivanov", 25, 0),
          Student("Petrov", 35, 0),
          Student("Sidorov", 45, 0)]


def get_new_Homework1():
    return Homework("OOP intorduction", "Extend logic for Student program", 2, False)


def get_new_Homework2():
    return Homework("OOP Classes and modules", "Details description for properties of Classe and Modules", 2, False)


table = Table(name="Python Basic")

print('Task 2 : Two homeworks were added for each Student:')
for student in school:
    student.add_homework(1, get_new_Homework1())
    student.add_homework(2, get_new_Homework2())
    table.add_student(student)
    print(student.name, student.homeworks)

print('\n ')
print('Task 3 : ')
num_hw = input("Input Homework number : ")
fio = input("Input Student : ")

for student in school:
    if student.name == fio:
        student.change_homework_status(int(num_hw))
        print(student.name, student.homeworks)

print("---------All Students and homeworks-----------------------------")
for student in school:
    print(student.name, student.homeworks)


print('\n ')
print('Task 5 : ')

summary = table.get_summary()
for item in summary:
    print(item)


print(table.get_summary_table())
