# Read the space-separated numbers from user input
numbers = input().split()

# Convert the numbers from strings to integers and filter out non-divisible numbers
divisible_by_3 = [int(num) for num in numbers if int(num) % 3 == 0]

# Print the list of numbers divisible by 3
print(divisible_by_3)

#  The code starts by reading the numbers from user input.
#  The code then splits the numbers into a list of strings and converts them to integers.
#  Next, it filters out all non-divisible numbers in the list using an if statement that checks whether or not a number is divisible by 3.
#  Finally, it prints out only those numbers that are divisible by 3.
#  The code attempts to read a list of numbers from user input and convert them into integers.
#  Next, the code will filter out any number that is not divisible by 3.
#  Finally, it prints the list of numbers divisible by 3.

#input
# 3 10 9 11 18 20
#output
# [3, 9, 18]
