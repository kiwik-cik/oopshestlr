import random

class Student:
    def __init__(self, name, group_number, academic_performance):
        self.name = name
        self.group_number = group_number
        self.academic_performance = academic_performance
        self.gpa_scores = sum(self.academic_performance) / 5

    def print_info(self):
        print(f'ФИ: {self.name}\nНомер группы: {self.group_number}\nУспеваемость: {self.academic_performance}\nСредний балл: {self.gpa_scores}')
def byGPA_key(person):
    return person.gpa_scores

def main():
    students = [
        Student(
            input('Введите фамилию и имя студента: '),
            input('Введите номер группы: '),
            [random.randint(1, 10) for i_grade in range(5)]
        )
        for i_student in range(10)
    ]

    students_sort = sorted(students, key=byGPA_key)
    for student in students_sort:
        student.print_info()

if __name__ == '__main__':
    main()