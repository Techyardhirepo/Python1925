#Operators


# 1. Arthmetic : used to perform Mathematcical Operations
# 2. Comparision
# 3. Logical 
# 4. Bitwise
# 5. Assignemnet 
# 6. Identity
# 7. Membership
# 8. Ternary, Walrus


# +
# -
# *
# /
# // (only in Python)
# %
# ** (only in Python)


a=10
b=3

# addition
c= a+b # 10+3 = 13
c= a-b # 10-3=7
c= a*b # 10*3= 30
c= a/b # 10/3= 3.3333 (Actual division with decimals)
c= a//b # 10//3= 3 (We have only in Pthon)
c= a%b # 10%3  1
c= a**b # 10 power 3 = 1000 (We have only in Pthon)


# Compaision/Relational Operators

 # output from this Comparsion operators always would be True or False
 # ==
 # !=
 # >
 # <
 # >=
 # <=
 
x=10;
y=10;

x<=y  #True


# Logical operators

# And
# Or
# Not


p=True
q=False

p and q  # True and False False
p or q # True or False True

not p # not True : False



number1=20;
number2= 10;

(number1>number2)
   #20  >  10   True

number1<number2
  #20 < 10  False

(number1>number2) and (number1<number2)
     #True                 #False         False

(number1>number2) or (number1<number2)
     #True                 #False         True

not (number1<number2)
      #20 > 10  Not(False) True
 

# Assignment Operators

# =



studentName = "Surya" #(Assignment)
#  <---------

# +=   (Addition with Assignemnet)
'''
someNumber= 10;
someNumber= someNumber+2; #12
someNumber += 2; # 14
'''

# -= ( Subtarction Assignment)
#print("someNumber 1",someNumber);

#someNumber -= 10; # 14-10= 4

#print("someNumber 2",someNumber);

# *=

someNumber= 17;
#someNumber *= 2; #someNumber= someNumber*5;

#someNumber //=4;  #someNumber= someNumber/4;

print("Some Number",someNumber);


# %=

#someNumber %= 4; #someNumber= someNumber % 4;

print("someNumber with %=", someNumber);


# **= ;


someNumber **= 3;

print("somenumber **= ", someNumber);

#Identity Operators



a= [1,2,3]
b=a;
c= [1,2,3]

print("a", a)
print("b", b)
print("c", c)

#True or False

print (" a,b is not identifier:",a is not b)

print ("a,c is not identifier:",a is not c)

# is not

#Membership operators

nums= [1,2,3,4,5,6,7,8,9,10];
someValue =4

#5

# in
# not in

print("in Opertor",someValue not in nums)   # 2 in [1,2,3,4,5,6,7,8,9,10]  # True

 

 #Bitwise Operators

 # 000 0000 00000
 #    7    15   31


  # &  (AND)
  # |  (OR)
  # ^  (XOR)

someNumber4= 25;  # 100
someNumber5=4;   # 100

someNumber6= 5 # 101
someNumber7 =4 # 100

someNumber6 & someNumber7 #  101 & 100 ==> 010 ==> 2 
someNumber4 | someNumber5 

print("XOR Output", (someNumber4 ^ someNumber5)) # 110 ^ 011
print("AND Output", (someNumber4 & someNumber5)) # 110 & 011
print("OR Output", (someNumber4 | someNumber5)) # 110 | 011
print("Not Output", (~someNumber4)) # ~101  #5 101 -110

#25   -26
  
'''
  & (AND) ===> If any one of the two digits is 0 output would be 0
  | (OR)  ===> If Any of the two digits is 1 output would be 1
  ^ (XOR) ==> if any of the two digits is 1 output would be 1, if two digits are 1 or 0 then output would be 0;
      
  ~ (NOT)  ===>

  
   100
   100
   -----
     100

     100
'''

      

#XOR ==> Exclusive OR
# 
#  

'''
110                    100
                       100
                       -----
                          101
                         
011
=====
 1 1 1 

-----
   111
   '''

 


'''
 000 --> 0

 001 --> 1

 011  --> 2+1                          000   --     111  (7)
                                       0000  --     1111 (15) 2 power 4 = 16-1 
                                       00000 --              11111 (31)  (2 power 5)-1 = 32-1=31
                                            
 010  --> 2
 011  --> 2+1 =3
 101  --> 4+ 1=5
 111  4+2+1 =7--> 

 '''
                         #       64   32  16   8   4   2  1

                         #       2 power 6     2 power 5    2 power 4   2 power 3     2 power 2     2 power 1   2 power 0


   





#Bitwise
# &

 


# |

   


# ^
    
     

# ~
 
someNumberN=200;

print ("Not SpmeNumber:",~someNumberN) # -(someNumberN+1)

# <<
# >>
print("Left shift Output:",10 << 1) 

 

# left shift : a << n = a * 2 power n

#104 * 2 power 1 => 10 * 2 =20

# Right Shift : a >> n = a/(2 power n)

print("Right Shift:",11>>3)  #  9//2










 





                                                 
   