marks = {
    "Math": 95,
    "Python": 88,
    "DBMS": 91,
    "OS": 84
}
total = 0
count = 0
high = marks["DBMS"]
low = marks["DBMS"]
highsub = "DBMS"

for key,value in marks.items():
    total+=value
    count+=1
    if high < value:
        high = value
        highsub = key
    if low>value:
        low = value
print(f"Your total marks are {total}, Average being {total/count}")
print(f"You acheived your highest marks of {high} in {highsub}")
print(f"Your lowest maks were {low}")