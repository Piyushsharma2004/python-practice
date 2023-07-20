def get_first_upper_letter(string):
    # complete this function
    upper =""
    for i in string:
        if i.upper() == i:
            upper += i 
            break
    return upper    


string = input()
upper_case_character = get_first_upper_letter(string)
print(upper_case_character)

