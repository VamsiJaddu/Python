

## Global variable
balance = 0.0
kyc_documents = {}

## Checking Balance
def check_balance():
    print(f"Available Balance: {balance}")
    print()
    
## Deposit Amount    
def deposit():
    global balance
    print(f"Available Balance: {balance}")
    deposit_amount = float(input("Deposit Amount: "))
    if deposit_amount > 0:
        balance += deposit_amount
        print(f"Deposited Amount {deposit_amount} is successful. ")
    else:
        print("Invalid Amount can not deposit.")
    print(f"Available Balance: {balance}")
    print()
    
## Withdraw Amount    
def withdraw():
    global balance
    print(f"Available Balance: {balance}")
    withdraw_amount = float(input("Withdraw Amount: "))
    if  withdraw_amount <= 0 or withdraw_amount > balance:
        print("Invalid Amount") 
    else:   
        balance -= withdraw_amount
        print(f"Amount {withdraw_amount} withdrawn is successful")    
    print(f"Availiable balance: {balance}") 
    print()
    
## KYC update
def kyc_update():
    global kyc_documents
    num = int(input("Enter number of documents you want to add: "))
    for i in range(num):
        key = input("Enter your document name: ")
        value = input("Enter document number: ")
        kyc_documents.update({key:value})
    print(f"You have successfully updated {kyc_documents}")
    print()

## checking KYC    
def check_kyc():
    if len(kyc_documents) == 0:
        print("KYC not yet done!!")      
    else:
        for doc in kyc_documents:
            print(f"{doc}:{kyc_documents[doc]}") 
    print()       
    
if __name__ == "__main__":         
    print("====================================")
    print("Welcome to ABC Bank")
    print("====================================")

    while True:
        print("1.Check balance", end = "  ")
        print("2.Deposit" , end = "  ")
        print("3.Withdraw" , end = "  ")
        print("4.Check KYC" , end = "  ")
        print("5.Update KYC" , end = "  ")
        print("6.Quit")
        print("====================================")
        choice = (input("Enter your choice: "))
        print("====================================")
        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
                check_kyc() 
        elif choice == "5": 
                kyc_update()           
        elif choice == "6":
            print("Have a Nice Day")
            break
        else:
            print("Invalid choice.Re-try!")        
    print("Thank you for visiting!")  
    print()  