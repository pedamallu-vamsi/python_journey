newGoal = input("Enter a new goal : ")
with open("Day_to_Day Projects/Day_07/Practice/Data/profile.txt", "a") as file:
    file.write(f",{newGoal}")