ratings = [1200, 1350, 1448, 1300, 1500]
maxi = ratings[0]
mini = ratings[0]
total = 0
for x in ratings:
    if x > maxi:
        maxi = x
    if x < mini:
        mini = x
    total+=x
print(f"The highest rating is {maxi} and minimum is {mini}, The average rating is {total/len(ratings)} and the number of ratings are {len(ratings)}")