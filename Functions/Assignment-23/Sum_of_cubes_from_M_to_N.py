def sum_of_cubes_m_to_n(m, n):
    sum_of_cubes = 0 
    for i in range(m,n+1):
        sum_of_cubes += i**3 
    return sum_of_cubes
    
m = int(input())
n = int(input())
# Call the sum_of_cubes_m_to_n function
print(sum_of_cubes_m_to_n(m,n))


# The provided code defines a function sum_of_cubes_m_to_n that calculates the sum of cubes of numbers from m to n (inclusive). The user is asked to input two integers m and n, and then the function is called to compute the sum of cubes for the given range.

# Let's break down the code step by step:

# def sum_of_cubes_m_to_n(m, n):: This line defines the function sum_of_cubes_m_to_n, which takes two arguments, m and n, representing the starting and ending values of the range, respectively.

# sum_of_cubes = 0: A variable sum_of_cubes is initialized to zero. This variable will be used to store the sum of cubes of numbers in the specified range.

# for i in range(m, n+1):: This for loop iterates over the numbers from m to n (inclusive). It includes both m and n in the range.

# sum_of_cubes += i**3: For each value i in the range, its cube (i**3) is calculated and added to the sum_of_cubes variable.

# return sum_of_cubes: After the loop completes, the function returns the final value of sum_of_cubes, which represents the sum of cubes of numbers from m to n.

# m = int(input()): This line takes user input from the console and converts it to an integer, storing it in the variable m.

# n = int(input()): This line takes another user input from the console and converts it to an integer, storing it in the variable n.

# print(sum_of_cubes_m_to_n(m, n)): The sum_of_cubes_m_to_n function is called with the user-inputted values of m and n, and the result (the sum of cubes) is printed to the console.

# For example, if the user enters 2 for m and 5 for n, the program will calculate the sum of cubes from 2 to 5:

# Copy code
# Sum of cubes = 2^3 + 3^3 + 4^3 + 5^3
# Sum of cubes = 8 + 27 + 64 + 125
# Sum of cubes = 224
# So, the program will print 224 as the result.