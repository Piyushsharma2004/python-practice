def sum_of_squares_m_to_n(m, n):
    # Complete this function
    sum_of_squares = 0
    for i in range(m , n+1):
        sum_of_squares += i**2
    return sum_of_squares    


m = int(input())
n = int(input())
print(sum_of_squares_m_to_n(m,n))

# def sum_of_squares_m_to_n(m, n):: This line defines the function sum_of_squares_m_to_n that takes two integer parameters m and n.

# sum_of_squares = 0: Inside the function, it initializes the variable sum_of_squares to 0, which will be used to accumulate the sum of squares.

# for i in range(m, n + 1):: The function uses a for loop to iterate over the numbers from m to n (inclusive). The range() function generates a sequence of numbers starting from m and ending at n, both endpoints included.

# sum_of_squares += i**2: For each number i in the range, it calculates its square i**2 and adds it to the sum_of_squares.

# return sum_of_squares: After the loop finishes, the function returns the final value of the sum_of_squares.

# m = int(input()) and n = int(input()): These lines prompt the user to input two integer values, m and n, and store them in variables m and n, respectively.

# print(sum_of_squares_m_to_n(m, n)): This line calls the sum_of_squares_m_to_n function with the input m and n as arguments and prints the resulting sum of squares.

# For example, if the user inputs 1 for m and 3 for n, the code will calculate and print the sum of squares of numbers from 1 to 3: 1**2 + 2**2 + 3**2 = 1 + 4 + 9 = 14.
# input
# 3
# 5
#output
# 50