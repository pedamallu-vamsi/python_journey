s = input("Enter a string : ")
k = input("Enter the keyword that is to be searched for in s : ")
a = s.lower()
b = k.lower()

if b in a:
    print(f"{k} exists in {s}.")
else:
    print(f"{k} does not exist in {s}.")