
# Conditional Statements

# if statement
# if else statement
# if elif (else if) statement (ladder of multiple conditions)
# Nested If ( if Inside if)


'''
age= input("Enetr Person Age: ")
gender=input("Enter Gender")

if int(age) > 21 and gender=='male'  :
    print('you are eleigible to marry')
else :
    print('you need to wait till you get 21 years')



if gender=="male" or gender=="female" :
    if gender=="male":
      if int(age)>21 :
        print("you are eligible to marry")
      else :
         print("male should be wait till 21 years")
    if gender=="female":
      if int(age)>18 :
        print("you are eligible to marry")
      else :
         print("female should be wait till 18 years")





#Match Case (availbale python version >=13)

'''


studentmarks= int(input("Enter Student Marks : "));


if studentmarks >=  90 :
   print("A grade")
elif studentmarks >= 80 :
   print("B grade")
elif studentmarks >= 70 :
   print("C grade")
elif studentmarks >= 60 :
   print("D grade")
elif studentmarks >= 50 :
   print("E grade")
elif studentmarks >= 40 :
   print("F grade")
else :
   print("fail")



if studentmarks >=90 :
   print("A grade")

if studentmarks >=80 :
   print("B grade")

if studentmarks >=70 :
   print("C grade")

if studentmarks >=60 :
   print("D grade")
   
if studentmarks >=50 :
   print("E grade")

if studentmarks >=40 :
   print("F grade")


trafficSignalColor = input("Enter Color :")

if trafficSignalColor == "red":
   print("STOP")
elif trafficSignalColor == "yellow":
   print("Ready to Move")
elif trafficSignalColor == "green":
   print("MOVE")
else :
   print("there is a problem in Traffic signal")



userName= "nightkingnani@gmail.com"
paswword = "qwerty@123"


friendList= ['f2','f1','f3','f4','f5','f6','f7','f8']

userEnteredUSerName= input("Enter UserName:  ")
userEnteredpassword= input("Enter password:  ")
ourName= input("enter your name:  ")
if userName==userEnteredUSerName and paswword == userEnteredpassword:
   print('Home Screen')
   if ourName in friendList:
      print('Show Account info')
   else:
      print('this account is locked')  
else :
   print("enter valid username and password")


