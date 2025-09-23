# Loop : repeat execution of a code block


# 1. for loop : when we know how many times we want to repeat the code execution
# 2. while : when we dont know number of times to repeat the code execution  and we only condition and
#     this will be executed untill that condition statisfies

# when ever we have collections and if we need to reapeat code execution. we can simply blindly go for for loop

customersList=["Ravi","Surya","Sarvesh","Shakeer","Ravi","Surya","Sarvesh","Shakeer","Ravi",
               "Surya","Sarvesh","Shakeer","Ravi","Surya","Sarvesh","Shakeer","Ravi","Surya",
               "Sarvesh","Shakeer","Ravi","Surya","Sarvesh","Shakeer","Ravi","Surya","Sarvesh",
               "Shakeer","Ravi","Surya","Sarvesh","Shakeer"]


taskList ={"Attend Class", "Take Break", "Practice","Lunch","Practice","Have Tea or Snacks",
           "Practice","Dinner","Sleep"}

for customer in customersList :
    print(customer)

for task in taskList :
    print(task)
    if task== "Attend Class" :
        print("open Laptop")
        print("Login to Teams")
        print("Join Session")
    if task== "Take Break" :
        print("Shut Down laptop for 30 mins")
    if task== "Practice" :
        print("Open Laptop")
        print("open VS code")
        print("write some code for practice")

#for identifier in collectionIdentifierName :







'''
customersList[0]
customersList[1]
customersList[2]
customersList[3]
customersList[4]
customersList[5]
customersList[6]
customersList[7]
'''

 

studentsdict= {"Ravi" : 85,
        "Surya" : 30,
        "Anil" : 75,
         "Vinith" : 80,
          "Sathish" : 83,
           "Neha" : 79,
           "Sai Ram": 81,
           "Swapnaam": 83}

for name,marks in studentsdict.items() :
    print(name ,marks)
    if marks <= 35 :
        print(f'{name} failed in exam with {marks} marks')
    else :
        print(f'{name} passed in exam with {marks} marks')


'''someChar ="8"
for i in range(1,15) :
    print( someChar*i )
    '''

'''
#number = int(input("Enter Table Number : "))
startNumber= int(input("Enter start Number : "))
endNumber = int(input("Enter End Number : "))
for number in range(startNumber,endNumber) :
  for i in range(1,11) :
    print(f'{number} X {i}== {number*i}')
'''
studentName= "Sai Ram Shankar"
count = 0;
for c in studentName :
    count +=1

print(count)
# can be used on sequence type
# str,list, tupple
# set,frozenset,Dict





     

      



