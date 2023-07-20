def is_prime(n):
    # complete this function
    p =""
    
    for num in range(2,n+1):
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            p += str(num) +" "
    return p 
    


n = int(input())

print(is_prime(n))

# def is_prime(n):: This line defines the function is_prime that takes one integer parameter n.

# p = "": Inside the function, it initializes the variable p to an empty string. This variable will be used to accumulate the prime numbers.

# for num in range(2, n + 1):: The function uses an outer for loop to iterate over the numbers from 2 to n (inclusive). The outer loop generates a sequence of numbers starting from 2 and ending at n.

# for i in range(2, num):: For each number num in the outer loop, it uses an inner for loop to iterate from 2 to one less than num. The inner loop generates a sequence of numbers starting from 2 and ending at one less than num.

# if num % i == 0:: For each number i in the inner loop, it checks if num is divisible by i by checking if the remainder of num divided by i is equal to 0.

# break: If num is divisible by any i, it breaks out of the inner loop and moves to the next num in the outer loop. This means num is not a prime number.

# else: ...: If the inner loop completes without finding any i that divides num, it means num is a prime number (it has only two factors: 1 and num itself).

# p += str(num) + " ": If num is a prime number, it converts num to a string using str(num), appends it to the p string, and adds a space after it. This way, each prime number is separated by a space in the final p string.

# return p: After the outer loop finishes, the function returns the final string p, which contains all the prime numbers separated by spaces.

# n = int(input()): This line prompts the user to input an integer value n and stores it in the variable n.

# print(is_prime(n)): This line calls the is_prime function with the input n as an argument and prints the resulting string of prime numbers.

# For example, if the user inputs 15, the code will calculate and print the prime numbers from 2 to 15: "2 3 5 7 11 13 " (note the space after each prime number).

#input
# 8
#output
# 2 3 5 7 