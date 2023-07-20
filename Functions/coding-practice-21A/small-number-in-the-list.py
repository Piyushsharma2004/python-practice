# Read the space-separated numbers from user input
numbers = input().split()

# Convert the numbers from strings to integers
numbers = [int(num) for num in numbers]

# Find the smallest number using the min() function
smallest_num = min(numbers)

# Print the smallest number
print(smallest_num)

#  The code starts by reading the numbers from user input.
#  The program then splits them into an array of strings and converts them to integers using the int() function.
#  Next, it finds the smallest number in the list using min().
#  Finally, it prints out that number.
#  The code starts by reading a string containing numbers separated by spaces from user input.
#  It then splits this string into an array of strings with each space being considered as a new element in the list (elements are numbered 0-9).
#  Each element is converted to an integer using int(), which is done for all elements in one go so that there's no need to iterate through every single element individually.
#  Then, min() is used on these integers to find the smallest value among them and print it out at last.
#  The code will print the smallest number.

#input
# 54 10 15 24 7 12
#output
# 7
