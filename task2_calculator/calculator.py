import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("=====================================")
    print("         🧮 CODSOFT CALCULATOR        ")
    print("=====================================\n")

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return "❌ Division by Zero!" if b == 0 else round(a / b, 2)

def calculator():
    while True:
        clear_screen()
        banner()
        print("Choose Operation:")
        print("1️⃣  Addition")
        print("2️⃣  Subtraction")
        print("3️⃣  Multiplication")
        print("4️⃣  Division")
        print("5️⃣  Exit\n")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("\n👋 Exiting Calculator. See you soon!")
            time.sleep(1)
            break

        try:
            a = float(input("\nEnter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("⚠️ Invalid input! Please enter numeric values.")
            time.sleep(1.5)
            continue

        if choice == '1':
            print(f"✅ Result: {a} + {b} = {add(a, b)}")
        elif choice == '2':
            print(f"✅ Result: {a} - {b} = {sub(a, b)}")
        elif choice == '3':
            print(f"✅ Result: {a} × {b} = {mul(a, b)}")
        elif choice == '4':
            print(f"✅ Result: {a} ÷ {b} = {div(a, b)}")
        else:
            print("⚠️ Invalid choice. Please select between 1–5.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    calculator()
