#Python is as object oriented programming language.
# Almost everything in Python is an object, with its properties and methos.
# A class is like an object constructor, or a "blueprint" for creating objects.

#lets start creating a class

class MyClass:
    x = 5

# now we can use the class MyClass to create objects:

p1 = MyClass()
print(p1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Vinicius', '22')

print(p1.name)
print(p1.age)

#Object Methods

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# its possible to modify or delete objects or objects properties

p1.age = 40

del p1.age

del p1
