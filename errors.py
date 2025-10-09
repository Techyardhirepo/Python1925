# Compile Time Errors
   # Syntax Error

# Run Time Errors
   # Exception


'''
try:
    code1
    code2
    code3
    code4

except:
    code1
    code2
else:
    code1
    code2
finally:
    code1
    code2


'''


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