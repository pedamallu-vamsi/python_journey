def isVowel(c):
    c = c.lower()
    if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
        return True
    else:
        return False

s = input("Enter a string : ")
vowels = 0
consonants = 0
digits = 0
spaces = 0
s = s.lower()
for x in s:
    if x>='a' and x<='z':
        if isVowel(x):
            vowels+=1
        else:
            consonants+=1
    elif x.isdigit():
        digits+=1
    elif x == " ":
        spaces+=1
print(f"The no.of vowels are {vowels}, The no.of consonants are {consonants}, The no.of digits are {digits} and the no.of spaces are {spaces}")