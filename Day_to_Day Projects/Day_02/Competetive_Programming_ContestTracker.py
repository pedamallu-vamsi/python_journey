n = int(input("How many contests did you participate in? "))
problems = 0
sum = 0
maxRating = 0
no3 = 0
for i in range(n):
    a = int(input(f"Enter contest {i}'s rating : "))
    b = int(input(f"Enter no.of problems solved in contest {i} : "))
    sum+=a
    maxRating = max(maxRating, a)
    problems+=b
    if b>=3 :
        no3 = no3+1
avg = sum/n
avgRating = sum/n
if avg>=1500:
    avg = "Excellent"
elif avg>=1200:
    avg = "Good"
elif avg>=900:
    avg = "Developing"
else:
    avg = "Beginner"
print(f"You rating is {avgRating} and you are a {avg}")
print(f"You have solved a total of {problems} problems")
print(f"You acheived a peak rating of {maxRating}")
print(f"You have solved atleast 3 problems in {no3} contests")