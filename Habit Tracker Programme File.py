def greet_user():
    name = input("Enter your name: ")
    print("Welcome,", name + "!")
    return name


def add_habit(habits):
    habit_name = input("Enter a habit name: ")

    if habit_name in habits:
        print("That habit already exists.")
        return

    try:
        target = int(input("Enter weekly target for this habit: "))

        if target <= 0:
            print("Target must be greater than 0.")
            return

        habits[habit_name] = {
            "target": target,
            "total": 0
        }

        print("Habit added successfully.")

    except ValueError:
        print("Invalid input. Please enter a number for the target.")


def log_today(habits):
    if not habits:
        print("No habits found. Please add a habit first.")
        return

    habit_name = input("Which habit did you complete today? ")

    if habit_name in habits:
        habits[habit_name]["total"] += 1
        print(habit_name, "has now been completed", habits[habit_name]["total"], "time(s).")
    else:
        print("Habit not found.")


def show_habits(habits):
    if not habits:
        print("No habits to show.")
        return

    print("\n===== Your Habits =====")

    for habit_name, data in habits.items():
        target = data["target"]
        total = data["total"]
        percentage = (total / target) * 100

        print("Habit:", habit_name)
        print("Weekly Target:", target)
        print("Total Completed:", total)
        print("Progress: {:.1f}%".format(percentage))
        print("------------------------")


def show_summary(habits):
    if not habits:
        print("No habits to summarise.")
        return

    print("\n===== Summary Report =====")

    overall_total = 0
    overall_target = 0

    for habit_name, data in habits.items():
        target = data["target"]
        total = data["total"]
        percentage = (total / target) * 100

        overall_total += total
        overall_target += target

        print(habit_name)
        print("  Target:", target)
        print("  Completed:", total)
        print("  Percentage achieved: {:.1f}%".format(percentage))

    if overall_target > 0:
        overall_percentage = (overall_total / overall_target) * 100
    else:
        overall_percentage = 0

    print("\nOverall completions:", overall_total)
    print("Overall target:", overall_target)
    print("Overall progress: {:.1f}%".format(overall_percentage))


def save_habits(habits, filename="habits.txt"):
    file = open(filename, "w")

    for habit_name, data in habits.items():
        line = (
            habit_name
            + ", target="
            + str(data["target"])
            + ", total="
            + str(data["total"])
            + "\n"
        )
        file.write(line)

    file.close()
    print("Habits saved to", filename)


def main():
    habits = {}

    greet_user()

    while True:
        print("\n===== Habit Tracker Menu =====")
        print("1. Add Habit")
        print("2. Log Daily Habit Completion")
        print("3. View All Habits")
        print("4. Show Summary")
        print("5. Save Habits to File")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_habit(habits)

        elif choice == "2":
            log_today(habits)

        elif choice == "3":
            show_habits(habits)

        elif choice == "4":
            show_summary(habits)

        elif choice == "5":
            save_habits(habits)

        elif choice == "6":
            save_habits(habits)
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


print("Habit Tracker Program")
print("© 2026 All Rights Reserved")

main()
