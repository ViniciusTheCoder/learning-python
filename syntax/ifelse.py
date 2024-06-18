# there is a easier way to write ifs in python, just like Ternary Operators in my beloved Javascript

a = 5
b = 5

if a > b: print('a is greater than b')

print ('a is greater than b') if a > b else print ("that's not true, pal")

# if we can / need to check more than 1 value to do something, we can use AND & OR in the if, like

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

  a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# we can use not to check the reverse result of the conditional statement
  a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

# we can also use one if inside another

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")