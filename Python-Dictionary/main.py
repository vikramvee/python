songDictionary = {"songName" : "Random Song", "year" : "2018","artist" : "Adams","genere" : "rock","duration" : "5 mins","publisher" : "Times music"}

def printDictionary():
    for item in songDictionary:
        print("Key: " + item + " Value: " +  songDictionary[item])


def guessKeyValue(key, value):
    if(key in songDictionary and songDictionary[key] == value):
        return True
    else:
        return False

print(guessKeyValue("songName", "Random Song"))

