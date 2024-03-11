"""
Objective: The objective of my code is to determine the MVP of the 2021-2022 Regular NBA Season based off basic stats,
that the average human being witnesses while watching a game. The stats that are being compared are the season avg
points, rebounds and assists. Amongst three players, if each player dominate their only 1 stat, their would have to be
a tie-breaker amongst them. The game of basketball is to have more points than the other team, thus the player that is
able to contribute the most points to the team will then win in terms of a tie-breaker. Otherwise, if there isn't a
situation like that, the method used in this program can easily find out the MVP of the 2021-2022 NBA Regular Season.
"""

"""
The function mvp_finder() was created to determine the MVP of the 2021-2022 NBA Regular Season based off of the players points,
rebounds & assists.
"""


def mvp_finder():
    # Joel Embiid's 21-22 NBA Regular Season Avg Stats [points, rebounds, assists]
    p1 = [30.6, 11.7, 4.2]
    # Nikola Jokic's 21-22 NBA Regular Season Avg Stats [points, rebounds, assists]
    p2 = [27.1, 13.8, 7.9]
    # Giannis Antetokounmpo's 21-22 NBA Regular Season Avg Stats [points, rebounds, assists]
    p3 = [29.9, 11.6, 5.8]
    # Devin Booker's 21-22 NBA Regular Season Avg Stats [points, rebounds, assists]
    p4 = [26.8, 5.0, 4.8]
    # Luka Doncic's 21-22 NBA Regular Season Avg Stats [points, rebounds, assists]
    p5 = [28.4, 9.1, 8.7]

    # SAMPLE TEST CASE
    # Derrick Rose's 10-11 NBA Regular Season Avg Stats [points, rebounds, assists]
    #p1 = [25.0, 4.1, 7.7]
    # Dwight Howard's 10-11 NBA Regular Season Avg Stats [points, rebounds, assists]
    #p2 = [22.9, 14.1, 1.4]
    # Lebron James's 10-11 NBA Regular Season Avg Stats [points, rebounds, assists]
    #p3 = [26.7, 7.5, 7.0]
    # Kobe Bryant's 10-11 NBA Regular Season Avg Stats [points, rebounds, assists]
    #p4 = [25.3, 5.1, 4.7]
    # Kevin Durant's 10-11 NBA Regular Season Avg Stats [points, rebounds, assists]
    #p5 = [27.7, 6.8, 2.7]

    # Statements to show the user Joel Embiid's stats
    print("The Regular NBA Season stats of Joel Embiid are: ", p1)
    # Statements to show the user Nikola Jokic's stats
    print("The Regular NBA Season stats of Nikola Jokić are: ", p2)
    # Statements to show the user Giannis Antetokounmpo's stats
    print("The Regular NBA Season stats of Giannis Antetokounmpo are: ", p3)
    # Statements to show the user Devin Booker's stats:
    print("The Regular NBA Season stats of Devin Booker are: ", p4)
    # Statements to show the user Luka Doncic's stats
    print("The Regular NBA Season stats of Luka Dončić are: ", p5)
    print()

    # occurrence counter for Embiid
    p1_occ = 0
    # occurrence counter for Jokic
    p2_occ = 0
    # occurrence counter for Giannis
    p3_occ = 0
    # occurrence counter for Booker
    p4_occ = 0
    # occurrence counter for Luka
    p5_occ = 0

    """
    This for loop was created to iterate three times throughout each players stats; it would first check who has the 
    most points, then the player with the most rebounds and finally the player with the most assists
    """
    for stat in range(3):
        """
        This 'if' statement is looped through 3 times, each time it goes through the players stats checking the points, 
        rebounds and assists. After comparing this players points to all the other possible MVP candidates points stat,
        if this player has the most points, a value of '1' is added to the counter. The same process is then done for
        checking the most rebounds and assists. 
        """
        if (p1[stat] > p2[stat]) and (p1[stat] > p3[stat]) and (
                p1[stat] > p4[stat]) and (p1[stat] > p5[stat]):
            p1_occ += 1

        elif (p2[stat] > p1[stat]) and (p2[stat] > p3[stat]) and (
                p2[stat] > p4[stat]) and (p2[stat] > p5[stat]):
            p2_occ += 1

        elif (p3[stat] > p1[stat]) and (p3[stat] > p2[stat]) and (
                p3[stat] > p4[stat]) and (p3[stat] > p5[stat]):
            p3_occ += 1

        elif (p4[stat] > p1[stat]) and (p4[stat] > p2[stat]) and (
                p4[stat] > p3[stat]) and (p4[stat] > p5[stat]):
            p4_occ += 1

        elif (p5[stat] > p1[stat]) and (p5[stat] > p2[stat]) and (
                p5[stat] > p3[stat]) and (p5[stat] > p4[stat]):
            p5_occ += 1

    # all the counters for each of the players are placed into a list
    occurrences = [p1_occ, p2_occ, p3_occ, p4_occ, p5_occ]
    # max_val holds the value of the highest number of occurrences from the list of counters
    max_val = max(occurrences)
    # index is a variable set to hold the index value of the player that had the most occurrences
    index = occurrences.index(max_val)

    """
    If the max_val is equivalent to the value of one, that would mean that there were three players that each either had
    the most points, most rebounds or most assists.
    # e.g) Embiid == 1, Jokic, == 1 and Luka == 1 ; this would mean that each of these players had a high value in 
    either of the three stats that are being compared
    """
    # set the code to a variable so that it can be used as a boolean for future uses
    tie = (max_val == 1)

    # variable to hold condition of the players points not being the same as each-others
    check_points = (p1[0] != p2[0]) and (p1[0] != p3[0]) and (p1[0] != p4[0]) and (p1[0] != p5[0]) and (
            p2[0] != p3[0]) and (p2[0] != p4[0]) and (p2[0] != p5[0]) and (p3[0] != p4[0]) and \
                   (p3[0] != p5[0]) and (p4[0] != p5[0])
    # variable to hold condition of the players rebounds not being the same as each-others
    check_rebounds = (p1[1] != p2[1]) and (p1[1] != p3[1]) and (p1[1] != p4[1]) and (p1[1] != p5[1]) and (
            p2[1] != p3[1]) and (p2[1] != p4[1]) and (p2[1] != p5[1]) and (p3[1] != p4[1]) and \
                     (p3[1] != p5[1]) and (p4[1] != p5[1])
    # variable to hold condition of the players assists not being the same as each-others
    check_assists = (p1[2] != p2[2]) and (p1[2] != p3[2]) and (p1[2] != p4[2]) and (p1[2] != p5[2]) and (
            p2[2] != p3[2]) and (p2[2] != p4[2]) and (p2[2] != p5[2]) and (p3[2] != p4[2]) and \
                    (p3[2] != p5[2]) and (p4[2] != p5[2])

    # entering the if statement only if we have a tie amongst three players
    if tie == True:
        """
        To break the tie we are going in order of points,rebounds than assists, because at the end of the day in a game 
        whoever contributes the most points is the player that was the most valuable to the teams chances at having the 
        higher score
        """

        # entering the if-statement only if everyone has different amount of points averaged
        # checking if boolean is true
        if check_points == True:
            # winner chosen based off the most points scored because points are more valuable than rebounds and assists
            if (p1[0] >= p2[0]) and (p1[0] >= p3[0]) and (p1[0] >= p4[0]) and (p1[0] >= p5[0]):
                print(f"Joel Embiid is the MVP with: {p1[0]} points, {p1[1]} rebounds & {p1[2]} assists! ")
            elif (p2[0] >= p1[0]) and (p2[0] >= p3[0]) and (p2[0] >= p4[0]) and (p2[0] >= p5[0]):
                print(f"Nikola Jokić is the MVP with: {p2[0]} points, {p2[1]} rebounds & {p2[2]} assists! ")
            elif (p3[0] >= p1[0]) and (p3[0] >= p2[0]) and (p3[0] >= p4[0]) and (p3[0] >= p5[0]):
                print(f"Giannis Antetokounmpo is the MVP with: {p3[0]} points, {p3[1]} rebounds & {p3[2]} assists! ")
            elif (p4[0] >= p1[0]) and (p4[0] >= p2[0]) and (p4[0] >= p3[0]) and (p4[0] >= p5[0]):
                print(f"Devin Booker is the MVP with: {p4[0]} points, {p4[1]} rebounds & {p4[2]} assists! ")
            elif (p5[0] >= p1[0]) and (p5[0] >= p2[0]) and (p5[0] >= p3[0]) and (p5[0] >= p4[0]):
                print(f"Luka Dončić is the MVP with: {p5[0]} points, {p5[1]} rebounds & {p5[2]} assists! ")
        # entering the elif-statement only if everyone has different amount of rebounds averaged
        elif check_rebounds == True:
            # winner chosen based off the most rebounds caught because rebounds are more valuable than assists
            if (p1[1] >= p2[1]) and (p1[1] >= p3[1]) and (p1[1] >= p4[1]) and (p1[1] >= p5[1]):
                print(f"Joel Embiid is the MVP with: {p1[0]} points, {p1[1]} rebounds & {p1[2]} assists! ")
            elif (p2[1] >= p1[1]) and (p2[1] >= p3[1]) and (p2[1] >= p4[1]) and (p2[1] >= p5[1]):
                print(f"Nikola Jokić is the MVP with: {p2[0]} points, {p2[1]} rebounds & {p2[2]} assists! ")
            elif (p3[1] >= p1[1]) and (p3[1] >= p2[1]) and (p3[1] >= p4[1]) and (p3[1] >= p5[1]):
                print(f"Giannis Antetokounmpo is the MVP with: {p3[0]} points, {p3[1]} rebounds & {p3[2]} assists! ")
            elif (p4[1] >= p1[1]) and (p4[1] >= p2[1]) and (p4[1] >= p3[1]) and (p4[1] >= p5[1]):
                print(f"Devin Booker is the MVP with: {p4[0]} points, {p4[1]} rebounds & {p4[2]} assists! ")
            elif (p5[1] >= p1[1]) and (p5[1] >= p2[1]) and (p5[1] >= p3[1]) and (p5[1] >= p4[1]):
                print(f"Luka Dončić is the MVP with: {p5[0]} points, {p5[1]} rebounds & {p5[2]} assists! ")
        # entering the elif-statement only if everyone has different amount of assists averaged
        elif check_assists == True:
            if (p1[2] >= p2[2]) and (p1[2] >= p3[2]) and (p1[2] >= p4[2]) and (p1[2] >= p5[2]):
                print(f"Joel Embiid is the MVP with: {p1[0]} points, {p1[1]} rebounds & {p1[2]} assists! ")
            elif (p2[2] >= p1[2]) and (p2[2] >= p3[2]) and (p2[2] >= p4[2]) and (p2[2] >= p5[2]):
                print(f"Nikola Jokić is the MVP with: {p2[0]} points, {p2[1]} rebounds & {p2[2]} assists! ")
            elif (p3[2] >= p1[2]) and (p3[2] >= p2[2]) and (p3[2] >= p4[2]) and (p3[2] >= p5[2]):
                print(f"Giannis Antetokounmpo is the MVP with: {p3[0]} points, {p3[1]} rebounds & {p3[2]} assists! ")
            elif (p4[2] >= p1[2]) and (p4[2] >= p2[2]) and (p4[2] >= p3[2]) and (p4[2] >= p5[2]):
                print(f"Devin Booker is the MVP with: {p4[0]} points, {p4[1]} rebounds & {p4[2]} assists! ")
            elif (p5[2] >= p1[2]) and (p5[2] >= p2[2]) and (p5[2] >= p3[2]) and (p5[2] >= p4[2]):
                print(f"Luka Dončić is the MVP with: {p5[0]} points, {p5[1]} rebounds & {p5[2]} assists! ")
    # else-statement is entered into if there wasn't a tie amongst the players' occurrence values
    else:
        # using the index value of the player with the most occurrences we can determine the mvp of the season
        if index == 0:
            print(
                f"Joel Embiid is the MVP with: {p1[0]} points, {p1[1]} rebounds & {p1[2]} assists! ")
        elif index == 1:
            print(
                f"Nikola Jokić is the MVP with: {p2[0]} points, {p2[1]} rebounds & {p2[2]} assists! ")
        elif index == 2:
            print(
                f"Giannis Antetokounmpo is the MVP with: {p3[0]} points, {p3[1]} rebounds & {p3[2]} assists! ")
        elif index == 3:
            print(
                f"Devin Booker is the MVP with: {p4[0]} points, {p4[1]} rebounds & {p4[2]} assists! ")
        elif index == 4:
            print(
                f"Luka Dončić is the MVP with: {p5[0]} points, {p5[1]} rebounds & {p5[2]} assists! ")


if __name__ == '__main__':
    mvp_finder()
    print()
    # comparing input to the string "EXIT"
    end_program = str(input("Type 'END' to end the program! "))
    if "END" == end_program:
        exit()
