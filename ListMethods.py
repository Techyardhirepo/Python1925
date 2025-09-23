

ExistingStudentsList= ["Vinith","Vinay","Linga","Anil","Sathish"]
newStudentsList= ['Hari','Swapna','Neha','Sai','Shakeer','Akash','Sathish']
#append
 

#extend
ExistingStudentsList.extend(newStudentsList)


print('StudentsList====>', ExistingStudentsList)

ExistingStudentsList.insert(4,'Pravallika')

print('StudentsList====>', ExistingStudentsList)

ExistingStudentsList[2]="Linga Swami"

print('StudentsList====>', ExistingStudentsList)


removedItem=ExistingStudentsList.pop(3)

print('popped Item===>', removedItem)

print('ExistingStudentsList===', ExistingStudentsList)

ExistingStudentsList.insert(1,removedItem)

print('ExistingStudentsList===', ExistingStudentsList)




# append
# extend
# insert
# list[i] =value;


#pop()
#pop(i)
#remove() It will delete first occurance of an element
# del list[i]
# del list[startIndex: EndIndex] Slicing
# clear
print('ExistingStudentsList before Remove===', ExistingStudentsList)

ExistingStudentsList.remove('Sathish')

print('ExistingStudentsList after Remove===', ExistingStudentsList)

ExistingStudentsList.remove('Sathish')

print('ExistingStudentsList after Remove again===', ExistingStudentsList)

del ExistingStudentsList[5]

print('ExistingStudentsList after del list[5]===', ExistingStudentsList)

del ExistingStudentsList[2:5] # Slicing 

print('ExistingStudentsList after del list[2:5]===', ExistingStudentsList)

ExistingStudentsList.clear()

print('ExistingStudentsList after Clear===', ExistingStudentsList)






