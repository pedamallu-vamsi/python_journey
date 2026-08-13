s = input("Enter a string : ")
words = s.split()
for i in range(len(words)):
    words[i] = words[i][::-1]
s = " ".join(words)
print(f"The words reversed string is {s}")