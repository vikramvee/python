myUniqueList = []
myLeftovers = []

def addValuesToUniqueList(value):
    if(not myUniqueList.__contains__(value)):
        myUniqueList.append(value)
        return True
    else:
        return False

def addValuesToLeftOvers(value):
    myLeftovers.append(value)

if(not addValuesToUniqueList(1)):
    addValuesToLeftOvers(1)

print(myUniqueList)
print(myLeftovers)

if(not addValuesToUniqueList(2)):
    addValuesToLeftOvers(2)

print(myUniqueList)
print(myLeftovers)

if(not addValuesToUniqueList(3)):
    addValuesToLeftOvers(3)

print(myUniqueList)
print(myLeftovers)

if(not addValuesToUniqueList(3)):
    addValuesToLeftOvers(3)

print(myUniqueList)
print(myLeftovers)
