
class Person():

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.list_of_persons = []

    def add_person(self):
        self.list_of_persons.append(mr_john_doe)

    def talk(self):
        print(f'Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old')


mr_john_doe = Person('John', 'Doe', '25')
mr_john_doe.talk()

