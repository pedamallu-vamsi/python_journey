messages = []
n = int(input("Enter the no.of messages : "))
s = ""
for i in range(n):
    sender = int(input("Who sent the message? (0 for user, 1 for AI) : "))
    if sender==0:
        sender = "User"
    else:
        sender = "AI"
    message = input("Enter the message : ")
    words = message.split()
    length = len(words)
    dictionary = {
        "sender" : sender,
        "message" : message,
        "length" : length
    }
    s+= " " + message
    messages.append(dictionary)

User_Messages = 0
Ai_Messages = 0
User_WordCount = 0
Ai_WordCount = 0
LongestMessage = ""
MostFreqWord = 0
MostActiveParticipant = ""
dictionary2 = {}
for message in messages:
    if message['sender']=="AI":
        Ai_Messages += 1
        Ai_WordCount += message['length']
    else:
        User_Messages += 1
        User_WordCount += message['length']
    if len(message['message']) > len(LongestMessage):
        LongestMessage = message['message']
s = s.lower()
words = s.split()
for word in words:
    if word in dictionary2:
        dictionary2[word]+=1
    else:
        dictionary2[word]=1
MostFreqWord = words[0]
for key,value in dictionary2.items():
    if value > dictionary2[MostFreqWord]:
        MostFreqWord=key
print(f"The total no.of messages is {len(messages)}")
print(f"The user sent {User_Messages} number of messages and the total word count of user sent messages is {User_WordCount}")
print(f"The Ai sent {Ai_Messages} number of messages and the total word count of user sent messages is {Ai_WordCount}")
print(f"The longest message is {LongestMessage}")
print(f"The most frequent word is {MostFreqWord}")
MostActiveParticipant = ""
if User_Messages > Ai_Messages :
    MostActiveParticipant = "User"
else:
    MostActiveParticipant = "Ai"
print(f"The most active participant is the {MostActiveParticipant}")
print(f"The average no.of words per message is {len(words)/n}")
for message in messages:
    print(f"{message['sender']} : {message['message']}")