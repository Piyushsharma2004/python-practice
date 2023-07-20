def is_prime(number):
    
    c = 0
    for i in range (1,number+1):
        if number % i == 0:
            c += 1
        else:
            continue
    if c == 2:
        return "Prime Number"
    else:
        return "Not a Prime Number"


number = int(input())
result = is_prime(number)
print(result)

# def is_prime(number):: This line defines the function is_prime that takes one integer parameter number.

# c = 0: Inside the function, it initializes the variable c to 0. This variable will be used to count the number of factors of number.

# for i in range(1, number + 1):: The function uses a for loop to iterate over the numbers from 1 to number (inclusive). The range() function generates a sequence of numbers starting from 1 and ending at number, both endpoints included.

# if number % i == 0:: For each number i in the range, it checks if number is divisible by i by checking if the remainder of number divided by i is equal to 0.

# c += 1: If number is divisible by i, it increments the counter c by 1, effectively counting the factors of number.

# else: continue: If number is not divisible by i, it continues to the next iteration of the loop using the continue statement.

# if c == 2:: After the loop finishes, the function checks if the count of factors c is equal to 2.

# return "Prime Number": If c is equal to 2, it means the input number has exactly two factors (1 and the number itself), and the function returns "Prime Number".

# else: return "Not a Prime Number": If c is not equal to 2, it means the input number has more than two factors, and the function returns "Not a Prime Number".

# number = int(input()): This line prompts the user to input an integer value number and stores it in the variable number.

# result = is_prime(number): This line calls the is_prime function with the input number as an argument and stores the resulting string (either "Prime Number" or "Not a Prime Number") in the variable result.

# print(result): Finally, the code prints the string result, which indicates whether the input number is prime or not.

# For example, if the user inputs 7, the code will calculate and print "Prime Number", indicating that 7 is a prime number. If the user inputs 10, the code will calculate and print "Not a Prime Number", indicating that 10 is not a prime number as it has more than two factors.

#input
# 13
#output
# Prime Number