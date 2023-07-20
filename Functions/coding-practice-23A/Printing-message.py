def message(arg_1, arg_2):
    # Complete this function
    detail = arg_1 + " is "+ str(arg_2)+ " years old."
    return detail

name = input()
age = int(input())
# Call the message function
detail= message(name,age)
print(detail)

# def message(arg_1, arg_2):: This line defines a function named message, which takes two parameters arg_1 and arg_2.

# detail = arg_1 + " is " + str(arg_2) + " years old.": Inside the message function, it creates a string detail by concatenating the name arg_1 with the string " is " and the age arg_2, which is converted to a string using str().

# return detail: The function then returns the detail string.

# name = input(): This line prompts the user to input their name, which is stored in the variable name.

# age = int(input()): This line prompts the user to input their age as an integer, which is stored in the variable age.

# detail = message(name, age): This line calls the message function with name and age as arguments and stores the resulting message in the variable detail.

# print(detail): Finally, the code prints the detail string, which contains the user's name and age in a formatted message.

# For example, if the user inputs the name "John" and the age 25, the code will print: "John is 25 years old."

#input
# Akhil
# 15
#output
# Akhil is 15 years old.
