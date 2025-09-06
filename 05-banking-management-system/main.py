from pathlib import Path
import random
import json
import string


class Bank :
    database = 'data.json'
    data = []

    # load the data When you create instance.
    try :
        if Path(database).exists() :
            with open(database , 'r') as fs :
                read_data = fs.read()
                data = json.loads(read_data)
        else :
            print("No such file exist !")

    except FileNotFoundError as err :
        print(f"Error : {err}")
    

    
    # class methods for generate acc no and update data into json.
    @classmethod
    def __generateAccountNumber(cls) :
        random_digit = string.digits
        acc_no = random.choices(random_digit , k=6)
        return "".join(acc_no)
    
    @classmethod
    def __updateDataIntoJsonFile(cls) :
        with open(cls.database , 'w') as fs :
            fs.write(json.dumps(cls.data))

    

    # 1 . create Account func.
    def createAccount(self) :
        user_data = {
            "name" : input("Enter your name : "),
            "age"  : int(input("Enter your age : ")),
            "accNo" : Bank.__generateAccountNumber(),
            "amount" : int(input("Enter amount : ")),
            "pin"  :  input("Enter 4 digit pin : ")
        }
        if user_data["age"] < 18 :
            print("minimum age required 18+ !")
            return
        
        elif len(user_data['pin']) != 4 :
            print("4 digit pin required !")
            return
        
        elif user_data['amount'] <= 0 :
            print("you could not add negative val")
            return

        Bank.data.append(user_data)
        Bank.__updateDataIntoJsonFile()
        print("Account Created Succesfully !")



    # 2 . Deposite Money func.
    def depoditeMoney(self) :
        acc_no = input("Please enter your account number : ")
        pin = input("Enter pin aswell : ")

        # find into data that already loads.
        user = [ i for i in Bank.data if i['accNo'] == acc_no and i['pin'] == pin]

        # check user exist using truthy or falsy val
        # if not able to find list empty it is falsy val.
        if not user :
            print("Invalid details user not found!")
            return
    
        amount =  int(input("How much money do you want to deposite : "))
        if amount <= 0 :
            print("Not allowed to add 0 or below the zero")
            return
        else :
            user[0]['amount'] += amount
            Bank.__updateDataIntoJsonFile()

            print("Money deposite succesfully !")
            print(f"your curr balance is {user[0]['amount']}")

    

    # 3. Withdraw Money func.
    def withdrawMoney(self) :
        acc_no = input("Enter account number : ")
        pin = input("Enter pin aswell : ")

        # # find into data that already loads.
        user = [i for i in Bank.data if i['accNo'] == acc_no and i['pin'] == pin]

        if not user :
            print("Invalid details user not found ! ")
            return
        
        amount = int(input("How much money you want to withdraw : "))
        if amount <= 0 :
            print("Not allowed to add 0 or below the zero")
            return
        elif amount > user[0]['amount'] :
            print("You dont have that much money to withdraw !")
            return
        else :
            user[0]['amount'] -= amount
            Bank.__updateDataIntoJsonFile()

            print("Money withdrawn successfully !")
            print(f"your curr balance is {user[0]['amount']}")



    # 4 . Update Bank details func.
    def updateBankDetails(self) : 
        acc_no = input("Enter account number : ")
        pin = input("Enter pin aswell : ")

        #  find into data that already loads.
        user = [i for i in Bank.data if i['accNo'] == acc_no and i['pin'] == pin]

        if not user :
            print("Invalid details user not found !")
        
        print("You only have permission to update (name , pin) :)")
        name = input("Enter new name if you want to update either skip press enter : ")
        pin = input("Enter new pin if you want to update (4 digit) , either skip press enter : ")

        if len(name) >=  3 :
            user[0]['name'] = name
        if len(pin) == 4 :
            user[0]['pin'] = pin
        
        Bank.__updateDataIntoJsonFile()
        ## print user details.
        for i in user[0] :
            print(f"{i} : {user[0][i]}")
        print("Your bank details updated succesfully !")
        
    

    # 5 . Delete Account func.
    def deleteBankAccount(self) :
        acc_no = input("Enter account number : ")
        pin = input("Enter pin aswell : ")

        #  find into data that already loads.
        user = [i for i in Bank.data if i['accNo'] == acc_no and i['pin'] == pin]

        if not user :
            print("Invalid details user not found!")
            return
        
        choice =  input("Are you really want to delete an account (y , n) : ").lower()

        if choice == 'n' :
            print("ByPassed !")
            return
        elif choice == 'y' :
            idx = Bank.data.index(user[0])
            Bank.data.pop(idx)
            Bank.__updateDataIntoJsonFile()
            print("Account Deleted Succesfull !")
        else :
            print("you must be write (y , n) oops !")



    # 6. Show ballance func
    def showBalance(self) :
        acc_no = input("Enter account number : ")
        pin = input("Enter pin aswell : ")

        #  find into data that already loads.
        user = [i for i in Bank.data if i['accNo'] == acc_no and i['pin'] == pin]

        if not user :
            print("Invalid details user not found!")
            return
        
        print(f"Hello {user[0]['name']} , your account balance is : {user[0]['amount']}")


    # 7. Send money function.
    def sendMoney(self) :
        acc_no = input("Enter account number : ")
        pin = input("Enter pin aswell : ")
        
        user = [i for i in Bank.data if i['accNo'] == acc_no and i['pin'] == pin]

        if not user :
            print("Invalid details user not found !")
            return
        
        # overide acc no.
        name = input("Enter reciver name : ").lower()
        acc_no = input("Enter Reciver account number : ").lower()

        reciver = [i for i in Bank.data if i['name'] == name and i['accNo'] == acc_no]

        if not reciver :
            print("Invalid details reciver not found !")
            return
        
        send_amount = int(input("Enter amount how much money you want to send : "))

        if send_amount <= 0 :
            print("Sorry Not able to send 0 or below zero !")
            return
        elif send_amount > user[0]['amount'] :
            print("You dont have enough money to send !")
            print(f"You trying to send : {send_amount} and you account balance : {user[0]['amount']}")
            return
        else :
            # send money
            # deduct from user account.
            user[0]['amount'] -= send_amount
            reciver[0]['amount'] += send_amount

            # push data into json.
            Bank.__updateDataIntoJsonFile()

            # Transaction done succesfull
            print("Transaction done succesfull !")
            print(f"You curr account balance is : {user[0]['amount']}")


    
        

        
        



# Program start from here !

print("\n--- Welcome to Python Banking Management System! ---")
print("Press 1 to create an account")
print("Press 2 for depositing the money")
print("Press 3 for withdrawing the money")
print("Press 4 for updating bank account details")
print("Press 5 for delete an account")
print("Press 6 for check account balance")
print("Press 7 for Send Money")
print("Press 8 For exit")

choice = int(input("Press a number what you want : "))

# Creating a bank object.
user = Bank()

# validate choices
if choice == 1 :
    user.createAccount()

elif choice == 2 :
    user.depoditeMoney()

elif choice == 3 :
    user.withdrawMoney()

elif choice == 4 :
    user.updateBankDetails()

elif choice == 5 :
    user.deleteBankAccount()

elif choice == 6 :
    user.showBalance()

elif choice == 7 :
    user.sendMoney()

elif choice == 8 :
    print("Thanks for using our Bank system !")
    quit()

else :
    print("Take a right choice next time !")


    