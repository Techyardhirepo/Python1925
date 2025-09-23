

studentsSet= {"Vinay","Vinith","Neha","Swapna","Sathish","Anil","Sai","Akash","Shakeer","Linga"}

newStudentsSet={"Pravallika","Hari","New Student 1"}

#unordered mutable unique collection

#add()

#update()

studentsSet.add("Pravallika")

studentsSet.update(newStudentsSet)

print('studentsSet=== ', studentsSet)


#remove(value) deletes the value if its found in the list other wise it will give error 
#discard(value) 
#pop()

studentsSet.discard('Surya')

print('studentsSet=== After Remove== ', studentsSet)

#studentsSet.discard('Hari')

print('studentsSet=== before pop== ', studentsSet)


studentsSet.pop()

print('studentsSet=== after pop== ', studentsSet)

studentsSet.pop() # deletes arbiratry element

print('studentsSet=== after pop pop== ', studentsSet)



# add : adding single element to set
# update : adding one set to another set


# remove(value)
# discard(value)
# pop() 
# clear()







