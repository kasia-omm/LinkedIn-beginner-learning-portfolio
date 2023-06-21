user_text = input("Enter some text: ")
print(user_text.upper())

user_number = input("What do you want to double? ")

print(int(user_number) * 2)

"""First ask for some text, and then prompt
 "Enter 1 to uppercase and 2 to lowercase:" and then 
 either upper or lowercase it """

text_input = input("Please enter some text: ")

upper_or_lower = input("Enter 1 to uppercase and enter 2 to lowercase: ")

if upper_or_lower == "1":
    print(text_input.upper())
else:
    print(text_input.lower())

