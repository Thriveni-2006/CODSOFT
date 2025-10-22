import random
import string
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("=======================================")
    print("        🔐 PASSWORD GENERATOR          ")
    print("=======================================\n")

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_strength(length):
    if length < 6:
        return "Weak ❌"
    elif 6 <= length < 10:
        return "Moderate ⚠️"
    else:
        return "Strong ✅"

def main():
    while True:
        clear_screen()
        banner()
        try:
            length = int(input("Enter desired password length (e.g., 8–16): "))
            if length <= 0:
                print("⚠️ Please enter a positive number!")
                time.sleep(1.5)
                continue

            password = generate_password(length)
            print(f"\nGenerated Password: {password}")
            print(f"Password Strength: {check_strength(length)}")

        except ValueError:
            print("⚠️ Invalid input! Enter a number only.")

        again = input("\nGenerate another password? (y/n): ").lower()
        if again != 'y':
            print("\n👋 Thank you for using Password Generator!")
            time.sleep(1)
            break

if __name__ == "__main__":
    main()
