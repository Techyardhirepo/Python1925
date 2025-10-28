#polymorphism : availability of an object in different froms with same name (Many forms)

# operator polymorphism
# method or function polymorphism (Overloading)
# method overriding polymorphism (overriding)


#  +

number1= 100
number2=200

#print(number1+number2)  #300


str1= "Techyardhi"
str2= "Institute"

#print(str1+str2) 


lst1= [1,2,3]
lst2=[3,4,5]

#print(lst1+lst2) 
  



#  *

number1= 100
number2=200

#print(number1*number2)  #300


str1= "Techyardhi "
str2= 10

#print(str1*str2) 


lst1= [1,2,3]
lst2=2

#print(lst1*lst2) 



def addition(a,b) :
    return a+b;


sum= addition('Techyardhi', 'Insititute')

#sum= addition(100)

print('Sum '+ str(sum))


#overloading : same method, different parameters and different behaviour is called method overloading





class SavingBankAccount:

    '''def depositAmount(self, amount):
        self.depositAmount=amount
        print('Amount Deposited in Savings Account')

    def depositAmount(self, amount,AccountNumber):
        self.depositAmount=amount
        print('Amount Deposited in Savings Account with Account number')'''

    def depositAmount(self, amount,AccountNumber='',IfscCode=''):
        self.depositAmount=amount
        if AccountNumber != '':
            print('')
        if IfscCode != '':
            print('')
        print('Amount Deposited in Savings Account  with Account number and IFSC')

class CurrentBankAccount :

    def depositAmount(self, amount):
        self.depositAmount=amount
        print('Amount Deposited in Current Account')

class LoanAccount :

    def depositAmount(self, amount):
        self.depositAmount=amount
        print('Amount Deposited in Loan Account')


savings= SavingBankAccount()
current= CurrentBankAccount()
loan= LoanAccount()

savings.depositAmount(100,'123456678')
#current.depositAmount(1000)
#loan.depositAmount(200)



#for account in [SavingBankAccount(),CurrentBankAccount(),LoanAccount()]:
#    account.depositAmount(200)


def depositintoAccount(accountType) :
    accountType.depositAmount(200)

depositintoAccount(SavingBankAccount())

# same name, differenet parameters - Overloading
# same name, same parameters - overriding



# overloading

# Overriding



# Duck typing polymorphism




class Bird:
    def makeSound(self):
        print('Bird sounds')

class Dog:
    def makeSound(self):
        print('Dog Barks')

class cat:
    def makeSound(self):
        print('Meow Meow')

def showAnimalSound(animalType):
    animalType.makeSound()

showAnimalSound(Bird())

showAnimalSound(Dog())

showAnimalSound(cat())



