# print numbers upto given input number

inputNumber= int(input("enter number : "))

for i in range(1,inputNumber+1) :
    print(i)


# print only even numbers
#2,4,6,8,10,12
for i in range(2,inputNumber+1, 2) :
    print(i)


# print only odd Numbers

#1,3,5,7,9,11,13

for i in range(1,inputNumber+1, 2) :
    print(i)


startNumber=1
while startNumber<=inputNumber:
    print("Without using Range",startNumber)
    startNumber+=2

#2,3,5,7,11,13,17,19,23,29

#the number which be divisble by 1 or that number only

if inputNumber <= 1 :
    print("not prime number")
else:
    for i in range(2,inputNumber) :
        if inputNumber%i==0:
            print("not prime number")
            break
    else:
        print("prime number")

# print Fibonacci Serries

#0 1 1,2,3,5,8,13,21,34

a=0
b=1

for _ in range(100) :
 print(a, end=" ") #0 1 1 2 3 5
 a,b= b,a+b  # a=1, b=1+1 




 number1=100
 number2=200

 number1,number2= number2,number1

    


