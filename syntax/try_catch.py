# when an error occurs, python will stop to run the code and generate an error message

#these exceptions can be handled using try catch

try:
    print(x)
except:
    print('deu ruim')

#using else

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#file handling
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

#raising errors

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
