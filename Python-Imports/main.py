from  random import randint,random
import random as r
import time as t

random = random()
randInt = randint(0,10)

print(random)
print(randInt)

simpleList = [1,2,3,4,5]
pickElement = r.choice(simpleList)
print(pickElement)

currentTime = t.clock()
print(1)
pastTime = t.clock()
print(pastTime - currentTime)

t.sleep(1)
print("Hello World")