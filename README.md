# NBA MVP Analyzer

## Overview
The **NBA MVP Analyzer** is a command-line program designed to determine the **Most Valuable Player (MVP)** of the NBA **2021-2022 Regular Season** based on fundamental statistics: **points, rebounds, and assists**. These stats represent the key performance metrics that an average basketball fan observes during a game. The program applies a rule-based comparison system to identify the best-performing player among multiple candidates.

## Features
- **Analyzes basic statistics (PPG, RPG, APG)** to determine the MVP.
- **Handles tie-breakers** by prioritizing points, rebounds, and assists in order.
- **Compares multiple player performances** and selects the most valuable contributor.
- **Simple command-line interface** with straightforward outputs.
- **Works with different datasets**, allowing for historical analysis.

## Technology Stack
- **Python**: Main programming language.
- **Standard I/O Handling**: Reads and processes input efficiently.

## Installation
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/yourusername/nba-mvp-analyzer.git
   ```
2. **Navigate to the Project Directory:**
   ```sh
   cd nba-mvp-analyzer
   ```
3. **Run the Program:**
   ```sh
   python mvp_analyzer.py
   ```

## How It Works
### Algorithm Explanation
1. **Stores predefined stats** for five NBA players (PPG, RPG, APG).
2. **Iterates through stats (points, rebounds, assists) to find leaders**.
3. **Counts occurrences** of each player leading in a category.
4. **Handles tie-breakers** by prioritizing points (since basketball is a scoring game).
5. **Prints the MVP based on the highest occurrence count or tie-break rule**.
6. **Allows user to exit program by typing 'END'**.

### Sample Output
```
The Regular NBA Season stats of Joel Embiid are: [30.6, 11.7, 4.2]
The Regular NBA Season stats of Nikola Jokić are: [27.1, 13.8, 7.9]
The Regular NBA Season stats of Giannis Antetokounmpo are: [29.9, 11.6, 5.8]
The Regular NBA Season stats of Devin Booker are: [26.8, 5.0, 4.8]
The Regular NBA Season stats of Luka Dončić are: [28.4, 9.1, 8.7]

Joel Embiid is the MVP with: 30.6 points, 11.7 rebounds & 4.2 assists!

Type 'END' to end the program!
```

## Inefficiencies & Possible Improvements
### **Current Inefficiencies:**
1. **Hardcoded player stats:**
   - The program manually stores stats in predefined lists.
   - This makes it inflexible to new data or other NBA seasons.
2. **Nested conditional checks:**
   - Uses multiple `if-elif` statements for comparisons.
   - Increases complexity and reduces maintainability.
3. **Tie-breaker implementation:**
   - Currently uses a static rule-based approach.
   - Does not dynamically adapt to more complex scenarios.

### **Optimization Strategies:**
1. **Use a Data Structure (Dictionary or JSON):**
   - Store players' stats dynamically in a dictionary instead of hardcoding lists.
   - Example:
     ```python
     players = {
         "Joel Embiid": {"PPG": 30.6, "RPG": 11.7, "APG": 4.2},
         "Nikola Jokic": {"PPG": 27.1, "RPG": 13.8, "APG": 7.9},
         "Giannis Antetokounmpo": {"PPG": 29.9, "RPG": 11.6, "APG": 5.8},
     }
     ```
   - This allows easy modifications and supports loading data from external sources.

2. **Refactor `if-elif` conditions into a loop:**
   - Instead of manually comparing each stat, loop through the dataset dynamically.
   - Example:
     ```python
     stat_categories = ["PPG", "RPG", "APG"]
     leader_counts = {player: 0 for player in players}
     
     for stat in stat_categories:
         best_player = max(players, key=lambda p: players[p][stat])
         leader_counts[best_player] += 1
     ```
   - This removes redundant `if-elif` checks, making the program more scalable.

3. **Make MVP selection dynamic:**
   - Currently, it assumes a tie-break is necessary only in some cases.
   - A weighted ranking system (e.g., assigning scores based on rank in each stat) would be more flexible.

## Future Enhancements
- **Allow user input for custom NBA stats** instead of hardcoded values.
- **Implement a web scraper** to fetch real-time NBA player statistics.
- **Integrate visualization tools (Matplotlib, Seaborn)** to represent MVP analysis graphically.
- **Use a database (SQLite/PostgreSQL)** to store historical MVP stats.
- **Enhance tie-breaking logic with advanced metrics** (e.g., player efficiency rating, usage rate).

## License
This project is licensed under the **MIT License**.

## Contact
**Author:** Aathushan Kugendran  
**Email:** aathushankugendran@gmail.com  
**GitHub:** [AathushanKugendran](https://github.com/aathushankugendran)
