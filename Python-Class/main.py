class Employee():
    #double quotes means that we are overriding the method
    def __init__(self):
        self.Name = ""
        self.Designation = ""
    
    def SetName(self, name):
        self.Name = name
    
    def SetDesignation(self, designation):
        self.Designation = designation

class SoftwareEngineer(Employee):
    def __init__(self):
        Employee.__init__(self)
        Employee.SetDesignation(self, "Software Engineer")
        Employee.SetName(self, "Vikram")
        self.canWriteCode = True
        self.hasAccesstoLab = True
    
    def CanWriteCode(self, writeCode):
        self.canWriteCode = writeCode

    def HasAccessToLab(self, hasAccess):
        self.hasAccesstoLab = hasAccess

    
softwareEng = SoftwareEngineer()
softwareEng.HasAccessToLab(True)
softwareEng.CanWriteCode(True)

print(softwareEng.Name)
print(softwareEng.Designation)