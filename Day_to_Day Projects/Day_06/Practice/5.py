def highest_rating(ratings):
    max = -123456789
    for key,value in ratings:
        max = max(max,value)
    return max

def average_rating(ratings):
    total = 0
    for key,value in ratings:
        total+=value
    return total/len(ratings)

ratings = {
    "LeetCode" : 1691,
    "CodeChef" : 1461,
    "CodeForces" : 991,
    "HackerRank" : 1567
}

print(f"The highest rating is {highest_rating(ratings)} and the average rating is {average_rating(ratings)}")