n = int(input("How many contests did you participate in? "))
problemsC = 0
sum = 0
maxRating = 0
minRating = 1000000000
no3 = 0
contest_names = []
ratings = []
problems = []
no3_contests = []
bestContest = -1
for i in range(n):
    name = input(f"Enter contest {i} name : ")
    a = int(input(f"Enter contest {i}'s rating : "))
    b = int(input(f"Enter no.of problems solved in contest {i} : "))
    sum+=a
    if a > maxRating:
        maxRating = a
        bestContest = name
    minRating = min(minRating, a)
    problemsC+=b
    if b>=3 :
        no3 = no3+1
        no3_contests.append(name)
    contest_names.append(name)
    ratings.append(a)
    problems.append(b)
avgRating = sum/n
print("The contests are : ", end=" ")
print(contest_names)
print(f"You rating is {avgRating}")
print(f"You have solved a total of {problemsC} problems")
print(f"You acheived a peak rating of {maxRating}, minimum rating of {minRating} and your best contest was {bestContest}")
print(f"You have solved atleast 3 problems in {no3} contests which are {no3_contests}")