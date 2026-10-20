count = 1
with open("Day_to_Day Projects/Day_07/Practice/Data/Subjects.txt", "r") as file:
    for line in file:
        print(f"{count}. {line}", end="")
        count+=1