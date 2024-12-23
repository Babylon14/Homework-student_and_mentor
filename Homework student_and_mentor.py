class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

class Mentor:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
        and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"
        

some_student = Student("Ruoy", "Eman")
some_student.courses_in_progress += ["Python"]
 
cool_mentor = Mentor("Some", "Buddy")
cool_mentor.courses_attached += ["Python"]
 
cool_mentor.rate_hw(some_student, "Python", 10)
cool_mentor.rate_hw(some_student, "Python", 10)
cool_mentor.rate_hw(some_student, "Python", 10)
 
print(some_student.grades)
    







