#creating a list with multiple variables using list constructor

name = 'vinicius'
age = float(22)
city = 'Curitiba'

secName = 'alicia'
secAge = '21'
secCity = 'Curitiba'

listCreator = list((name, age, city))
print(listCreator)
print(listCreator[0]) # might print 'vinicius'
print(type(listCreator[1]))

newCity = 'Rio de janeiro'

listCreator[2] = newCity # changing an index value
print(listCreator)

# inserting values in a list
listCreator.insert(0, 'alicia')
print(listCreator)

# append method will insert a new index at the end of the list
listCreator.append(newCity)
print(listCreator)

# it's also possible to concatenate two different lists, like the following code
secListCreator = list((secName,  secAge, secCity))
listCreator.extend(secListCreator)
concatenatedList = listCreator
print(concatenatedList)

# looping the list starting by the index at position 1

i = 0
while i < len(listCreator): 
    print(listCreator[1])
    i = i + 1
          

# i can create a new list from a old list using the copy() method

# in python we have 4 kinds of collection
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

