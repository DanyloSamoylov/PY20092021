from abc import ABC, abstractmethod


class Animal(ABC):

    # def __init__(self):
    #     pass
    @abstractmethod
    def talk(self):
        pass
        # raise NotImplementedError('You need to implement module for parent classes')


class Dog(Animal):

    def talk(self):
        return 'Woof'


class Cat(Animal):

    def talk(self):
        return 'Meow'


dog = Dog()
cat = Cat()

def some_func(obj):
    return obj.talk()

for obj in [dog, cat]:
    print(some_func(obj))

print(dog.talk())
print(cat.talk())
