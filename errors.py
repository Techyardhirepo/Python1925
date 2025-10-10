# Compile Time Errors
   # Syntax Error

# Run Time Errors
   # Exception


#Exceptions Handling


#try : the code which has to be executed
#except : if any exception comes in the code which has written in try block
#else : this block exceute only when try block executes without any exception
#finally : this will execute everytime which is used for dispoing of resources




try:
  number1= int(input("Enter Number 1"))
  number2= int(input("Enter Number 2"))
  # create a file
  number3=number1/number2
  print('code1')

except Exception as ex:
  print(f'Something went wrong {ex}')
else:
  print('Try Block executed successfully')
finally:
 print('Exception handling done')



firstNumber= int(input("enter Number: "))
SecondNumber= int(input("enter Number: "))

try:
 if SecondNumber==0:
   print("enter valid second number")
 else:
  thirdNumber= firstNumber/SecondNumber
  print(thirdNumber)
except:
  print('Second number number shoul not be zero')
else:
  print('test')
finally:
  print('test')