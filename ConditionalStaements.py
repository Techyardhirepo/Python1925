# If

# If else

# if Elseif Else

# Nested If

# Match Case


#We need Identifiers along with data types
#Relational and Logical Operators

'''
Ternary and Walrus
'''

'''
phoneScreenPassword="12345"
inputpassword= input("Enter Screen Password: ");
if phoneScreenPassword==inputpassword:  # if condition true
    print('open home screen')
else:  # if Condition false
    print("Enter valid passwrod")
'''

'''
atmPin= "9876"
inputatmPin= input("enter your PIN: ")

if atmPin==inputatmPin:
    print('Show Withdrwal or balance check screen');
else:
    print('The pin you entered is wrong')
'''

'''
username="vinith@gmail.com"
password="techyardhi@123"

inputuserName= input("Enter Username: ")
inputPassword= input("Enter Password ")

if username == inputuserName and password ==inputPassword:
    print("Go To Home Screen")
else:
    print("enter valid username and password")
'''






'''
somenumber= int(input("Enetr Value: "))
print("type of somenumber", type(somenumber));
if somenumber >= 5:
    print("somenumber is greater than 5")

'''


# 1. Pin Verification
       # Valid Pin - Home Screen
       # Invalid Pin - Enter Valid Pin

'''
atmPin='6578'
accountBalance=25000
pinFromUserInput= input("Enter your PIN: ")
if atmPin == pinFromUserInput :
    print('Welcome to Home screen');
else :
    print('Enter Valid Pin');

selectChoice= input("Enter your Choice: ")

if selectChoice =="Balance Enquery":
    print("your Account balance is", accountBalance);
elif selectChoice == "Deposit":
    depositAmount= int(input ("enter deposit Amount: "))
    if depositAmount > 0 :
       #accountBalance=accountBalance+depositAmount
       accountBalance+=depositAmount
       print("Your Amount Deposited successfully. Your Account balance is",accountBalance)
    else :
        print('Enter valid positive deposit amount')
elif selectChoice == "Withdrawl":    
    withdrawAmount= int(input ("enter withdrawl Amount: "))
    if accountBalance < withdrawAmount:
        print('in sufficient account balance');
    else :
         #accountBalance=accountBalance-withdrawAmount
         accountBalance-=withdrawAmount
         print("Please collect your cash. Your Account balance is",accountBalance)
else:
    print('Enter valid choice')

'''
'''
weekdayNumber = int(input("Enter Day Number: "));

match weekdayNumber:
    case 1:
        print("Monday")
    case 2 :
        print("Tuesday")   
    case 3:
        print("Wednesday")
    case  4:
        print("Thursday")   
    case 5:
        print("Friday")
    case 6 :
        print("Staturday")   
    case 0:
        print("Sunday")
    case _:
        print("Enter Valid Week day")
'''

'''
atmPIN=1234
accountBalance=30000
      
userEnteredPIN= input("Enter ATM PIN: ")

if str(atmPIN) == userEnteredPIN:
            userChoice= input("Enter your Choice: ")
            match userChoice :
                case 'Balance Enquiry':
                      print("your Account balance is", accountBalance);
                case 'Deposit':
                      print("your Amount Deposited");
                case 'Withdrawl':
                      print("your amount withdrawn");
                case _:
                      print("Enter Valid Choice");


else :
            print("Enter valid ATM PIN")

# Ternary Operator : Its a single line if else condition;


studentAge=18;

if studentAge>18 :
       print('student is Major')
else :
       print('Student is Minor')




'''

# value_if_true  If Condition  Value_if_false
studentAge= int(input("Enter Student Age: ")) # 25
studentStatus= 'Major' if studentAge >  18 else 'Minor'
                              
Marks= int(input("Enter Studnet Marks: "))
StudentResult = 'Fail' if Marks < 35 else 'Pass'

print('StudentResult', StudentResult)


           

     


    







