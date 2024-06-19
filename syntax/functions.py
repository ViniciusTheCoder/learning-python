def myFunction():
    print('My happy function')

myFunction()

# args are added inside the parentheses of a function, and they pass information to the function

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# if my function expects 2 arguments, i have to call the function expecting 2 arguments

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

# if i do not know how many arguments 'll be passed into my func, i have to add a * before the parameters, this will create a tuple of arguments for the function

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# default parameters

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function() # the value that will apear here is Norway
my_function("Brazil")

# returning values

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))