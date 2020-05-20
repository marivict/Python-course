class Vehiculo():
    def __init__(self, brand, model, years):
        self.__brand = brand
        self.__model = model
        self.__years = years
        self.ruedas = 4

        self.__gas = 100
        self.doors = 4
        self.__color = "blanco"
        self.__doorsStatus = "Cerradas"

        self.__passenger = 0

    def getBrand(self):
        return self.__brand
    def setBrand(self, brand):
        self.__brand = brand
        
    def getModel(self):
        return self.__model
    def setModel(self, model):
        self.__model = model
        
    def getYears(self):
        return self.__years
    def setYears(self, years):
        self.__years = years
        
    def getColor(self):
        return self.__color
    def setColor(self, color):
        self.__color = color

    def setDoors(self, doors):
        self.doors = doors
    def getDoors(self):
        return self.doors

    def setWheels(self, wheels):
        self.wheels = wheels
    def getWheels(self):
        return self.wheels

    def openDoors(self):
        self.__statusDoor == "Abiertas"
    def closeDoors(self):
        self.__statysDoors == "Cerradas"

    def addPassenger(self, passenger):
        pass
        
    def displayPassenger(self):
        return "Hay {} pasajeros".format(self.__passenger)
    
    def getInfo(self):
        print("="*15)
        print("Marca: {} \nModelo: {} \nAño: {}\nColor: {}\nRuedas: {} \nPuertas: {}".format(self.getBrand(), self.getModel(), self.getYears(), self.getColor(), self.getWheels(), self.getDoors()()))
        print("="*15)

    def getStatus(self):
        if self.__gas > 0 and self.__doorsStatus == "Cerradas":
            return True
        else:
            return False

    def getReport(self):
        print("="*15)
        print("Reporte:\n","Gas:",self.__gas,"\n", "Puertas:", self.__doorsStatus, "\n", self.displayPassenger() )
        print("="*15)
        
    def turnOn(self, mode):
        status = self.getStatus()
        if mode and status:
            return True           
        elif mode and status == False:
            return False

        return mode
 
    def turnOff(self):
        print("Apagando...")
        self.turnOn(False)

    def drive(self):
        if self.turnOn(True):
            print("Encendiendo... Listo")
            print("Los comandos son: 1 hacia adelante, 2 hacia la izquierda, 3 hacia atrás, 4 hacia la derecha, 5 frenamos, 6 apagamos el vehículo.")
            while self.turnOn(True) and self.__gas > 0:
                number = int(input("Introduzca comando... "))
                if number == 1:
                    self.driveFoward()
                elif number == 2:
                    self.driveLeft()
                elif number == 3:
                    self.driveBack()
                elif number == 4:
                    self.driveRight()
                elif number == 5:
                    self.brake()
                elif number == 6:
                    self.turnOff()
                    self.getReport()
                    break
                else:
                    self.turnOff()
                    print("Debe introducir un numero del 1 al 6")
                    
                       
            if self.__gas == 0:
                print("Se ha acabado el combustible")
                self.turnOff()
        else:
            print("Algo a ido mal en el chequeo. No podemos arrancar.")
                
        
    def driveFoward(self):
        print("Conduciendo hacia adelante")
        self.__gas -=5
    def driveLeft(self):
        print("Doblando hacia la izquierda")
        self.__gas -=5
    def driveBack(self):
        print("Dando reversa")
        self.__gas -=5
    def driveRight(self):
        print("Doblando hacia la derecha")
        self.__gas -=5
    def brake(self):
        print("Frenando...")
        self.__gas -=10

class Carro(Vehiculo):
    def __init__(self, brand, model, years):
       Vehiculo.__init__(self, brand, model, years)
       self.__passenger = 0
       
    def addPassenger(self, passenger):
        self.__passenger += passenger
        

        if self.__passenger < 0:
            self.__passenger = 0
            return "No puedes quitar pasajeros que no estan"
        elif self.__passenger < 4 :
            result = 4 - self.__passenger
            return "Hay {} pasajeros. Se puden montar {} pasajeros más".format(self.__passenger, result)
        else:
            self.__passenger = 4
            return "Hay {} pasajeros. Ya no se pueden montar más".format(self.__passenger);
class Camion(Vehiculo):
    def __init__(self, brand, model, years):
       Vehiculo.__init__(self, brand, model, years)
       self.doors = 2
       self.__gas = 0

    def carry(self, carry):
        self.__carry = carry

        if self.__carry:
            return "El camión esta cargado"
        else:
            return "El camión no esta cargado"
        
    def addPassenger(self, passenger):
        self.__passenger += passenger

        if self.__passenger < 0:
            self.__passenger = 0
            return "No puedes quitar pasajeros que no estan"
        elif self.__passenger < 2 :
            result = 2 - self.__passenger
            return "Hay {} pasajeros. Se puden montar {} pasajeros más".format(self.__passenger, result)
        
        else:
            self.__passenger = 2
            return "Hay {} pasajeros. Ya no se pueden montar más".format(self.__passenger);
           
class Bus(Vehiculo):
    def __init__(self, brand, model, years):
       Vehiculo.__init__(self, brand, model, years)
       self.doors = 2

       def addPassenger(self, passenger):
        self.__passenger += passenger

        if self.__passenger < 0:
            self.__passenger = 0
            return "No puedes quitar pasajeros que no estan"
        elif self.__passenger < 30 :
            result = 30 - self.__passenger
            return "Hay {} pasajeros. Se puden montar {} pasajeros más".format(self.__passenger, result)
        
        else:
            self.__passenger = 30
            return "Hay {} pasajeros. Ya no se pueden montar más".format(self.__passenger);
       
class Motor(Vehiculo):
    def __init__(self, brand, model, years):
       Vehiculo.__init__(self, brand, model, years)
       self.wheels = 2
       self.doors = 0
       self.__passenger = 0

    def addPassenger(self, passenger):
        self.__passenger += passenger

        if self.__passenger < 0:
            self.__passenger = 0
            return "No puedes quitar pasajeros que no estan"
        elif self.__passenger < 2 :
            result = 2 - self.__passenger
            return "Hay {} pasajeros. Se puden montar {} pasajeros más".format(self.__passenger, result)
        else:
            self.__passenger = 2
            return "Hay {} pasajeros. Ya no se pueden montar más".format(self.__passenger)


     
#funcion de evaluar estados
#funcion de evaluar año
