passWord = "JaiBob"
for i in range(3):
    trial = input("Enter your password : ")
    if(trial == passWord):
        print("Access Granted")
        break
    else:
        print(f"Access Denied, {2-i} tries remaining ")