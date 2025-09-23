# Operators

   # 1. Arthimetic Operators
       
           # 1. Addition (+)
           # 2. Subtraction (-)
           # 3. Multiplication (*) // Replication Operator
           # 4. Division (//)(Floor Division)
           # 5. Division(/) (float Division)
           # 6. Modulus (%)
           # 7. Exponent (power) (**)

   # 2. Comparison/Relational operators (True/False)
           
           # 1. Equal to (==)
           # 2. Not Equal To (!=)
           # 3. Greater Than (>)
           # 4. Less Than (<)
           # 5. Greater Than Or Equal (>=)
           # 6. Less Than Or Equal (<=)
   
   # 3. Assignment Oprators
           
           # 1. =
           # 2. +=
           # 3. -=
           # 4. *=
           # 5. /=
           # 6. //=
           # 7. %=
           # 8. **=

  # 4. Logical Operators
           
        # 1. and  : every condition should be true : Output true
        # 2. or   : any of the conditions is true : output true
        # 3. not  : inverts the output ( true--> false, false--> true)
 
  
  # 5. Bitwise Operators
        
        # 1. &  (AND)
        # 2. |  (OR)
        # 3. ^ (XOR) X- Or (Exclusive OR)
        # 4. (<<) left shift 
        # 5. (>>) right shift
        # 6. ~


 # 6. Membership operators
 #     
 #       1. in
 #       2. not
 # 

  # 7. Identity Operators     
       # 1. is


someIdentifier=[1,2,3,4,5,6];
anotherIdentifier=someIdentifier

print("Identity operator  'is'", someIdentifier is anotherIdentifier)


studentsList= ['Anil','sathish','Linga','Vinay','Vinith','Neha','Indu','Swapna']   


studentName= 'surya'

instituteDescription='Techyardhi is an institute estabkished at KPHB in Hyderabad'

strPlace='HYDERABAD'

strPlace not in instituteDescription



a=64  # 1001"
        
b= 5 # 0101
#===============
        #   1100
    
   
           

#print('binary Format',format(a,'b'))
                                       #9   #5
print('Bitewise ~ operator :',~b)   # -(5+1)

# 101
# 011
#-------
#     001



           



atmCradNumber= '1234 3456 3456 9876'
atmPin='4567'

cardNumberFromUser= input("enter Card Number:  ")
userAtmPin =input("enetr ATM PIN:  ")

      #true                                  false             


atmCheckCondition = (atmCradNumber== cardNumberFromUser) and (atmPin==userAtmPin)
print('and output ',atmCheckCondition)
print('not output ',not(atmCheckCondition))






value1=50
value1 **= 20 # value1 = value1/20

print('value1', value1)

 
number1 = 39

number2= 50

print(number1  <= number2)  # 39 <= 50

'''
firstName="Surya"
lastName="Trainer"
middleNmae="Techyardhi"


numberlist=[1,2,3,4,5]
'''

'''for i in range(1,10):
    print('*' * i)'''

'''
tarinerName= firstName +' '+middleNmae+ ' '+lastName

print(numberlist*10);

number1 = 3
number2 = 10

number3= number1*number2
'''
#print(f'number3 {number3}')

'''
        14/5

   5)14(2
     10
     ----
       4
'''
