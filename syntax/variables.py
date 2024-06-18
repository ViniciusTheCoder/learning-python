x = 5
y = 4

def sumFunction(x, y):
  
  sum = x + y  
  return sum  

result = sumFunction(x, y)
print(result)


# Variables do not need to be declared with any particular type, and can even change type after they have been set.
z = 32
z = 'teste'
print(z)

# If I want, it's possible to specify the type of data that a variable can accept, casting it

a = str(3)
b = int(3)
c = float(3)

print (a, b, c)
print (type (a))

def checkTypeVariable(x, y, c):
    sum = x + y  
    if sum > 8: 
        print (type (c))
        return sum
    
# Variables are case sensitive, the following code creates 2 different variables

a = 'nice'
A = 'nice'

# in 1 line of code it's possible to assign values to multiple values:

testVariable1, testVariable2, testVariable3 = 'test1', 'test2', 'test3'
print(testVariable1, testVariable2, testVariable3)

# i can also assign the same value to multiple variables

t1 = t2 = t3 = str('same value')
print(t1, t2, t3)

# If I have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

hardwares = ['rtx4070', 'rtx3060', 'gtx2060']
seriesRtx = hardwares[0:2]
seriesGtx = hardwares[2]
print (seriesRtx)
print (seriesGtx)

# to output multiple variables with different types its important to sepparate them ALWAYS by comma

variableOne = 5.0
variableTwo = 'Vinicius'
print(variableOne, variableTwo)

print(x + y)

# variables created outside a function are global, but it's possible to create a variable inside a function and declare it global, also I can call a global variable inside a functiona and change it's value

x = "awesome"

def myfunc():
  global x
  x = "fantastic" # changing the value of a global value inside a function

myfunc()

print("Python is " + x)

def myfunc():
  global x # creating a global variable inside a function
  x = "fantastic"

myfunc()

print("Python is " + x)

