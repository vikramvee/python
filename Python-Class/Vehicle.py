class Vehicle():
    def __init__(self):
        self.NeedsMaintainenance = False
        self.TripsSinceMaintenance = 0
       

    def SetMake(self, make):
        self.Make = make

    def SetModel(self, model):
        self.Model = model

    def SetYear(self, year):
        self.Year = year

    def SetWeight(self, weight):
        self.Weight = weight

    def Repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintainenance = False

    def __str__(self):
        print("Make: " + self.Make)
        print("Model: " + self.Model)
        print("Year: " + str(self.Year))
        print("Weight: " + str(self.Weight))
        print("NeedsMaintainenance: " + str(self.NeedsMaintainenance))
        print("TripsSinceMaintenance: " + str(self.TripsSinceMaintenance))
        return self.Make

class Cars(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
    
    def Drive(self):
        self.IsDriving = True
        self.TripsSinceMaintenance += 1
        if(self.TripsSinceMaintenance > 100):
            self.NeedsMaintainenance  = True

    def Stop(self):
        self.IsDriving = False    



class Planes(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)

    def Flying(self):
        self.IsFlying = True
        if(self.NeedsMaintainenance == False)
            self.TripsSinceMaintenance += 1
            return True
        else:
            print("Cannot Fly")
            return False

    def Landing(self):
        self.IsFlying = False   



myCar = Cars()
myCar.SetModel("Maruti")
myCar.SetMake("Ritz")
myCar.SetYear(2011)
myCar.SetWeight(1000)

dadcar = Cars()
dadcar.SetModel("Maruti")
dadcar.SetMake("Zen")
dadcar.SetYear(2005)
dadcar.SetWeight(1000)


wifeCar = Cars()
wifeCar.SetModel("Maruti")
wifeCar.SetMake("SX4")
wifeCar.SetYear(2019)
wifeCar.SetWeight(1000)



for i in range(101):
    myCar.Drive()
    dadcar.Drive()
    wifeCar.Drive()

print(myCar)
print(dadcar)
print(wifeCar)

myCar.Repair()

print(myCar)

    
    
