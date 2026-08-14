n = int(input("Enter the no.of programmers : "))
coders = []
lchigh = 0
cchigh = 0
cfhigh = 0
probhigh =  0
total = 0
bestAvg=0
bestProgrammer = ""
for i in range(n):
    name = input(f"Enter coder {i+1}'s name : ")
    lcr = int(input("Enter LeetCode rating : "))
    ccr = int(input("Enter CodeChef rating : "))
    cfr = int(input("Enter CodeForces rating : "))
    problems = int(input("Enter the no.of problems you have solved : "))
    total += problems
    if lcr > lchigh:
        lchigh = lcr
    if ccr > cchigh:
        cchigh = ccr
    if cfr > cfhigh:
        cfhigh = cfr
    if problems > probhigh:
        probhigh = problems
    avg = (lcr+ccr+cfr)/3
    if avg > bestAvg:
        bestAvg = avg
        bestProgrammer = name
    code = {
        "name" : name,
        "LeetCode Rating" : lcr,
        "CodeChef Rating" : ccr,
        "CodeForces Rating" : cfr,
        "Problems Solved" : problems
    }
    coders.append(code)
print()
print("The names of all the coders are")
for i in range(len(coders)):
    print(coders[i]['name'], end=" ")
print()
print(f"The highest LeetCode rating is {lchigh}, highest CodeChef rating is {cchigh} and the highest CodeForces rating is {cfhigh}")
print(f"The most problems solved are {probhigh}")
print(f"The average number of problems solved by each programmer is {total/len(coders)}")
print(f"The best programmer is {bestProgrammer}")