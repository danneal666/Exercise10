print("Welcome to DanBank")

attempts = 3

UserPin = 1234

while attempts != 0:
    Pin = int(input("Please Enter 4 digit Pin: "))
    if Pin != UserPin:
        attempts -= 1
        print ("Incorrect pin number", attempts, "attempts left")
    else:
        UserChoice = input("d: Deposit or w: Withdraw: ")
        if UserChoice == "d":
            UserDeposit = input("Enter Amount: ")
            print(UserDeposit, "£ deposited successfully")
        if UserChoice == "w":
            UserWithdraw = input("Enter amount to withdraw: ")
            print(UserWithdraw, "£ Withdrawn successfully")
    UserExit = input("Would you like to continue Y/N: ")
    if UserExit == "n":
        print("Thanks for being a DanBank Customer")
        break
    else:
        continue
