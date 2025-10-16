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





    