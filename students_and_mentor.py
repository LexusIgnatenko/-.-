class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка' 

    def __str__(self):
        res = f"Имя: {self.name}\n" \
              f"Фамилия: {self.surname}\n" \
              f"Средняя оценка за домашние задания: {self.get_average_grade_homework()}\n" \
              f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
              f"Завершенные курсы: {', '.join(self.finished_courses)}"
        return res
      
    def get_average_grade_homework(self):
        sum_ = 0
        count = 0
        for course in self.grades.values():
            sum_ += sum(course)
            count += len(course)
        return round(sum_ / count, 2) 
    
    def get_average_grade_course(self, course):
        sum_ = 0
        count = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_ += sum(self.grades[course])
                count += len(self.grades[course])
        return round(sum_ / count, 2)

    
    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
            print("Ошибка")
            return
        else:
            compare = self.get_average_grade_homework() < other_student.get_average_grade_homework()
            if compare:
                print(f"У {self.name} {self.surname} оценка хуже чем, у {other_student.name} {other_student.surname}")
            else:
                print(f"У {self.name} {self.surname} оценка лучше чем, у {other_student.name} {other_student.surname}")
      
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.get_average_grade()}"
        return res
    
    def __lt__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            print("Ошибка")
            return
        else:
            compare = self.get_average_grade() < other_lecturer.get_average_grade()
            if compare:
                print(f"У {self.name} {self.surname} оценка хуже чем, у {other_lecturer.name} {other_lecturer.surname}")
            else:
                print(f"У {self.name} {self.surname} оценка лучше чем, у {other_lecturer.name} {other_lecturer.surname}")

    def get_average_grade(self):
        sum_ = 0
        count = 0
        for course in self.grades.values():
            sum_ += sum(course)
            count += len(course)
        return round(sum_ / count, 2)
    

    def get_average_grade_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating
    
student = Student('Alex', 'Smit', 'M')
student.courses_in_progress += ['Python']
student.finished_courses += ['Введение в программирование']

student2 = Student('Pamela', 'Grand', 'F')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Java']

stud_lst = [student, student2]

lecturer = Lecturer('Peter', 'Parker')
lecturer.courses_attached += ['Python']

lecturer2 = Lecturer('Ben', 'Kross')
lecturer2.courses_attached += ['Python']

lect_lst = [lecturer, lecturer2]

reviewer = Reviewer('Brian', 'Adams')
reviewer.courses_attached += ['Python']

reviewer2 = Reviewer('Lois', 'Klarck')
reviewer2.courses_attached += ['Python']

reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'Python', 9)

reviewer2.rate_hw(student2, 'Python', 7)
reviewer2.rate_hw(student2, 'Python', 9)

student.rate_lecturer(lecturer, 'Python', 10)
student.rate_lecturer(lecturer, 'Python', 8)

student2.rate_lecturer(lecturer2, 'Python', 8)
student2.rate_lecturer(lecturer2, 'Python', 6)

def average_rating_for_course(course, list_):
    sum_rat = 0
    quant_rat = 0
    for stud in list_:
        for course in student.grades:
            stud_sum_rating = stud.get_average_grade_course(course)
            sum_rat += stud_sum_rating
            quant_rat += 1
    average_rating = round(sum_rat / quant_rat, 2)
    return average_rating


print('=' * 30)
print(f"Средняя оценка по курсу {''.join(student.courses_in_progress)} у студентов {average_rating_for_course('Python', stud_lst)}")
print(f"Средняя оценка по курсу {''.join(lecturer.courses_attached)} у лекторов {average_rating_for_course('Python', lect_lst)}")

print('=' * 30)
print(reviewer.__str__())
print('-' * 30)
print(reviewer2.__str__())
print('=' * 30)
print(lecturer.__str__())
print('-' * 30)
print(lecturer2.__str__())
print('=' * 30)
print(student.__str__())
print('-' * 30)
print(student2.__str__())
print('=' * 30)
 
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
 
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
 
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
 
# print(best_student.grades)

# some_reviewer = Reviewer("Some", "Name")
# some_reviewer.courses_attached += ["Python"]
# some_reviewer.courses_attached += ["Git"]
# some_reviewer.rate_hw(some_reviewer, 'Python', 10)
# some_reviewer.rate_hw(some_reviewer, 'Git', 8)
# # print(some_reviewer)

# some_lecturer = Lecturer("Name", "Surname")
# some_lecturer.courses_attached += ["Python"]
# some_lecturer.courses_attached += ["Git"]
 
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
# best_student.courses_in_progress += ['Git']
# best_student.rate_lecturer(some_lecturer, 'Python', 5)
# best_student.rate_lecturer(some_lecturer, 'Python', 4)
# best_student.rate_lecturer(some_lecturer, 'Git', 4)

# # print(some_lecturer)
# # print(get_avg_lect_grade([some_lecturer], "Python"))
# # cool_mentor = Mentor('Some', 'Buddy')
# # cool_mentor.courses_attached += ['Python']
 
# # cool_mentor.rate_hw(best_student, 'Python', 10)
# # cool_mentor.rate_hw(best_student, 'Python', 10)
# # cool_mentor.rate_hw(best_student, 'Python', 10)
 
# # print(best_student.grades)
# print(best_student)