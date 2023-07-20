def indexing(arg_1, arg_2):
    # Complete this function
    new_index = arg_1[arg_2]
    return new_index

word = input()
index = int(input())
# Call the indexing function
new_index = indexing(word, index)
print(new_index)

# def indexing(arg_1, arg_2):: This line defines a function named indexing, which takes two parameters arg_1 (the word or string) and arg_2 (the index).

# new_index = arg_1[arg_2]: Inside the indexing function, it retrieves the character at the specified arg_2 index from the string arg_1 and assigns it to the variable new_index. Note that indexing in Python starts from 0, so arg_1[0] will be the first character of the string.

# return new_index: The function then returns the character at the specified index.

# word = input(): This line prompts the user to input a word (string), which is stored in the variable word.

# index = int(input()): This line prompts the user to input an index as an integer, which is stored in the variable index.

# new_index = indexing(word, index): This line calls the indexing function with word and index as arguments and stores the resulting character at the specified index in the variable new_index.

# print(new_index): Finally, the code prints the character at the specified index, which was retrieved by the indexing function.

# For example, if the user inputs the word "Hello" and the index 2, the code will print the character 'l' (the third character, as indexing starts from 0).

#input
# Chocolate
# 2
#output
# o
#input
# Google
# 4
#output
# l