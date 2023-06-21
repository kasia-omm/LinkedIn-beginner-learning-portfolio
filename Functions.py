def bark():
    print("Woof woof!")
    print("I'm a dog ")

for x in range(10):
    bark() #call the funtion

#Create a function called hello that prints "Hello Nick!"

def hello():
    print("Hello Nick!")

hello()

"""PARAMETERS"""

def hello(name):
    print(f"Hello {name}")

hello("Mary")

def add_numbers(num1, num2):
    print(num1 + num2)

add_numbers(4, 8)
add_numbers(3, 8)

"""Create a function called dog_info that takes in a dog's 
age and name and prints a sentence about the dog"""

def dog_info(age, name):
    print(f"This dog is called {name}, and it is {age} years old.")

dog_info(5, "Bari")

"""RETURNING INFORMATION"""

def double(number):
    return number * 2

new_number = double(7)

print(new_number)

"""Create a function that returns a string in all caps"""

def capital_str(word):
    return word.upper()

print(capital_str("Kasia"))

names = ["Nick", "Jane", "Sara"]

for name in names: #to loop through the list of names 
    print(capital_str(name)) #print each name in capital letters 
