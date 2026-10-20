Characters = 0
WordCount = 0
Lines = 0
Sentences = 0
Longest_Word = 0
MostFreqWord= 0

with open("Day_to_Day Projects/Day_07/Practice/Data/input.txt", "r") as file:
    content = file.read()
    chars = len(content)
    words = content.strip()
    words = content.split()
    WordCount = len(words)
    Lines = len(content.splitlines())
    for c in content:
        if c=='.' or c=='?' or c=='!':
            Sentences+=1
    mydict = {}
    Longest_Word = words[0]
    for word in words:
        if(len(word) > len(Longest_Word)):
            Longest_Word = word
        vord = word.lower()
        if vord in mydict:
            mydict[vord]+=1
        else :
            mydict[vord] = 1
    MostFreqWord = words[0].lower()
    for key, value in mydict.items():
        if value > mydict[MostFreqWord]:
            MostFreqWord = key
with open("Day_to_Day Projects/Day_07/Practice/Data/Report.txt", "w") as file:
    file.write(f"Document Analysis\n======================================\nCharacters : {chars}\nWords : {WordCount}\nLines : {Lines}\nSentences : {Sentences}\nLongest Word : {Longest_Word}\nMost Frequent Word : {MostFreqWord}")