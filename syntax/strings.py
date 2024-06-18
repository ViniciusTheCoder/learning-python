# every string is an array, which means that every character inside a string have an array position

a = 'Hello World'
print(a[1]) # shall print 'e'

for x in 'banana':
    print(x)

txt = 'testando parametro in'
print('legal' in txt)

# its possible to slice a string, like in the following code

print(txt[:5])

# its also possible to begin from the end of the string

print(txt[-2:]) # this code take the last 2 characters from txt variable

y = print(txt.split(' '))

#F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

#To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

age = 22
string = f'My name is Vinicius, I am {22} years old'
print(string.upper())