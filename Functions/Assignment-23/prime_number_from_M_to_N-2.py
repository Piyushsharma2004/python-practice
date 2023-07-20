def check_is_prime(m, n):
    
    r = ""
    for i in range(m,n+1):
        if i < 0:
            r+=str(i) + " "
        else:
            c = 0 
            for j in range(1,i+1):
                if i % j ==0:
                    c += 1 
            if c == 2:
                r += str(i) + " "
    return r          
m = int(input())
n = int(input())

prime_numbers =  check_is_prime(m,n)

print(prime_numbers) 


# The provided code defines a function check_is_prime that finds prime numbers in the range from m to n (inclusive). The user is asked to input two integers m and n, and then the function is called to compute the prime numbers within the given range.

# Let's go through the code step by step:

# def check_is_prime(m, n):: This line defines the function check_is_prime, which takes two arguments, m and n, representing the starting and ending values of the range, respectively.

# r = "": A variable r is initialized as an empty string. This variable will be used to store the prime numbers found in the specified range.

# for i in range(m, n+1):: This for loop iterates over the numbers from m to n (inclusive). It includes both m and n in the range.

# if i < 0:: Inside the loop, there's a check to see if the current number i is negative. If it is negative, it is appended to the r string with a space, as negative numbers are not considered prime.

# else:: If the current number i is positive (not negative), the code proceeds to check if it is a prime number.

# c = 0: A variable c is initialized to zero. This variable will be used to count the number of divisors of the current number i.

# for j in range(1, i+1):: This nested for loop iterates over the numbers from 1 to i (inclusive) to find the divisors of the current number i.

# if i % j == 0:: For each value j in the range, the code checks if the current number i is divisible by j without any remainder. If it is, the c variable is incremented by 1, as j is a divisor of i.

# if c == 2:: After the nested loop finishes, the code checks if the number of divisors (c) is equal to 2. A prime number has exactly two divisors: 1 and itself. So, if c is 2, it means the current number i is a prime number.

# r += str(i) + " ": If the current number i is prime, it is appended to the r string, separated by a space.

# return r: After the loop completes, the function returns the r string, which contains all the prime numbers found in the range, separated by spaces.

# m = int(input()): This line takes user input from the console and converts it to an integer, storing it in the variable m.

# n = int(input()): This line takes another user input from the console and converts it to an integer, storing it in the variable n.

# prime_numbers = check_is_prime(m, n): The check_is_prime function is called with the user-inputted values of m and n, and the result (prime numbers) is stored in the prime_numbers variable.

# print(prime_numbers): The prime numbers found in the specified range are printed to the console.

# For example, if the user enters 1 for m and 10 for n, the program will find the prime numbers in the range from 1 to 10:

# mathematica
# Copy code
# Prime numbers: 2 3 5 7
# So, the program will print 2 3 5 7 as the result.

