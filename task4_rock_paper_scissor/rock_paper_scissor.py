import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("========================================")
    print("     🎮 ROCK PAPER SCISSORS GAME        ")
    print("========================================\n")

def play_game():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    comp_score = 0
    round_number = 1

    while True:
        clear_screen()
        banner()
        print(f"⭐ Round {round_number}")
        print("Type 'q' to quit anytime.\n")
        user_choice = input("Enter rock, paper, or scissors: ").lower()

        if user_choice == 'q':
            print("\nFinal Scores:")
            print(f"🧍 You: {user_score} | 💻 Computer: {comp_score}")
            if user_score > comp_score:
                print("🏆 You are the winner!")
            elif user_score < comp_score:
                print("💻 Computer wins this time!")
            else:
                print("🤝 It's a tie overall!")
            print("\n👋 Thanks for playing!")
            time.sleep(2)
            break

        if user_choice not in choices:
            print("⚠️ Invalid input! Please choose rock, paper, or scissors.")
            time.sleep(1.5)
            continue

        computer_choice = random.choice(choices)
        print(f"\n🧍 You chose: {user_choice}")
        print(f"💻 Computer chose: {computer_choice}")
        time.sleep(1)

        if user_choice == computer_choice:
            print("🤝 It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("🎉 You win this round!")
            user_score += 1
        else:
            print("😞 Computer wins this round!")
            comp_score += 1

        print(f"\nCurrent Score -> You: {user_score} | Computer: {comp_score}")
        round_number += 1
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    play_game()
