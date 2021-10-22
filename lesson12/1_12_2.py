
class Dog():

    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        return self.age * self.age_factor


my_dog = Dog(10)
print(my_dog.human_age())
