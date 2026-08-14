s = input("Enter a string : ")
s = s.lower()
words = s.split()
mp = {

}
for x in words:
    if x in mp:
        mp[x]+=1
    else:
        mp[x]=1
print()
print("The frequency of the words is")
for key,value in mp.items():
    print(f"{key} : {value}")