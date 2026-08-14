marks = {
    "LeetCode": 1691,
    "CodeChef": 1461,
    "CodeForces": 991,
    "HackerRank": 1567
}
total = 0
count = 0
high = marks["LeetCode"]
low = marks["LeetCode"]


for key,value in marks.items():
    print(f"{key} : {value}")
    total+=value
    count+=1
    if high < value:
        high = value
    if low>value:
        low = value
print(f"Your average rating is {total/count}")
print(f"You highest rating is {high} and your lowest rating is {low}")