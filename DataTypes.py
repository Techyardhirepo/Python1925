
import keyword as kw


print(kw.kwlist)



'''

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 
 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


'''


# Data Types in Python
# 
# 
# 1.Number Type
#      1. int (Whole Numbers (positive or negative along with zero))
#      2. float
#      3. complex


# 2. Text Type 
#       1. String : str
# 3. None Type
#     1.None

# 4. Bool Type
#    1.True
#    2.False


# 5. Sequnce Type

#      1. List
#           1. Ordered Collection
#           2. Mutable Collection
#           3. Heterogenious Collection

#      2. Tupple
#            1. Ordered Collection
#            2. Immutable Collection
#            3. Heterogenious Collection

#      3. range
#            1. This is used to give sequnce of numbers
#            2. This is also kind of pre defined function
     
#               0            1            2            3  
# 6. Set Type

    # 1. set
     
        # 1. un ordered Colletion
        # 2. Unique Collection
        # 3. Mutable Collection
     
     #2. Frozen Set
        
# 7. Mapping Type
     
     #  1. Dict

studentDeatilsMap= {
    "studentName" :"Anil",
     "studentAge" : 22,
     "studentMarks" : 22,
     "Gender" : "Male",
     "StudentName":"Satheesh",
     "Gender":None
}

studentsFrozen= frozenset(["Vinay", 25,"Anil",34.55,"linga"])
 
studentsSet = {"Vinay", 25,"Anil",34.55,"linga"}

studentsList= ["Vinay", "linga","Anil","sathish","linga"]

print(studentDeatilsMap)

print(studentsSet)
print(studentsList)

studentDetails= ["Student Name", 25, 78.5, None]
'''
print(f'type of studnetsList : {type(studentsList)}')



monthsTupple= ('Jan',5,2)


#"'i am techyardhi's student'"

studentMarks= "75"

averageMarks= '50.58787'

electricPower= 3+4j  


courseName= "Python"


aboutStudent="'i am techyardhi's student'"

Total =None


#10+5j

# to find type of an identifier

print(type(studentMarks))

print(type(averageMarks))

print(type(electricPower))

print(f' type of the Markes {type(Total)}')



isAvialable= "True"
'''