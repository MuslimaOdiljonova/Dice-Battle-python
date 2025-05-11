import random

def roll():
    return random.randint(1, 6)

while True:
    players = input("Enter the number of players (2 to 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
    print("Invalid input. Please enter a number between 2 and 4.")

player_names = []
for i in range(players):
    name = input(f"Enter name for Player {i + 1}: ")
    player_names.append(name)

MAX_SCORE = 50
scores = [0] * players
current = 0

while max(scores) < MAX_SCORE:
    print(f"\n{player_names[current]}'s turn:")
    turn_total = 0

    while True:
        input("Press Enter to roll the dice...")
        result = roll()
        print(f"🎲 You rolled a {result}.")

        if result == 1:
            print("No luck! You rolled a 1 and lost all turn points.")
            break
        else:
            turn_total += result
            print(f"Current turn total: {turn_total}")
            again = input("Roll again? (y/n): ").strip().lower()
            if again != 'y':
                break

    scores[current] += turn_total
    print(f"{player_names[current]}'s total score: {scores[current]}")

    if scores[current] >= MAX_SCORE:
        print(f"\n🎉 {player_names[current]} wins the game with {scores[current]} points!")
        break

    current = (current + 1) % players
