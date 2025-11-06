from abc import ABC, abstractmethod    # ABC - Abstarct class



class Vehicle(ABC):
    @abstractmethod
    def start(self):
        print('Starting Engine.....')
        print('Fuel verification....')
        print('Sensors verifiaction')


    
    @abstractmethod
    def getMaterial(self) :
        pass
    
    @abstractmethod
    def getDesign(self) :
        pass

    @abstractmethod
    def pollutionCheck(self) :
        pass

    @abstractmethod
    def safetyCheck(self) :
        pass

    @abstractmethod
    def SeatBeltsCheck(self) :
        pass
    
#objVehicle= Vehicle()
#objVehicle.start()


class Car(Vehicle) :
    def start(self):
        print('Car started successfully')

    def getMaterial(self):
        print('got required Material')

    def SeatBeltsCheck(self):
        print('Seat belts are fine')

    def getDesign(self):
        print('Desin Finalised')

    def pollutionCheck(self):
        print('polution check done')
    
    def safetyCheck(self):
        print('safety check done')

objCar= Car()
objCar.start()
objCar.getMaterial()
objCar.getDesign()
objCar.pollutionCheck()
objCar.safetyCheck()
objCar.SeatBeltsCheck()

# Abstract classes classes can not be instantiated
# Should be inherited





