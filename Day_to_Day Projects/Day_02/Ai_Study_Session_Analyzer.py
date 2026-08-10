n = int(input("How many study sessions did you have : "))
problems = 0
hours = 0
mostProductive = 0
comparator= -1
for i in range(n):
    subject = input(f"What subeject did you study in session {i+1} : ")
    hour = int(input(f"How many hours did you study in session {i+1} : "))
    problem = int(input(f"How many problems did you solve in session {i+1} : "))
    problems += problem
    hours += hour
    if hour >=2 and problem>=5 and (hour+problem)>comparator:
        mostProductive = i+1
        comparator = hour+problem
    if hour<2 or problem<5:
        print("This session needs improvement")
    elif hour >=3 and problem>=8:
        print("It was an highly productive hour!!")
    else:
        print("It was a productive hour :)")
print()
print(f"You studied for a total of {hours} hours!")
print(f"You solved a total of {problems} problems")
print(f"You studied for a average of {hours/n} hours per session")
print(f"Your most produtive session was session number {mostProductive}")