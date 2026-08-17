def find_largest(numbers):
    maxi = numbers[0]
    for x in numbers:
        if x > maxi:
            maxi = x
    return maxi
def find_smallest(numbers):
    mini = numbers[0]
    for x in numbers:
        if x < mini:
            mini = x
    return mini
def calculate_average(numbers):
    sum = 0
    for x in sum:
        sum+=x
    return sum/len(numbers)
n = int(input("Enter the number of numbers in list : "))
numbers = []
for i in range(n):
    x = int(input(f"Enter {i+1} number : "))
    numbers.append(x)
print(f"The largest in the list is {find_largest(numbers)}, The smallest in the list is {find_smallest(numbers)} and the average of the numbers is {calculate_average(numbers)}")