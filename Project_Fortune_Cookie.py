#introducing random numbers by importing a module 

import random #import random module
print(random.randint(1,10)) #randint - specifies random integers and two numbers in brackets are min and max for number generating 

print(random.random()) #random gives us a random float 


# Make your own version of a magic 8 ball that prints yes, no or maybe each time you ask it 
answer = random.randint(1,3)

if answer == 1:
    print("Yes")
if answer == 2:
    print("No")
if answer ==3:
    print("Maybe")

