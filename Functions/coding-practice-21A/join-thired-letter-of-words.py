# Read the sentence string from user input
sentence = input()

# Split the sentence into individual words
words = sentence.split()

# Extract the third letter from each word and join with commas
third_letters = [word[2] for word in words]
joined_letters = ",".join(third_letters)

# Print the joined third letters
print(joined_letters)

# User Input: The code prompts the user to enter a sentence.
# Splitting: The split() method is used to split the sentence into individual words. The words are stored in the list words.
# Extracting Third Letters: A list comprehension is used to extract the third letter of each word in the words list. It assumes that the third letter is at the index 2 since indexing in Python starts from 0.
# Joining: The third letters extracted from the words are joined together with commas using the join() method and stored in the variable joined_letters.
# Printing: The joined third letters are then printed to the console.
# For example, if the input sentence is "This is a simple sentence," the code would extract the third letters "i,a,m,l,e,e" and print them.

#input
# Being More Productive
#output
# i,r,o
