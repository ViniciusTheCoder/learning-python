# for loop is used for iterating over collections like lists, tuples, dicts and also sets, or even a string

# the following example prints each fruits from de list:

fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)

# the following code loop through the letters in the word banana

for x in 'banana':
    print(x)

# in for loops we also have break statement
for x in 'banana':
    print(x)
    if x == 'n':
        break

for fruit in fruits:
    print (fruit)
    if fruit == 'banana':
        break

for fruit in fruits:
        if fruit == 'banana': # in this example we have the break before the print
            break
        print (fruit)



for x in range (2, 30, 3):
    print(x)


#Nested loops are loops inside another loops

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)