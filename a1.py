"""
Objective:
---------
Determine the MVP of the 2021–2022 NBA Regular Season using ONLY three basic statistics:
- Points per game
- Rebounds per game
- Assists per game

This simulates the perspective of an average viewer watching games without advanced analytics.

Rules:
------
1. For each category (points, rebounds, assists), the player with the highest value earns 1 "category win".
2. The player with the most category wins becomes the MVP.
3. If there is a tie where each tied player only wins one category (max_val == 1), 
   we break the tie using the following priority:
        points > rebounds > assists
   because scoring is the most critical contributor to winning games.
"""

def mvp_finder():
    """
    This function compares NBA player stats, counts category wins, detects ties,
    applies tie-breaker rules, and prints the MVP.
    """

    # ---------------------------------------------------------
    # PLAYERS AND THEIR STATS (points, rebounds, assists)
    # ---------------------------------------------------------
    # Using a list of dictionaries to make player access clearer and scalable
    players = [
        {"name": "Joel Embiid",           "stats": [30.6, 11.7, 4.2]},
        {"name": "Nikola Jokić",          "stats": [27.1, 13.8, 7.9]},
        {"name": "Giannis Antetokounmpo", "stats": [29.9, 11.6, 5.8]},
        {"name": "Devin Booker",          "stats": [26.8,  5.0, 4.8]},
        {"name": "Luka Dončić",           "stats": [28.4,  9.1, 8.7]},
    ]

    # SAMPLE TEST CASE (2010–2011 MVP Race)
    # Uncomment to test the older season
    # players = [
    #     {"name": "Derrick Rose",   "stats": [25.0, 4.1, 7.7]},
    #     {"name": "Dwight Howard",  "stats": [22.9,14.1, 1.4]},
    #     {"name": "LeBron James",   "stats": [26.7, 7.5, 7.0]},
    #     {"name": "Kobe Bryant",    "stats": [25.3, 5.1, 4.7]},
    #     {"name": "Kevin Durant",   "stats": [27.7, 6.8, 2.7]},
    # ]

    # ---------------------------------------------------------
    # PRINT ALL PLAYER STATS FOR USER VISIBILITY
    # ---------------------------------------------------------
    print("Regular NBA Season average stats (points, rebounds, assists):\n")
    for player in players:
        print(f"{player['name']}: {player['stats']}")
    print()

    # Number of players (helps generalize if more players are added)
    num_players = len(players)

    # occurrences[i] = number of categories won by player i
    occurrences = [0] * num_players

    # ---------------------------------------------------------
    # STEP 1 — COUNT CATEGORY WINS
    # ---------------------------------------------------------
    # Each stat index represents:
    #   0 = points
    #   1 = rebounds
    #   2 = assists
    for stat_index in range(3):

        # Extract this stat for all players into a list
        # Example: for points → [30.6, 27.1, 29.9, 26.8, 28.4]
        current_stat_values = [
            player["stats"][stat_index] for player in players
        ]

        # Highest value in this category
        max_value = max(current_stat_values)

        # Only increase wins if there is a UNIQUE category leader
        if current_stat_values.count(max_value) == 1:
            winner_index = current_stat_values.index(max_value)
            occurrences[winner_index] += 1

    # ---------------------------------------------------------
    # STEP 2 — CHECK IF THERE IS A CLEAR WINNER
    # ---------------------------------------------------------
    max_val = max(occurrences)             # highest number of category wins
    index_of_max = occurrences.index(max_val)  # player who achieved that

    # A tie occurs when max_val == 1 → no one dominated more than one category
    tie = (max_val == 1)

    # ---------------------------------------------------------
    # STEP 3 — HANDLE TIE WITH TIE-BREAKER LOGIC
    # ---------------------------------------------------------
    if tie:
        """
        Tie-breaker priority:
            1. Points
            2. Rebounds
            3. Assists
        
        For each stat, we check if EVERY player has a DIFFERENT value.
        If so, the highest value wins.
        This prevents ambiguous tie-breaking when two players tie in a stat.
        """

        # Check stats in order of importance
        for stat_index in [0, 1, 2]:

            # Grab all values for this stat across all players
            stat_values = [player["stats"][stat_index] for player in players]

            # If all values are unique → safe to pick the max stat leader
            if len(set(stat_values)) == len(stat_values):
                max_value = max(stat_values)
                winner_index = stat_values.index(max_value)
                winner = players[winner_index]

                # Extract stats for print formatting
                pts, reb, ast = winner["stats"]
                print(f"{winner['name']} is the MVP with: {pts} points, {reb} rebounds & {ast} assists!")
                break

    # ---------------------------------------------------------
    # STEP 4 — CLEAR WINNER WITHOUT TIE
    # ---------------------------------------------------------
    else:
        winner = players[index_of_max]
        pts, reb, ast = winner["stats"]
        print(f"{winner['name']} is the MVP with: {pts} points, {reb} rebounds & {ast} assists!")

if __name__ == '__main__':
    mvp_finder()
    print()

    # Simple exit mechanic
    end_program = input("Type 'END' to end the program! ")

    if end_program == "END":
        exit()
