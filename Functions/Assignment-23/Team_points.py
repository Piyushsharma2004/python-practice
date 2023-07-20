def calculate_league_points(wins, draws, losses):
    # Complete this function
    print(wins*4 + draws*2 - losses*1)

statistics = input().split(",")
wins = int(statistics[0])
draws = int(statistics[1])
losses = int(statistics[2])

calculate_league_points(wins,draws,losses)


# This code defines a function calculate_league_points that calculates the total points earned by a team in a league based on the number of wins, draws, and losses. The points are calculated using the following rules:

# Each win earns the team 4 points.
# Each draw earns the team 2 points.
# Each loss costs the team 1 point.
# Let's go through the code step by step:

# def calculate_league_points(wins, draws, losses):: This line defines the function calculate_league_points, which takes three arguments: wins, draws, and losses. These parameters represent the number of wins, draws, and losses, respectively, for the team.

# print(wins*4 + draws*2 - losses*1): Inside the function, the total points are calculated using the provided formula, and the result is immediately printed to the console.

# statistics = input().split(","): This line takes user input from the console and splits it into a list using the comma , as the delimiter. The user is expected to enter three values separated by commas, representing the number of wins, draws, and losses, respectively.

# wins = int(statistics[0]), draws = int(statistics[1]), losses = int(statistics[2]): The three values from the statistics list are converted to integers and assigned to the variables wins, draws, and losses.

# calculate_league_points(wins, draws, losses): The calculate_league_points function is called with the provided wins, draws, and losses values.
# Input 
# 4,1,2
# Output
# 16