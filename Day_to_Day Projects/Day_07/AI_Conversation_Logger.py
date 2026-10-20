def add_message(path, messages):
    n = int(input("Who entered the message (0 for AI, 1 for User) ? : "))
    while n!=0 and n!=1:
        n = int(input("Enter a valid input, valid inputs are 0 and 1 : "))
    message = input("Enter the message : ")
    sender = ""
    if n==0:
        sender = "AI"
    elif n==1:
        sender = "User"
    dictionary = {
        "sender" : sender,
        "message" : message
    }
    messages.append(dictionary)
    with open(path, "a") as file:
        file.write(f"{sender}: {message}\n")
def read_conversation(path):
    content = ""
    with open(path, "r") as file:
        content = file.read()
    print(content)
def analyze_conversation(messages):
    total_messages = len(messages)
    user_messages = 0
    AI_messages = 0
    total_words = 0
    longest_message = ""
    mydict = {}
    for x in messages:
        if x["sender"] == "AI":
            AI_messages += 1
        else:
            user_messages += 1
        words = x["message"].split()
        for word in words:
            word = word.lower()
            if word in mydict:
                mydict[word] += 1
            else:
                mydict[word] = 1
        total_words += len(words)
        if(len(words) > len(longest_message.split())):
            longest_message = x["message"]
    arr = messages[0]["message"].split()
    most_frequent_word = arr[0].lower()
    for key,value in mydict.items():
        if(mydict[most_frequent_word] < value):
            most_frequent_word = key
    statistics = {
        "total_messages" : total_messages,
        "user_messages" : user_messages,
        "AI_messages" : AI_messages,
        "total_words" : total_words,
        "longest_message" : longest_message,
        "most_frequent_word" : most_frequent_word
    }
    return statistics
def generate_report(path, messages):
    statistics = analyze_conversation(messages)
    with open(path, "w") as file:
        file.write(f"Total Messages : {statistics['total_messages']}\nUser Messages : {statistics['user_messages']}\nAI Messages : {statistics['AI_messages']}\nTotal Words : {statistics['total_words']}\nLongest Message : {statistics['longest_message']}\nMost Frequent Word : {statistics['most_frequent_word']}\n")
    print("\nReport has been saved to Conversation_Report.txt in the data folder!")

messages = []
n = int(input("How many messages are in this conversation  : "))
if n==0:
    print("How can you log a conversation without any messages!!")
else:
    path = "Day_to_Day Projects/Day_07/Practice/Data/Conversation.txt"
    with open(path, "w") as file:
        file.write("")
    for i in range(n):
        add_message(path, messages)
    print("\nGenerating Report.....")
    path = "Day_to_Day Projects/Day_07/Practice/Data/Conversation_Report.txt"
    generate_report(path, messages)
    path = "Day_to_Day Projects/Day_07/Practice/Data/Conversation.txt"
    print("\n===============Conversation===========")
    read_conversation(path)