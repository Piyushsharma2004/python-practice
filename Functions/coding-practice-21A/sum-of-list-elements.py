# Read the list of numbers from user input
num_list = input().split()

# Convert the numbers from strings to integers and calculate the sum
sum = 0
for num in num_list:
    sum += int(num)

# Print the sum of the numbers
print(sum)

#  The code starts by reading the list of numbers from user input.
#  The code then splits the list into individual strings and converts them to integers.
#  Next, the code calculates the sum of all of the numbers in a loop.
#  Finally, it prints out that sum on screen.
#  The program starts by asking for a number from user input using input().
#  Then, it splits that number into individual characters with split() and converts each character to an integer with int().
#  It then adds up all of those integers in a loop with for num in num_list: sum += int(num).
#  Finally, it prints out that sum on screen with print(sum)
#  The code converts the inputted list of numbers into an integer sum.

#input 
#2 5 10 -15 3
#output
# 5