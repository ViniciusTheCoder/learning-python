import json

# some JSON:
x =  '{ "name":"Vinícius", "age":22, "city":"Curitiba"}'

# parse x:
y = json.loads(x)

print(y["age"])

# now lets convert from python to json

name = 'Vinicius'
age = '22'

x = {
    'name': name,
    'age': age
}

y = json.dumps(x)

print(y)

# now let's create a more complex logic, we'll create a class, that has name and age attributes, this attributes will be shared between 3 people, then we will create a list for the 3 of them and then create a json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

vinicius = Person('Vinicius', 22)
alicia = Person('Alicia', '21')

people = [vinicius, alicia]

json_converter = json.dumps([person.__dict__ for person in people])

print(json_converter)

# converting a python object containing all the data types:

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))