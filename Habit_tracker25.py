# Habit Tracker Application
# Author: Aisha (CST0400)
# -------------------------------------------

# Dictionary to store habits
# Structure:
# habits = [
#     {"name": "Exercise", "target": 5, "total": 2}
# ]
habits = []


# ---------------- FUNCTIONS ----------------

def greet_user():
    """Greets the user by name."""
    name = input("Welcome! Please enter your name: ")
    print(f"\nHello {name}, welcome to your Habit Tracker!\n")
    return name


def add_habit():
    """Adds a new habit with a weekly target."""
    habit_name = input("Enter the name of the new habit: ")
    target = int(input("Enter your weekly target for this habit: "))
    
    habit = {
        "name": habit_name,
        "target": target,
        "total": 0
    }
    
    habits.append(habit)
    print(f"\n Habit '{habit_name}' added successfully!\n")


def log_habit():
    """Logs completion of a habit for the day."""
    if not habits:
        print("\n No habits found. Please add a habit first.\n")
        return

    print("\nWhich habit would you like to log?")
    for i, habit in enumerate(habits):
        print(f"{i+1}. {habit['name']}")

    choice = int(input("Enter the number of the habit: "))
    
    if 1 <= choice <= len(habits):
        habits[choice - 1]["total"] += 1
        print(f"\n Logged 1 day for '{habits[choice - 1]['name']}'!\n")
    else:
        print("\n Invalid choice.\n")


def view_habits():
    """Displays all habits with weekly targets and totals."""
    if not habits:
        print("\n No habits available yet.\n")
        return

    print("\n----- ALL HABITS -----")
    for habit in habits:
        print(f"Habit: {habit['name']}")
        print(f" - Weekly Target: {habit['target']}")
        print(f" - Completed: {habit['total']}\n")


def show_summary():
    """Displays progress summary with percentages."""
    if not habits:
        print("\n⚠ No habits to summarise.\n")
        return

    print("\n----- HABIT SUMMARY -----")
    for habit in habits:
        # Prevent division by zero
        if habit['target'] > 0:
            percent = (habit['total'] / habit['target']) * 100
        else:
            percent = 0

        print(f"{habit['name']}: {percent:.2f}% of weekly target achieved")
    print()


def save_to_file():
    """Saves habit data to a text file."""
    with open("habit_data.txt", "w") as file:
        file.write("Habit Tracker Data\n")
        file.write("------------------\n\n")
        for habit in habits:
            file.write(f"Habit: {habit['name']}\n")
            file.write(f"Weekly Target: {habit['target']}\n")
            file.write(f"Completed: {habit['total']}\n\n")

    print("\n Data saved to 'habit_data.txt'\n")


# ---------------- MAIN PROGRAM ----------------

def menu():
    """Displays menu and handles choices."""
    print("1. Add a new habit")
    print("2. Log today's habit completion")
    print("3. View all habits")
    print("4. View summary")
    print("5. Save and exit")


def main():
    """Main loop of the program."""
    greet_user()

    running = True
    while running:
        menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_habit()
        elif choice == "2":
            log_habit()
        elif choice == "3":
            view_habits()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            save_to_file()
            print("\nThank you for using the Habit Tracker! Goodbye!\n")
            running = False
        else:
            print("\n Invalid choice. Please choose from the menu.\n")


# Run program
main()
