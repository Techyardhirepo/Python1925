import json,os

#jsonFile= open("StudentsList.json","w")

#jsonFile.close()




studentData= {
  "name" : "Sai Ram",
  "Role" : "Developer",
  "Skills" : ["python","HTML","CSS","Javascript"]
}

with open("StudentsList.json","w") as jsonFile:
     json.dump(studentData,jsonFile, indent=2)


with open("StudentsList.json","r") as jsonFile:
     jsondata= json.load(jsonFile)


print('jsondata=== ', jsondata)


jsondata["Role"] ="Tester"

with open("StudentsList.json","w") as jsonFile:
     json.dump(jsondata,jsonFile, indent=2)


with open("StudentsList.json","r") as jsonFile:
     jsondata= json.load(jsonFile)


print('jsondata=== ', jsondata)


os.remove('StudentsList.json')


def methodname() :
   print('test')




# Identifiers
# Data Types
# Operators
# Type Casting/ Conversion
# Conditional Statements
# Loops
# Exception Handling
# File Handling
# OOPS ( Object Oriented Programming System)
    # 1. Encapsulation
    # 2. Abstraction
    # 3. Polymorphism
    # 4. Inheritance


# Class : User defined Data Type
          # Contains attributes/Properties and Methods 

  # Attributes/Proprties
  # Methods : Re usable Code Block also called as Funtion




