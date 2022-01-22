import random

i = 0
player_won = 0
computer_won = 0
m = 0
while i < 10:

    random_Random_word = ["Snake", "Water", "Gun"]
    Random_word = random.choice(random_Random_word)
    n = input("You have only 10 chances to play \nEnter the your choice from Snake , Gun , Water :")
    m += 1

    if n == "Snake" and Random_word == "Water":
        print("You Won..!! computer has chosen Water")
        player_won += 1
    elif Random_word == "Snake" and n == "Water":
        print("You Lost ! computer has chosen Snake")
        computer_won += 1
    elif n == "Water" and Random_word == "Gun":
        print("You won ..!! computer has chosen Gun")
        player_won += 1
    elif Random_word == "Water" and n == "Gun":
        print("You Lost ! computer has chosen Water")
        computer_won += 1
    elif n == "Gun" and Random_word == "Snake":
        print("You Won..!! computer has chosen Snake")
        player_won += 1
    elif Random_word == "Gun" and n == "Snake":
        print("You Lost..!! computer has chosen Gun")
        computer_won += 1
    elif Random_word == "Gun" and n == "Gun":
        print("Play again both had inputed same thing")
    elif Random_word == "Snake" and n == "Snake":
        print("Play again both had inputed same thing")
    elif Random_word == "Water" and n == "Water":
        print("Play again both had inputed same thing")
    print(f"{10 - m} chances left be confident")
    i += 1

print(f"You won {player_won} times")
print(f"computer won {computer_won} times")
if player_won > computer_won:
    print("Human has won the game")
elif player_won == computer_won:
    print("Tie....!!!")
else:
    print("Computer has won the match")