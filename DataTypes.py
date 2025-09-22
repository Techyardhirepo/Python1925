#Numeric Type Data Types

# int 

studentAge=17;

##type(studentAge);

print("Data Type in Student Age:" , type(studentAge));


# Float

studentAttendancePercentage=75.84;

print("Data Type in studentAttendancePercentage:" , type(studentAttendancePercentage));

#Complex    

power= 20+5j;

print("Data Type in power:" , type(power));


#Text Based Data Type

#str

studentName= "you are the techyardhis student";

Grade='A';

print("Data Type in studentName:" , type(studentName));

# type() is a method to identify the data type of data/value stored in an identifier
#text enclosed in single or double QUotes


#Sequence Type Data Types

#List
            #            0     1      2       3     4
programmingLanguages=["Java","C#","Python","PHP","Ruby","Java"];
print(programmingLanguages);

#Mutable : can be added, modified or removed elements from the list

programmingLanguages.append("R Language");
programmingLanguages[3];
programmingLanguages.extend(["JavaScript","Type Script"]);

print("Data Type in programmingLanguages:" , type(programmingLanguages));
programmingLanguages.insert(2,"Some Value");

#programmingLanguages.remove(4);


print("Get First Language:" , programmingLanguages[2]);


 

#programmingLanguages[0];

#Mutable --> Something can be modified or updated after creation
#Unmutable --> Something Cant be modified or updated after Creation

#Tuple
   #           0        1           2       3
languages= ("Telugu","English","Kannada","Tamil","Telugu")
#languages.__add__("Malayalam");
print(languages);





fruits= {"Mango","Apple","Grape", "Apple"}
print(fruits);


#List
studentDetailsList= ["Surya","35","Hyderabad","9876543210","surya@techyardhi.com"]
studentDetailsList.append("Python");
#Tuple
studentDetailsTuple= ("Surya","35","Hyderabad","9876543210","surya@techyardhi.com")
#set
studentDetailsset= {"Surya","35","Hyderabad","9876543210","surya@techyardhi.com"}
studentDetailsset.add("Python")

studentDetailsDict= {"name" : "Surya" , "place": "Hyderabad", "age":35, "Contact": "9876543210"}
studentDetailsDict["place"]="karimnagar";
studentDetailsDict["age"]=33;


#frozenStudentDetailsSet= ({"Surya",35,"Hyderabd"})
#frozenStudentDetailsSet.append("python");

#print('frozenStudentDetailsSet',frozenStudentDetailsSet);

activecase=True

inactivecase=False

student= None;


 