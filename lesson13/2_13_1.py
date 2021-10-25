
class Person:

    def __init__(self, name, age, college, city):
        self.name = name
        self.age = age
        self.college = college
        self.city = city
        self.teachers = []
        self.students = []

    def __repr__(self):
        return f'{self.name}, age {self.age}, work in {self.college}. From {self.city}.'

    def show_students(self):
        for index, human in enumerate(self.students):
            print(f'{index + 1}. {human.name}, age {human.age}, study in {human.college}. From {human.city}.')

    def add_new_student(self):
        self.students.append(self)

    def add_new_teacher(self):
        self.teachers.append(self)


class Student(Person):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stu_ticket = True


class Teacher(Person):

    def __init__(self, salary,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.salary = salary
        self.high_education = True

    def show_teachers(self):
        return self.teachers

    def tch_salary(self):
        print('Yes i have salary.')


pers = Person
stu = Student
tch = Teacher

stu_lena = stu('Lena', '21', 'Hogwarts', 'Kiev')
stu_dasha = stu('Dasha', '20', 'Hogwarts', 'Odessa')
tch_misha = tch(1000, 'Misha', '30', 'Hogwarts', 'Kiev')
tch_kolya = tch(2000, 'Kolya', '31', 'Hogwarts', 'Kiev')
pers.add_new_student(stu_lena)
pers.add_new_student(stu_dasha)
pers.add_new_teacher(tch_misha)
pers.add_new_teacher(tch_kolya)
# pers.show_students(stu_lena)
print(tch.show_teachers)
# print(pers.show_students())
print(tch_kolya.high_education)
print(tch_misha.salary)
