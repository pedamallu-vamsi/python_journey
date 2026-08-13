def isVowel(c):
    c = c.lower()
    if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
        return True
    else:
        return False

n=int(input("Enter the number of lines in the paragraph : "))
print(f"Enter {n} lines seperated by new lines")
para = ""
for i in range(n):
    s = input()
    para += s
para = para.strip()
words = para.split()
para = " ".join(words)
sentences = para.count(".")+para.count("?")+para.count("!")
print(f"Total no.of characters are {len(para)}, The no.of words are {len(words)} and the number of sentences are {sentences}")
vowels = 0
consonants = 0
digits=0
for x in para:
    if(x.lower() >='a' and x.lower()<='z'):
        if isVowel(x):
            vowels+=1
        else:
            consonants+=1
    elif x.isdigit():
        digits+=1
spaces = len(words)-1
search = input("Enter a word you want to search for in the paragraph : ")
search = search.lower()
x = para.lower()
if search in x:
    print(f"{search} occurs {x.count(search)} times in the entered paragraph")
else:
    print(f"{search} does not exist in the paragraph")
print(f"The no.of spaces in the paragraph is {spaces}")
print(f"The upper case paragraph is {para.upper()}")
print(f"The lower case paragraph is {para.lower()}")
print(f"The cleaned paragraph is {para}")
print(f"The reversed paragraph is {para[::-1]}")