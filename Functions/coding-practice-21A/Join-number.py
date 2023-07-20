# Read the space-separated numbers from user input
numbers = input().split()

# Join the numbers with commas using the join() method
joined_numbers = ",".join(numbers)

# Print the joined numbers
print(joined_numbers)

#  The code reads the input from the user and splits it into a list of numbers.
#  The split() method returns an empty list if there are no spaces in the input, otherwise it returns a list with all of the space-separated numbers.
#  The join() method joins each number in one string separated by commas.
#  Finally, print(joined_numbers) prints out joined_numbers which is ",".join(numbers).
#  The code will print the comma-separated numbers from user input.

#input
# 24 45 86 57 88
#output
# 24,45,86,57,88
