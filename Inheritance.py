# Parent class == Base Calss
# Child Class == Deriveed class


 





class parent:
    def show_parent(self):
        print('This is from Parent Class')


class FirstChild(parent):
    def show_child(self):
        print('This is from Child Class')


class SecondChild(parent):
    def show_Secondchild(self):
        print('This is from Second Child Class')


objChild= FirstChild()
objChild.show_child()
objChild.show_parent()


objSecondChild= SecondChild()
objSecondChild.show_Secondchild()
objSecondChild.show_parent()



# Single Inheritance
# Multiple Inheritance
# Multi LevelI inheritance
# Hierarchial Inheritance



class Father :
    def fatherskills(self):
        print('Driving,Farming,something')


class Mother :
    def motherskills(self):
        print('Cooking,Home Making,Job')


class child(Mother,Father):
    def more_skills(self):
        print('dancing,Singing,Reading,Eating')


obj= child()
obj.fatherskills()
obj.motherskills()
obj.more_skills()



class grandPraent:
    def show_grandParent(self):
        print('Grand Parent')

class parent(grandPraent):
    def show_Parent(self):
        print('Parent')

class Child(parent):
    def show_Child(self):
        print('Child')


objC= Child()
objC.show_grandParent()
objC.show_Parent()



class Manager:
    def manageTeam(self):
        print('Managing Team')

class TeamLead1(Manager):
     def ManageTeam_Lead(self):
        print('Managing Team')


class TeamLead2(Manager):
     def ManageTeam_Lead(self):
        print('Managing Team')


#class TeamMember(TeamLead1):


#class TeamMember(TeamLead2):


# Single --->    [Child <--- Parnet]

# Multiple -->   [Child <---- (Parent1, Parent2 ,Parent3)]

# Multi Level --> [Child <---- Parent1  <--- Parent2 <--- Parent3)]

# Hierachial Inheritance --> [ Child1 <---  Parent]
                             #[Child 2 <--- Parent]
                             #[Child 3 <--- Parent]



class Vehicle :
    def __init__(self, brand,model)  :
       self.brand=  brand
       self.model=model   

    def start(self)  :
        print(f'{self.brand} {self.model} is starting......')               


    def stop(self)  :
        print(f'{self.brand} {self.model} is stopping......')     


    def fuelType(self)  :
        print(f'{self.brand} {self.model} is general Fuel Type......')     



class Tata(Vehicle):
    def fuelType(self, vfuelType):
        print(f'{self.brand} {self.model} fuel type is {vfuelType}')


class tesla(Vehicle):
    def fuelType(self, vfuelType):
        print(f'{self.brand} {self.model} fuel type is {vfuelType}')


class Mahindra(Vehicle):
    def fuelType(self, vfuelType):
        print(f'{self.brand} {self.model} fuel type is {vfuelType}')


tata_car = Tata('Tata','Harrier')
tata_car.start()
tata_car.stop()
tata_car.fuelType('Petrol')


tesla_car = tesla('Tesla','Cyber Truck')
tesla_car.start()
tesla_car.stop()
tesla_car.fuelType('CNG')