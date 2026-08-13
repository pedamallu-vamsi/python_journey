n=int(input("Enter the number of lines in the documents : "))
print(f"Enter {n} lines seperated by new lines")
para = ""
for i in range(n):
    s = input()
    para += " " + s
para = para.strip()
words = para.split()
para = " ".join(words)
longWord = ""
shortWord = "                                                                                                         "
for word in words:
    if len(word) > len(longWord):
        longWord = word
    if len(word) < len(shortWord):
        shortWord = word
sentences = para.count(".")+para.count("?")+para.count("!")
print(f"Total no.of characters are {len(para)}")
print(f"The no.of words are {len(words)}")
print(f"The number of sentences are {sentences}")
print(f"The average no.of words per sentence are {len(words)/sentences}")
print(f"The longest word is {longWord} and the shortest word is {shortWord}")
search = input("Enter a word you want to search for in the paragraph : ")
search = search.lower()
x = para.lower()
if search in x:
    print(f"{search} occurs {x.count(search)} times in the entered paragraph")
else:
    print(f"{search} does not exist in the paragraph")
print(f"The cleaned document is {para}")
mfword= words[0].lower()
para = para.lower()
for word in words:
    if para.count(mfword) < para.count(word.lower()):
        mfword = word
print(f"The most frequent word is {mfword}")