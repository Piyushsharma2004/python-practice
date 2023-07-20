def factors_of_n(number):
    
    f =""
    for i in range(1,number+1):
        if number % i==0:
            f += str(i) +" "
    return f     
    

number = int(input())
result = factors_of_n(number)
print(result)

# def factors_of_n(number):: This line defines the function factors_of_n that takes one integer parameter number.

# f = "": Inside the function, it initializes the variable f to an empty string. This variable will be used to accumulate the factors of number.

# for i in range(1, number + 1):: The function uses a for loop to iterate over the numbers from 1 to number (inclusive). The range() function generates a sequence of numbers starting from 1 and ending at number, both endpoints included.

# if number % i == 0:: For each number i in the range, it checks if number is divisible by i by checking if the remainder of number divided by i is equal to 0.

# f += str(i) + " ": If number is divisible by i, it converts i to a string using str(i), appends it to the f string, and adds a space after it. This way, each factor of number is separated by a space in the final f string.

# return f: After the loop finishes, the function returns the final string f, which contains all the factors of number separated by spaces.

# number = int(input()): This line prompts the user to input an integer value number and stores it in the variable number.

# result = factors_of_n(number): This line calls the factors_of_n function with the input number as an argument and stores the resulting string of factors in the variable result.

# print(result): Finally, the code prints the string result, which contains all the factors of the input number, separated by spaces.

# For example, if the user inputs 12, the code will calculate and print the factors of 12: "1 2 3 4 6 12 " (note the space after each factor).

#input
# 6
#output
# 1 2 3 6 


