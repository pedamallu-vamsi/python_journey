def isVowel(c):
    return c=='a' or c=='e' or c=='i' or c=='o' or c=='u'
def count_words(text):
    words = text.split()
    return len(words)
def count_vowels(text):
    text = text.lower()
    count = 0
    for x in text:
        if isVowel(x):
            count+=1
    return count
def reverse_text(text):
    s = text[::-1]
    return s
text = input("Enter a string : ")
print(f"The no.of words in the entered string is {count_words(text)}, the no.of vowels is {count_vowels(text)} and the reversed string is {reverse_text(text)}")