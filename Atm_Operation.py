
import random
Database = { 8705029962: ["emma"," bola","bola@gmail.com", 1234, 0]}

##INITIALIZE THE SYSTEM
def init():
    validOption = False
    while validOption == False:
        print("============================================")
        print("============Welcome to ZuriBank============")
        print("============================================") 
        accountRequest = int(input("Do you have acount with us ? \n 1. YES \n 2. NO \n"))
        if (accountRequest == 1):
            validOption = True
            login()
        elif (accountRequest == 2):
            validOption = True
            register()
        else:
            print("You have selected an invalid option")
            validOption = False


#login to the system
def login():
    print("==================================")
    print("========== *LOGIN HERE* ==========")
    print("==================================")
    validDetails = False
    while validDetails == False:
       acctNumber = int(input("Enter your account number... \n"))
       accountPin = int(input("Enter your account pin \n"))
       for accountNumber, userDetails in Database.items():
            if (acctNumber == accountNumber  and accountPin == userDetails[3]):
                bankOperation()
                validDetails = True
            else:
                print("Invalid credentials \n Please login again \n")
                validDetails = False


#logout from the system
def register():
    print("=====================================")
    print("========== *Register HERE* ==========")
    print("=====================================")
    firstName = input("Enter your first name ? \n")
    lastName = input("Enter your lasst name ? \n")
    accountEmail = input("Enter your email address ? \n ")
    accountPin = int(input("Enter your pin ? \n"))
    accountNumber = generateAccountNumber()
    currentBalance = 0

    #Adding user name, pin and account number to Database
    Database[accountNumber] = [firstName, lastName, accountEmail, accountPin, currentBalance]
    print("*******Login with your account number and pin******\n************ ensure you keep it save**************")
    getAccountNumber = Database.keys()
    print("************Account Number : %d***********" % accountNumber) 
    login()


#generate account number
def generateAccountNumber():
    accountNumber = random.randrange(1111111111, 9999999999)
    return accountNumber


#get account balance  
def getBalance(userDetails):
        return userDetails[4]

#Deposit operation
def deposit():
    amount = int(input("How much would you like to deposit \n"))
    for userDetails in Database.values():
        userDetails[4] += amount
        print("Deposit completed successfully")
        print("Your Balance is %d" % getBalance(userDetails))


def withdraw():
    amount = int(input("How much would you like to withdraw \n"))
    for userDetails in Database.values():
        if (amount <= getBalance(userDetails)):
            userDetails[4] -= amount
            print("Withdrawal completed succesfully")
            print("Take your cash")
            print("Your Balance is %d" % getBalance(userDetails))
        else:
            print("insuffiecient fund")
    

#run bank operation
def bankOperation():
    print("======You have logged in successfully======")
    for userDetails in Database.values():
        print("**********welcome %s %s**********" %(userDetails[0], userDetails[1]))
    import datetime
    x = datetime.datetime.now()
    day = x.strftime("%A")
    year = x.year
    print("=========== %s, %d ===========" % (day, year))
    operationRequest = True
    while operationRequest == True:

        print("=====================================")
        print("============Bank Operation============")
        print("=====================================") 
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Account Balance")
        print("4. Complaints")

        selectedOption = int(input("please select an option \n"))
        if (selectedOption == 1):
           withdraw()
        elif(selectedOption == 2):
            deposit()
        elif (selectedOption == 3):
            for userDetails in Database.values():
                print("Your account balance is %d" % getBalance(userDetails))
        elif (selectedOption == 4):
             input("What issue wil you like to report \n")
             print("Thank you for contacting us")
            

        inputOption = int(input("Would you like to do another transaction \n 1. Yes \n 2. NO \n"))
        if (inputOption == 1):
             operationRequest = True
        elif (inputOption == 2):
            login()
            operationRequest == False
        
init()