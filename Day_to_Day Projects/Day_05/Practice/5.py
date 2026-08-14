product = {}
n = int(input("Enter no.of products : "))
for i in range(n):
    s = input(f"Enter product {i+1} name : ")
    k = int(input(f"Enter the quantity of {s} : "))
    product[s] = k

y = int(input("Do you wanna add a product ? (0 for no, 1 for yes) : "))
if y==1:
    s = input(f"Enter product name : ")
    k = int(input(f"Enter the quantity of {s} : "))
    product[s] = k
y = int(input("Do you wanna update the quantitiy of any product ? (0 for no, 1 for yes) : "))
if y==1:
    s = input(f"Enter product name : ")
    k = int(input(f"Enter the updated quantity of {s} : "))
    product[s] = k
y = input("Enter the name of the product you want to search for : ")
if y in product :
    print(f"{y} exists in the dictionary")
else:
    print(f"{y} does NOT exist in the dictionary")
print()
print("The final dictionary is")
for key,value in product.items():
    print(f"{key} : {value}")