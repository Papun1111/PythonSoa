import random

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def simulate_craps(num_games=1000000):
    rolls = {}  # Track both wins and losses in a single dictionary
    
    for _ in range(num_games):
        roll_count = 0
        point = roll_dice()
        roll_count += 1
        
        # Check for instant win/loss on the first roll
        if point in {7, 11}:  # Win on first roll
            rolls[roll_count] = rolls.get(roll_count, (0, 0))[0] + 1, rolls.get(roll_count, (0, 0))[1]
        elif point in {2, 3, 12}:  # Loss on first roll
            rolls[roll_count] = rolls.get(roll_count, (0, 0))[0], rolls.get(roll_count, (0, 0))[1] + 1
        else:
            # Keep rolling until player wins or loses
            while True:
                new_roll = roll_dice()
                roll_count += 1
                if new_roll == point:  # Win on this roll
                    rolls[roll_count] = rolls.get(roll_count, (0, 0))[0] + 1, rolls.get(roll_count, (0, 0))[1]
                    break
                elif new_roll == 7:  # Loss on this roll
                    rolls[roll_count] = rolls.get(roll_count, (0, 0))[0], rolls.get(roll_count, (0, 0))[1] + 1
                    break
    
    total_wins = sum(w for w, _ in rolls.values())
    total_losses = sum(l for _, l in rolls.values())
    
    # Display the percentages and resolved statistics
    print(f"Percentage of wins: {total_wins / num_games * 100:.1f}%")
    print(f"Percentage of losses: {total_losses / num_games * 100:.1f}%")
    
    print("\nPercentage of wins/losses based on total number of rolls:")
    print("Rolls | % Resolved on this roll | Cumulative % of games resolved")
    print("------------------------------------------------------------------")
    
    total_resolved = total_wins + total_losses
    cumulative_percentage = 0
    for roll in range(1, max(rolls.keys()) + 1):
        resolved_on_this_roll = rolls.get(roll, (0, 0))[0] + rolls.get(roll, (0, 0))[1]
        resolved_percentage = (resolved_on_this_roll / num_games) * 100
        cumulative_percentage += resolved_percentage
        print(f"{roll} | {resolved_percentage:.2f}% | {cumulative_percentage:.2f}%")

# Run the simulation
simulate_craps()
