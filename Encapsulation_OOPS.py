class Bank :
      __bankName="SBI"
      __address= "Raod No 1,KPHB,Hyderabad"

    
      def __init__(self,bankAccountNumber,personName,BankBalance):
        self.__accountNumber=bankAccountNumber
        self.__personName=personName
        self.__Balance=BankBalance

      def __showAccountDetails(self):
          print(f' Account Number {self.__accountNumber} and Name : {self.__personName} and Bank balance {self.__Balance}')

      @classmethod
      def showBankDetails(cls) :
          print('Bank Name: '+ cls.__bankName)


      def depositAmount(self, depositAmount) :
          if(depositAmount<0) :
            print('invalid amount entered')
          else:
            self.__Balance += depositAmount

      def withdrawAmount(self, withdrawAmount) :
          self.__Balance -= withdrawAmount


objBank= Bank('1234567','Anil',20000)     
#objBank.__showAccountDetails()
objBank.depositAmount(-10000)

#objBank.__showAccountDetails()

objBank.withdrawAmount(5000)
#print('Bank Name:'+ Bank.bankName)

objBank.__showAccountDetails()

#Bank.showBankDetails()

#print('Bank Name:'+ Bank.bankName)