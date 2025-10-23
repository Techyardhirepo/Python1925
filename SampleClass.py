class Student:
    InstituteName="Techyardhi"

    def StudentDetails(self, name,contact="12345") :
        print(f'Student Name: {name} Contact {contact} and Institute Name {self.InstituteName}')

# self will give the context of current class
# instance of a class is called object

class Animal:
    

    def AnimalDetails(self,name,sound,breed) :
        print(name + ' ' +sound + ' '+ breed)


class Bike:
    name="Pulsar"
    Company="Bajaj" 

    def AnimalDetails(self) :
        print(self.name + ' ' +self.Company)







std= Student()
std.StudentDetails("Anil")
std.StudentDetails("Satheesh","4763465")
std.StudentDetails("Vineeth","7634635")
std.StudentDetails("Sai ram","67564")
 
        
anm= Animal()
anm.AnimalDetails('Dog',"Bow Bow","German Shephered")    
anm.AnimalDetails('Cat',"Meow Meow","Some Breed")  
anm.AnimalDetails('Tiger',"Roar","Some Breed")  


anm1= Animal()

anm1.AnimalDetails('Lion','Roaring',"no Breed")

#parameters : names which are given while defining or writing a method
#Arguments : values which are passing to a method


#Class Method

# Instance Method

# Static Method