from getpass import getpass


HANGMANPICS = ['''
+---+
|   |
    |
    |
    |
    | 
=========''',
'''
 +---+
 |   |
 O   |
/    |
     |
     | 
=========''',
'''
 +---+
 |   |
 O   |
/|   |
 |   |
     | 
=========''',
'''
 +---+
 |   |
 O   |
/|\  |
 |   |
     | 
=========''',
'''
 +---+
 |   |
 O   |
/|\  |
 |   |
/    | 
=========''',
'''
 +---+
 |   |
 O   |
/|\  |
 |   |
/ \  | 
=========''']




def PlayHangMan():
    word = EnterTheWord()
    hangManGraphic = 0
    print(chr(27) + "[2J") 
    print("_ " * len(word), "")
    print(HANGMANPICS[hangManGraphic])
    wordCharacters = {}

    while(True):
        character = GuessTheCharacter()        

        characterFound = False
        for char in range(len(word)):
            if(character == word[char]):
                wordCharacters[char] = character
                characterFound = True

        if(characterFound == False):
            print(chr(27) + "[2J") 
            print("Character not present")
            hangManGraphic += 1
            print(HANGMANPICS[hangManGraphic])
        else:
            for char in range(len(word)):
                if(wordCharacters.get(char)):
                    print(wordCharacters[char], end = '')
                else:
                    print(" _", end = '')
            
            print("")

        if(hangManGraphic + 1 == len(HANGMANPICS) or wordCharacters.__len__ == len(word)):
           print("You lost the game")
           break
        elif len(wordCharacters) == len(word):
            print("You guessed the word right")
            break


def EnterTheWord():
    return getpass(prompt="Enter the word:")

def GuessTheCharacter():
    return input("Guess one character in the word: ")


PlayHangMan()