name = input("Enter your name : ")
college = input("Enter your college name : ")
goal = input("Enter your career goal : ")

with open("Day_to_Day Projects/Day_07/Practice/Data/profile.txt", "w") as file:
    file.write(f"{name},{college},{goal}")