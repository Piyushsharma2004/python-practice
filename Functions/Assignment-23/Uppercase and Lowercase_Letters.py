def get_lower_and_upper_case_letters(word):
    # Complete this function
    upper_char = ""
    lower_char = ""
    for i in word:
        if i in word:
            if i == i.upper():
                upper_char += i 
            else:
                lower_char += i 
    print(upper_char)
    print(lower_char)

word = input()
# Call the get_lower_and_upper_case_letters function
result = get_lower_and_upper_case_letters(word)


# The provided code defines a function named get_lower_and_upper_case_letters, which separates the uppercase and lowercase letters from a given word. After defining the function, the user is prompted to input a word, and then the function is called to display the uppercase and lowercase letters separately.

# Let's examine the code step by step:

# def get_lower_and_upper_case_letters(word):: This line defines the function get_lower_and_upper_case_letters, which takes one argument, word, representing the word for which we want to separate the uppercase and lowercase letters.

# upper_char = "" and lower_char = "": Two empty strings, upper_char and lower_char, are initialized. These variables will be used to store the uppercase and lowercase letters, respectively.

# for i in word:: This for loop iterates through each character i in the input word.

# if i in word:: This line is redundant and unnecessary. The condition if i in word: will always be true because we are iterating through the characters in the word itself. This line can be removed without affecting the logic of the code.

# if i == i.upper():: This line checks if the character i is an uppercase letter. It compares i with its uppercase version i.upper(). If they are equal, it means i is an uppercase letter.

# upper_char += i: If the character i is an uppercase letter, it is added to the upper_char string.

# else:: If the character i is not an uppercase letter (i.e., it is a lowercase letter), this block is executed.

# lower_char += i: The lowercase letter i is added to the lower_char string.

# print(upper_char): After the loop completes, the function prints the upper_char string, which contains all the uppercase letters from the input word.

# print(lower_char): Similarly, the function also prints the lower_char string, which contains all the lowercase letters from the input word.

# word = input(): This line takes user input from the console and stores it in the variable word. The user is expected to enter a word.

# result = get_lower_and_upper_case_letters(word): The get_lower_and_upper_case_letters function is called with the user-inputted word. However, this line is not necessary since the function already prints the results directly.