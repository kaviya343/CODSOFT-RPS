import random

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

choices = [ROCK, PAPER, SCISSORS]

user_score = 0
computer_score = 0
round_number = 1

print("=" * 55)
print("      ROCK • PAPER • SCISSORS CHALLENGE")
print("=" * 55)
print("Instructions:")
print("Type Rock, Paper or Scissors to play.")
print("Type Exit anytime to quit.")
print("-" * 55)

while True:

    print(f"\nRound {round_number}")

    user_choice = input(
        "Enter your choice (Rock/Paper/Scissors): "
    ).lower().strip()

    if user_choice == "exit":
        break

    if user_choice not in choices:
        print("Invalid choice! Try again.")
        continue

    computer_choice = random.choice(choices)

    print(f"\nYour Choice     : {user_choice.capitalize()}")
    print(f"Computer Choice : {computer_choice.capitalize()}")

    if user_choice == computer_choice:
        print("\nResult : Match Tied!")

    elif (
        (user_choice == ROCK and computer_choice == SCISSORS)
        or
        (user_choice == PAPER and computer_choice == ROCK)
        or
        (user_choice == SCISSORS and computer_choice == PAPER)
    ):
        print("\nResult : You Won This Round!")
        user_score += 1

    else:
        print("\nResult : Computer Won This Round!")
        computer_score += 1

    print("\nCurrent Score")
    print("-" * 25)
    print(f"You      : {user_score}")
    print(f"Computer : {computer_score}")

    play_again = input(
        "\nDo you want to play another round? (yes/no): "
    ).lower().strip()

    if play_again != "yes":
        break

    round_number += 1

print("\n" + "=" * 55)
print("                 GAME SUMMARY")
print("=" * 55)

print(f"Your Score      : {user_score}")
print(f"Computer Score  : {computer_score}")

if user_score > computer_score:
    print("\nOverall Winner : You")
elif computer_score > user_score:
    print("\nOverall Winner : Computer")
else:
    print("\nOverall Result : Draw")

print("\nThank you for playing!")