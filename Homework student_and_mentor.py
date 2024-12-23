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

    def average_grade(self):
        if not self.grades:
            return 0.0
        all_grades = [grd for grade in self.grades.values() for grd in grade]
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        return (f"Имя: {self.first_name}\n"
                f"Фамилия: {self.last_name}\n"
                f"Средняя оценка за домашние задания: {self.average_grade()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")
    
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade() == other.average_grade()
    

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

    def average_grade(self):
        if not self.lector_grades:
            return 0.0
        all_grades = [grd for grade in self.lector_grades.values() for grd in grade]
        return round(sum(all_grades) / len(all_grades), 1)
    
    def __str__(self):
        return (f"Имя: {self.first_name}\n"
                f"Фамилия: {self.last_name}\n"
                f"Средняя оценка за лекции: {self.average_grade()}")
    
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        
    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() == other.average_grade()

    
some_student = Student("Ruoy", "Eman")
some_student.courses_in_progress += ["Python", "Git"]
some_student.finished_courses += ["Введение в программирование"]

some_student_1 = Student("Ruoy", "Eman")
some_student_1.courses_in_progress += ["Python", "Git"]
some_student_1.finished_courses += ["Введение в программирование"]

some_lecturer = Lecturer("Some", "Buddy")
some_lecturer.courses_attached += ["Python"]

some_lecturer_1 = Lecturer("Some", "Buddy")
some_lecturer_1.courses_attached += ["Python"]

some_reviewer = Reviewer("Some", "Budy")
some_reviewer.courses_attached += ["Python"]

some_reviewer_1 = Reviewer("Some", "Buddy")
some_reviewer_1.courses_attached += ["Python"]
 
some_reviewer.rate_hw(some_student, "Python", 8)
some_reviewer.rate_hw(some_student_1, "Python", 9)

some_student.rate_lecturer(some_lecturer, "Python", 9)
some_student_1.rate_lecturer(some_lecturer, "Python", 9)


print(some_student)
print()
print(some_lecturer)
print()
print(some_reviewer)
    
print()

print(some_student < some_student_1)
print(some_student == some_student_1)
print(some_lecturer > some_lecturer_1)
print(some_lecturer == some_lecturer_1)







