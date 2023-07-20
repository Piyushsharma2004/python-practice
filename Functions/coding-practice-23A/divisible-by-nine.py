def check_divisible_by_9(first_number, second_number, third_number):
    if first_number % 9 == 0 or second_number % 9 == 0 or third_number % 9 == 0:
        return True
    else:
        return False
    # TODO: write code...    
    

first_number = int(input())
second_number = int(input())
third_number = int(input())

result = check_divisible_by_9(first_number,second_number,third_number)

print(result)

# def check_divisible_by_9(first_number, second_number, third_number):: This line defines the function check_divisible_by_9 that takes three integer parameters first_number, second_number, and third_number.

# if first_number % 9 == 0 or second_number % 9 == 0 or third_number % 9 == 0:: Inside the function, it checks if any of the numbers (first_number, second_number, or third_number) are divisible by 9. It does this by checking if the remainder of each number when divided by 9 is 0.

# return True: If any of the numbers are divisible by 9, the function returns True.

# else:: If none of the numbers are divisible by 9, the function executes the code block following else.

# return False: The function returns False in case none of the numbers are divisible by 9.

# first_number = int(input()), second_number = int(input()), third_number = int(input()): These lines prompt the user to input three integer values and store them in variables first_number, second_number, and third_number, respectively.

# result = check_divisible_by_9(first_number, second_number, third_number): This line calls the check_divisible_by_9 function with the input numbers as arguments and stores the result (True or False) in the variable result.

# print(result): Finally, the code prints the result, which is either True if any of the numbers are divisible by 9 or False if none of them are divisible by 9.

# For example, if the user inputs the numbers 27, 10, and 45, the code will print True, as 27 is divisible by 9.

#input
# 3
# 9
# 16
#output
# True



