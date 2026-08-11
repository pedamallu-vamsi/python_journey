n = int(input("How many messages : "))
user_messages = []
Ai_messages = []
Longest_Message = ""
userWords = 0
AiWords = 0
convo = []
for i in range(n):
    s = input("Enter the message : ")
    k = int(input("The above message was sent by ? (0 for AI, 1 for User) : "))
    if k==0 :
        Ai_messages.append(s)
        AiWords += len(s.split())
        convo.append("AI : " + s)
    else:
        user_messages.append(s)
        userWords += len(s.split())
        convo.append("User : " + s)
    if len(s.split()) > len(Longest_Message.split()):
        Longest_Message = s
print("======================= CHAT HISTORY =================")
print()
i=0
while i<len(convo):
    print(convo[i])
    i+=1
print()
print("========================================================")
print()
print(f"Total messages : {len(Ai_messages)+len(user_messages)}")
print(f"User Messages : {len(user_messages)}")
print(f"AI messages : {len(Ai_messages)}")
print()
print(f"User Words : {userWords}")
print(f"AI words : {AiWords}")
print()
print("Longest message: ")
print(Longest_Message)