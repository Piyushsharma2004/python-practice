def number_of_cars_needed(no_of_people):
    # Complete this function
    no_of_cars = no_of_people // 5 
    other_people = no_of_people % 5 
    if other_people > 0 :
        no_of_cars += 1 
    print(no_of_cars)    


no_of_people = int(input())
# Call the number_of_cars_needed function
number_of_cars_needed(no_of_people)

# The provided code defines a function number_of_cars_needed that calculates the number of cars needed to transport a given number of people. The number of people is divided by 5 (as each car can carry up to 5 people), and then any remaining people that do not fit into a full car are accommodated by additional cars. After defining the function, the user is prompted to input the number of people, and then the function is called to calculate the number of cars needed.

# Let's go through the code step by step:

# def number_of_cars_needed(no_of_people):: This line defines the function number_of_cars_needed, which takes one argument, no_of_people, representing the total number of people who need to be transported.

# no_of_cars = no_of_people // 5: The total number of people is divided by 5 (using // for integer division) to calculate the number of full cars needed. Each car can carry up to 5 people.

# other_people = no_of_people % 5: The remaining people who do not fit into a full car are calculated using the modulo operator %. For example, if there are 7 people and each car can carry up to 5 people, there will be 2 other people who cannot fit into a full car.

# if other_people > 0:: This condition checks if there are any remaining people who cannot fit into a full car.

# no_of_cars += 1: If there are other people who cannot fit into a full car, an additional car is needed to accommodate them, so the no_of_cars variable is incremented by 1.

# print(no_of_cars): After the calculations are done, the function prints the total number of cars needed to transport all the people.

# no_of_people = int(input()): This line takes user input from the console and converts it to an integer, storing it in the variable no_of_people. The user is expected to enter the total number of people.

# number_of_cars_needed(no_of_people): The number_of_cars_needed function is called with the user-inputted number of people. The function calculates the number of cars needed and prints the result.

# For example, if the user enters 12, the program will calculate the number of cars needed to transport 12 people:

# java
# Copy code
# Number of cars needed = 12 // 5 = 2 (full cars) + 2 (remaining people) = 4 cars
# So, the program will print 4 as the result.