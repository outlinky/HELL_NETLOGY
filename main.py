class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        student = f'Имя:{self.name} \n' \
                  f'Фамилия:{self.surname} \n' \
                  f'Средняя оценка за домашние задания: {average_grade(self.grades)} \n' \
                  f'Курсы в процессе изучения: {self.courses_in_progress} \n' \
                  f'Завершенные курсы: {self.finished_courses} \n' \
                  f'Средняя оценка {self.name} по "Git": {average_grades(self.grades, "Git")} \n' \
                  f'Средняя оценка {self.name} по "Python": {average_grades(self.grades, "Python")}'
        return student

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Character!')
            return
        return average_grade(self.grades) < average_grade(self.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    pass

    def __str__(self):
        lecturer = f'Имя:{self.name} \n' \
                   f'Фамилия:{self.surname} \n' \
                   f'Средняя оценка за лекции: {average_grade(self.grades)} \n' \
                   f'Средняя оценка {self.name} по "Git": {average_grades(self.grades, "Git")} \n' \
                   f'Средняя оценка {self.name} по "Python": {average_grades(self.grades, "Python")}'
        return lecturer


class Reviewer(Mentor):
    pass

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        reviewer = f'Имя:{self.name} \n' \
                   f'Фамилия:{self.surname}'
        return reviewer


# Средняя оценка общая (для студентов и лекторов)
def average_grade(grades):
    _sum = sum(sum(value) for value in grades.values())
    _len = len(grades.values())
    avg = _sum / _len
    return avg


# Средняя оценка студентов и лекторов
def average_grades(persons, courses):
    _sum = sum(persons.setdefault(courses))
    _len = len(persons.values())
    avg = _sum / _len
    return avg


# создаем экземпляры классов |
reviewer1 = Reviewer('Doctor', 'Strange')
reviewer2 = Reviewer('Doctor', 'Connor')
student1 = Student('Scott', 'Summers', 'M')
student2 = Student('Peter', 'Parker', 'M')
lecturer1 = Lecturer('Charles', 'Xavier')
lecturer2 = Lecturer('Otto', 'Octopus')

# Задаем атрибуты классам
reviewer1.courses_attached += ['Python', 'Git']
reviewer2.courses_attached += ['Python', 'Git']
student1.courses_in_progress += ['Python', 'Git']
student2.courses_in_progress += ['Python', 'Git']
lecturer1.courses_attached += ['Python', 'Git']
lecturer2.courses_attached += ['Python', 'Git']

# Ревьюеры ставят оценки студентам
reviewer1.rate_hw(student1, 'Python', 2)
reviewer1.rate_hw(student1, 'Git', 3)
reviewer2.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student2, 'Git', 9)

# Студенты ставят оценки преподавателям
student1.rate_lecturer(lecturer1, 'Python', 2)
student1.rate_lecturer(lecturer2, 'Python', 10)
student2.rate_lecturer(lecturer1, 'Git', 1)
student2.rate_lecturer(lecturer2, 'Git', 9)

# Печать экземпляров класса (почему я не могу напечатать список указав на сам класс?)
print('Ревьюеры:')
print(reviewer1)
print()
print(reviewer2)
print()
print('Студенты:')
print(student1)
print()
print(student2)
print()
print('Лекторы:')
print(lecturer1)
print()
print(lecturer2)
print()

# Проверяем оценки студентов
print()
print(f'{student1.name}:')
print(student1.grades)
print(f'{student2.name}:')
print(student2.grades)

# Проверяем оценки преподавателей
print()
print(f'{lecturer1.name}:')
print(lecturer1.grades)
print(f'{lecturer2.name}:')
print(lecturer2.grades)

# Сравниваем студентов
print()
print(f'Средние оценки студентов:')
print(f'Студент {student1.name}: {average_grade(student1.grades)} и'
      f' Студент {student2.name}: {average_grade(student2.grades)}')
if average_grade(student1.grades) > average_grade(student2.grades):
    print(f'{student1.name} успешнее {student2.name}')
elif average_grade(student2.grades) > average_grade(student1.grades):
    print(f'{student2.name} успешнее {student1.name}')
else:
    print(f'{student2.name} и {student1.name} имеют одинаковые средние оценки')

# Сравниваем лекторов
print()
print(f'Средние оценки лекторов:')
print(f'Лектор {lecturer1.surname}: {average_grade(lecturer1.grades)} и'
      f' Лектор {lecturer2.surname}: {average_grade(lecturer2.grades)}')
if average_grade(lecturer1.grades) > average_grade(lecturer2.grades):
    print(f'{lecturer1.surname} успешнее {lecturer2.surname}')
elif average_grade(lecturer2.grades) > average_grade(lecturer1.grades):
    print(f'{lecturer2.surname} успешнее {lecturer1.surname}')
else:
    print(f'{lecturer2.surname} и {lecturer1.surname} имеют одинаковые средние оценки')
