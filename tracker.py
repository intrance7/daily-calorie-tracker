# ==================================================
#            DAILY CALORIE TRACKER
# --------------------------------------------------
# Project: Daily Calorie Tracker
# Author : Tanishq Sethi
# Date   : 04-10-2025
# Roll No: 2501410009
# --------------------------------------------------
# Description:
# This program allows users to track their daily meals
# and calorie intake. It calculates total and average
# calories, compares them with a user-defined limit,
# and provides warnings if the limit is exceeded.
# Users can optionally save the report to a file.
# ==================================================

# -------------------- START OF PROGRAM --------------------

# Welcome message
print("\n================ Welcome to the Daily Calorie Tracker! ================\n")
print("Track your meals and calorie intake easily.\n")

# -------------------- USER INPUT --------------------

# Ask for user's name
name = input("Enter your name: ")

n = int(input("How many meals do you want to enter?: "))

meals = []
calories = []

for i in range(n):
    meal = input(f"Enter name of meal {i+1}: ")
    while True:  # Validate calorie input
        try:
            cal = float(input(f"Enter calories for {meal}: "))
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value for calories.")
    meals.append(meal)
    calories.append(cal)

# -------------------- CALCULATIONS --------------------

total = sum(calories)
average = total / n

while True:
    try:
        limit = float(input("Enter your daily calorie limit: "))
        break
    except ValueError:
        print("Invalid input! Please enter a numeric value for the limit.")  

# -------------------- DISPLAY DAILY REPORT --------------------

print("\n======================= DAILY REPORT =======================")
print(f"Name: {name}")
print(f"{'Meal Name':<15} {'Calories':>8}")
print("-" * 28)
for i in range(n):
    print(f"{meals[i]:<15} {calories[i]:>8}")
print("-" * 28)
print(f"Total:          {total}")
print(f"Average:        {average:.2f}")

# Check if total calories exceed the limit
if total > limit:
    print(f"⚠ Warning: You crossed your daily limit of {limit}!")
else:
    print(f"✅ Good: You are within your {limit} calorie limit.")

# -------------------- SAVE REPORT TO FILE --------------------

save = input("\nDo you want to save this report to a file? (yes/no): ")
if save.lower() == "yes":
    with open("calorie_log.txt", "a") as f:
        f.write("======================= DAILY REPORT =======================\n")
        f.write(f"Name: {name}\n")
        f.write(f"{'Meal Name':<15} {'Calories':>8}\n")
        f.write("-" * 28 + "\n")
        for i in range(n):
            f.write(f"{meals[i]:<15} {calories[i]:>8}\n")
        f.write("-" * 28 + "\n")
        f.write(f"Total:          {total}\n")
        f.write(f"Average:        {average:.2f}\n")
        if total > limit:
            f.write(f"⚠ Warning: You crossed your daily limit of {limit}!\n")
        else:
            f.write(f"✅ Good: You are within your {limit} calorie limit.\n")
        f.write("\n")  # Blank line for the next report
    print("Report saved to calorie_log.txt")

# -------------------- END OF PROGRAM --------------------
print(f"\nThank you {name} for using Daily Calorie Tracker!")
print("====================================================================")
