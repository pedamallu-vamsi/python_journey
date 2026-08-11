list = ["DBMS", "OS", "Cpp", "Java", "Python"]
x = input("Enter the subject you want to search in list")
if x in list:
    print(f"{x} is present in the list")
else:
    print(f"{x} is not present in the list")