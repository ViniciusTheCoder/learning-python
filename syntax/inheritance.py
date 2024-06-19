# to create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class

class Person:
    def __init__(self, fname, lname) :
        self.firstname = fname
        self.lastname = lname

    def printName(self):
        print(self.firstname, self.lastname)

x = Person('John', 'Doe')
x.printName()

class Student(Person):
    pass

x = Student('Mike', 'Olsen')
x.printName()

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname) # super() fn will automatically inherits the methods and parents from its parents
    self.graduationyear = 2019 ## we are now adding a property unique to the student class

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
   print('Welcome', self.firstname, self.lastname, 'to the class of', self.graduationyear)

x = Student('Mike', 'Olsen', 2019)
x.welcome()