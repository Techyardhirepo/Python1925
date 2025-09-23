# Type Casting or Type Converion


# 1. Impilicit Type Casting : Type Conversion will be done automatically by python
# 2. Explicit Type Casting


number1 = 12.5 # int
number2 = 3+4j # float


number3 = number1+number2

print('type of number3==',number3)

number4= 100.256

number5= int(number4)

print('number5',number5)

number6= float(number5)

print('number6', number6)

print('Convert to Complex', complex(number6) )



someString ="256"

someIntValue= complex(someString)

print('someIntValue====>',someIntValue)


number8=2000.6565

strNumber8 = int(number8)

print('strNumber8', strNumber8)


studentsList = ["Vinay","Vinith","Sathish","Anil","Linga","Sathish"]

studentsSet= set(studentsList)

print('studentsSet===', studentsSet)

studentsList= list(studentsSet)

print('StudentList===', studentsList)

print('StudentList value by Index===', studentsList[1])


studentTupple= tuple(studentsList)

print('studentTupple===', studentTupple)


set, list, tuple, dict

numbersList= [(1,3),(2,4),(3,4),(5,6),(7,8)]

someDictIdentifier= dict(numbersList)

print('someDictIdentifier===', someDictIdentifier)

numbersList= tuple(someDictIdentifier)

print('numbersList Dict to tuple', numbersList)




 









