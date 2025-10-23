# Class : is a user defined data type
# Object : instance of a class


class Vehcile:
    vehicleCompany="Bajaj" # class level varaible

    # Constructor : is a default method which is called automatically when we create an instance for a class

    def __init__(self,model,year,color,engineCC):  # Default Constructor
        print('Class Constructor Called')
        self.VehiCleModel=model  #instance variable
        self.VehicleYear=year
        self.VehicleColor=color
        self.VehicleEngineCc=engineCC

    def showVehicleDetails(self): #Intsance Method
        print(f'{self.VehiCleModel} {self.VehicleYear} {self.VehicleColor} {Vehcile.vehicleCompany}')

    # Class Method
    @classmethod
    def showVehcileDetails(cls):
       print("Vehcile Company:" + cls.vehicleCompany)
       #print(cls.VehiCleModel)


    @staticmethod
    def showVehicleDetailsStatic(company,model,year,cc,vtype):
        print(f'{company} {model} {year} {cc} {vtype}')

Vehcile.showVehicleDetailsStatic('Hero','Spendor','2024','100','Two wheeler')

objVehicle= Vehcile("Pulsar","2025","Red","150")
objVehicle.showVehicleDetails()

print(objVehicle.vehicleCompany)


objVehicle1= Vehcile("Platina","2020","Blue","100")
objVehicle1.showVehicleDetails()

print(objVehicle1.vehicleCompany)


#objVehicle1= Vehcile()

#objVehicle2= Vehcile()




# Instance Level Identifier
    # An identifier which can be accessed when we create an instance for a class
    # Calling : instanceName.identifierName
# Class Level Identifier
    # An idenfier Which can be accessed class level without depending on intsance of class
    #  # Calling : ClassName.identifierName


#Methods

# Constructor : Default method which will be ncalled automatically when we create an instance for a class
                # all instance variable will be defined in side constructor

                #  def __init__(self)

# Instance Method : 
             # is a method which can be called when we create instance for class
             # behaviour of the method will vary depends on instance
             # instanceName.MethodName
             # we can access class level identifiers and instance level identifiers

# Class Method:
            # is a method which can be called with out creating instance for class
            #  behaviour of the method is same for the particular
            # we can access class level identifiers 
            # className.MethodName()

# static Method
            # is a generic and independent method which is not depend on any class resoucre
            # className.MethodName()
