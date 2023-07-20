def get_odd_numbers_in_range(start_number, end_number):
    w = ""
    for i in range(start_number,end_number+1):
        if i% 2 != 0:
            w += str(i) + " "
    return w        
    

start_number = int(input())
end_number = int(input())

odd_numbers = get_odd_numbers_in_range(start_number,end_number)

print(odd_numbers)

# def get_odd_numbers_in_range(start_number, end_number):: This line defines the function get_odd_numbers_in_range that takes two integer parameters start_number and end_number.

# w = "": Inside the function, it initializes the variable w to an empty string. This variable will be used to accumulate the odd numbers.

# for i in range(start_number, end_number + 1):: The function uses a for loop to iterate over the numbers from start_number to end_number (inclusive). The range() function generates a sequence of numbers starting from start_number and ending at end_number, both endpoints included.

# if i % 2 != 0:: For each number i in the range, it checks if i is odd by checking if i is not divisible by 2 (i.e., the remainder of i divided by 2 is not equal to 0).

# w += str(i) + " ": If i is odd, it converts i to a string using str(i), appends it to the w string, and adds a space after it. This way, each odd number is separated by a space in the final w string.

# return w: After the loop finishes, the function returns the final string w, which contains all the odd numbers separated by spaces.

# start_number = int(input()) and end_number = int(input()): These lines prompt the user to input two integer values, start_number and end_number, and store them in variables start_number and end_number, respectively.

# odd_numbers = get_odd_numbers_in_range(start_number, end_number): This line calls the get_odd_numbers_in_range function with the input start_number and end_number as arguments and stores the resulting string of odd numbers in the variable odd_numbers.

# print(odd_numbers): Finally, the code prints the string odd_numbers, which contains all the odd numbers from start_number to end_number, separated by spaces.

# For example, if the user inputs 3 for start_number and 10 for end_number, the code will calculate and print the odd numbers in that range: "3 5 7 9 " (note the space after each odd number).

#input
# 2
# 7
#output
# 3 5 7 
