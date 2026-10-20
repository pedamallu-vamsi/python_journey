count = 0
lines=1
sentences = 0
words = 0
with open("Day_to_Day Projects/Day_07/Practice/Data/input.txt", "r") as file:
    content = file.read()
    for c in content:
        if c=='.' or c=='?' or c=='!':
            sentences+=1
        count+=1
        if c=='\n':
            lines+=1
    words = content.split()
print(f"Chars : {count}, Lines : {lines}, Sentences : {sentences}, words : {len(words)}")
