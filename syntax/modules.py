import mymodule
import secmodule as smx

mymodule.greetings('Vinícius') # when i call a function from a module, the syntax is always module_name.function_name

a = mymodule.person1['country']
print(a)

b = smx.person2['hair']
print(b)

x = dir(mymodule) ## the dir() function can be used in EVERY module
print(x)