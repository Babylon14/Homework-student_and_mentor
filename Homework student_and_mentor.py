class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
        and course in lecturer.courses_attached:
            if course in lecturer.lector_grades:
                lecturer.lector_grades[course] += [grade]
            else:
                lecturer.lector_grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return (f"Имя: {self.first_name}\n"
                f"Фамилия: {self.last_name}\n"
                f"Средняя оценка за домашние задания: {9.9}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {", ".join(self.finished_courses)}")



class Mentor:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
        and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"
        
    def __str__(self):
        return (f"Имя: {self.first_name}\n"
                f"Фамилия: {self.last_name}")
        
class Lecturer(Mentor):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.lector_grades = {}

    def __str__(self):
        return (f"Имя: {self.first_name}\n"
                f"Фамилия: {self.last_name}\n"
                f"Средняя оценка за лекции: {9.9}")

    
some_student = Student("Ruoy", "Eman")
some_student.courses_in_progress += ["Python", "Git"]
some_student.finished_courses += ["Введение в программирование"]

some_lecturer = Lecturer("Some", "Buddy")
some_lecturer.courses_attached += ["Python"]

some_reviewer = Reviewer("Some", "Budy")
some_reviewer.courses_attached += ["Python"]
 

print(some_student)
print()
print(some_lecturer)
print()
print(some_reviewer)
    







