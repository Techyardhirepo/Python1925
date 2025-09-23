#Dict : key value pair Collection

# Key s are Unique
# Value s are can be duplicate
# mutable collection


studentDetailsDict= ({"studentName": "Anil",
                      "Qualification": "B.Tech",
                      "Branch" : "ECE",
                      "Grade" : "A+" 
                      })
print('studentDetailsDict==== ',studentDetailsDict)

studentDetailsDict.update({"College Name": "JNTUH", "Address": "Kphb,Hyderabad"})

print('studentDetailsDict==== ',studentDetailsDict)

studentDetailsDict["Branch"]= "CSE - AI/ML"

print('studentDetailsDict==== ',studentDetailsDict)


studentDetailsDict.popitem();



print('studentDetailsDict==== pop Item ===',studentDetailsDict)


del studentDetailsDict["Grade"]

print('studentDetailsDict==== del Item ===',studentDetailsDict)


#update - inserting new key value pair (single / multiple)
#dict[Key] - updating value of input key


#popitem() - deletes last added key value pair in the dictonary
# del dict[key] - delete key value pair of input key