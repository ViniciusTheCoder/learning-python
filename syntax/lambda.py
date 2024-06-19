#lambda functions are anonymous, which means they dont have a name and are use exclusively in the place where they were created at the code

# they dont have instructions, loops, conditionals neither alligned functions

# 1 line of code

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6)) # multiplying arguments

x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) #summarize of arguments

# The power of lambda is better shown when you use them as an anonymous function inside another function.

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

# Use lambda functions when an anonymous function is required for a short period of time.