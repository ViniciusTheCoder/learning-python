# with the while loops i can execute a set of statements as long as a condition is true

i = 1
while i < 6:
    print(i)
    i += 1

i = 1 
while i < 6:
    print(i)
    if i == 3: ## even with a true condition, i can stop a loop with the break
        break
    i += 1

i = 0
while i < 6:
  i += 1
  if i == 4:
    continue # the continue statement will stop the iteration when the loop arrive in number 4, and then jump to number 5
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else: # we can use else when the iteration ends, or by meaning the condition is false
  print("i is no longer less than 6")