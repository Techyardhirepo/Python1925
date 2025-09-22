# Loops in Python


# For Loop
# While

#range() # which generates sequence of Numbers

#range(1,100, 1)
'''
startNumber= int(input("Enter Start Number: "))
endNumber= int(input("Enter End Number: "))
difference=int(input("Enter Step Difference: "))

if startNumber<endNumber:
       for i in range(startNumber,endNumber,difference):
        print(i)
else :
    print('Start number should not be less than end Number')

     
    while startNumber <= endNumber:
        print(startNumber)
        startNumber += difference; # i= i+1



 
  
# for loop
# while

studnetsMarks= [45,25,96,85,72,88,44,15,90,62]

for marks in studnetsMarks:
    if marks>40 :
        print("pass")
    else :
        print('fail')     

'''
'''
atmPin='1234'
enteredAtmPin=  input("Enter your PIN :")
count=1
while atmPin!=enteredAtmPin and count < 3 :
    enteredAtmPin= input("Enter your PIN :")
    count +=1


if count==3 and atmPin != enteredAtmPin :
    print("your card is blocked")
else :
    print("Home Screen")
'''
'''
count=0
while True :
    count+=1
    if count < 10000 :
        pass
        print('Count:',count)
    

#Control Statements in loops


#continue -> skips executes next statements in th loop
#break --> stops execution of loop and exiting the loop
#pass --> do nothiing

'''
#walrus

# for loop is used mostly on sequnces like string, list,set,tuple,dict or frozen
# while loop is used when we need to execute some code until some condtion is false

#while loop with else
#for loop with else

numbers= [10,25,30,5,12]
'''
for number in numbers:
    if(n := number) >20 :
        print(n);
while (n := numbers) > 20:
    print(n)
     '''
enteredString= input("enter string:  ")

if (length := len(enteredString)) > 5 :
    print("string length is",length)





