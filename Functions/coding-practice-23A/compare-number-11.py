def compare_numbers(first_number, second_number):
    if(first_number > 100 and second_number > 100)and (first_number < second_number):
        return True
    else:
        return False
    
    

first_number = int(input())
second_number = int(input())

is_true = compare_numbers(first_number,second_number)

print(is_true)

# def compare_numbers(first_number, second_number):: This line defines the function compare_numbers that takes two integer parameters first_number and second_number.

# if (first_number > 100 and second_number > 100) and (first_number < second_number):: Inside the function, it checks if both first_number and second_number are greater than 100 and if first_number is less than second_number. It uses logical operators and to combine the conditions.

# return True: If both conditions are met, the function returns True.

# else:: If any of the conditions are not met, the function executes the code block following else.

# return False: The function returns False if any of the conditions are not met.

# first_number = int(input()) and second_number = int(input()): These lines prompt the user to input two integer values and store them in variables first_number and second_number, respectively.

# is_true = compare_numbers(first_number, second_number): This line calls the compare_numbers function with the input numbers as arguments and stores the result (True or False) in the variable is_true.

# print(is_true): Finally, the code prints the result, which is either True if both numbers are greater than 100 and first_number is less than second_number, or False if any of the conditions are not met.

# For example, if the user inputs 150 for first_number and 200 for second_number, the code will print True because both numbers are greater than 100 and first_number (150) is less than second_number (200).

#input
# 105
# 120
#output
# True