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
        
class Lecturer(Mentor):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.lector_grades = {}
        

some_student = Student("Ruoy", "Eman")
some_student.courses_in_progress += ["Python"]
 
some_lecturer = Lecturer("Some", "Buddy")
some_lecturer.courses_attached += ["Python"]
 
some_student.rate_lecturer(some_lecturer, "Python", 10)
some_student.rate_lecturer(some_lecturer, "Python", 8)
some_student.rate_lecturer(some_lecturer, "Python", 5)


print(some_lecturer.lector_grades)
    







