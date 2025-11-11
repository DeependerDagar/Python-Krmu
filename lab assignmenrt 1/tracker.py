"""
Name: <Deepender>
Course: B.Tech CSE AIML
Subject: Programming for Problem Solving using Python
Project: Daily Calorie Tracker (CLI)
Date: Nov 2025
"""

print("======================================")
print("   DAILY CALORIE TRACKER - PYTHON CLI")
print("======================================\n")
print("This program helps you log meals and track your daily calories.\n")

meals = []
calories = []

num = int(input("How many meals did you eat today? "))

for i in range(num):
    meal_name = input(f"Enter meal {i+1} name: ")
    cal = float(input(f"Enter calories for {meal_name}: "))
    meals.append(meal_name)
    calories.append(cal)

total = sum(calories)
average = total / len(calories)

limit = float(input("\nEnter your daily calorie limit: "))

if total > limit:
    status = "Exceeded"
    print("\n⚠ WARNING: You have exceeded your daily limit!")
else:
    status = "Within Limit"
    print("\n✅ Good job! You're within the limit.")

print("\n=========== SUMMARY REPORT ===========\n")
print("Meal Name\tCalories")
print("--------------------------------------")
for i in range(len(meals)):
    print(f"{meals[i]}\t\t{calories[i]}")
print("--------------------------------------")
print(f"Total:\t\t{total}")
print(f"Average:\t{average:.2f}")
print(f"Status:\t\t{status}")

save = input("\nDo you want to save this report? (yes/no): ").lower()
if save == "yes":
    from datetime import datetime
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("calorie_log.txt", "a") as f:
        f.write("Daily Calorie Tracker Log\n")
        f.write(f"Timestamp: {time}\n\n")
        f.write("Meal Name\tCalories\n")
        f.write("----------------------------------\n")
        for i in range(len(meals)):
            f.write(f"{meals[i]}\t\t{calories[i]}\n")
        f.write("----------------------------------\n")
        f.write(f"Total:\t\t{total}\n")
        f.write(f"Average:\t{average:.2f}\n")
        f.write(f"Status:\t\t{status}\n")
    print("\n✅ Log saved to calorie_log.txt")

print("\nThank you for using the Calorie Tracker!")