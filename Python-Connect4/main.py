rows = [''] * 7
boardInMemory = [['','','','','','',''], ['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','','']];

def drawPalyingBoard(row, column):   

    for drawRow in range(0, row):
        if(drawRow == 0):
            print("  _" * column)
        for drawColumn in range(0,column):
                if(boardInMemory[drawRow][drawColumn] != ''):           
                    print("|", end = boardInMemory[drawRow][drawColumn])
                else:
                    print("|", end = " ")

                if(drawColumn < column):
                    print("_", end = "")   
                if(drawColumn == column - 1):  
                    print("|")
    
def playTheGame():
    print("Symbol for player 1 is X")
    print("Symbol for player 2 is O")
    turnof = "player 1"
    
    while(True):
        column = int(input("Enter the column for " + turnof + " :"))
        if(column > 7):
            print("column should be less than 7")
            continue

        row = GetTheCorrectRow(column)
        symbol = ''
        if(turnof == "player 1"):
            symbol = 'X'
        else:
            symbol = 'O'

        MakeTheMove(row, column, symbol)
        #print(boardInMemory)
        drawPalyingBoard(6, 7)
        
        if(IsWinner(row, column, symbol)):
            print(turnof + " is the winner")
            break

        turnof = SwitchThePlayer(turnof)


def GetTheCorrectRow(column):
    if(boardInMemory[5][column] == ''):
        return 5
    elif(boardInMemory[4][column] == ''):
        return 4
    elif(boardInMemory[3][column] == ''):
        return 3
    elif(boardInMemory[2][column] == ''):
        return 2
    elif(boardInMemory[1][column] == ''):
        return 1
    elif(boardInMemory[0][column] == ''):
        return 0
    
def MakeTheMove(row, column, symbol):
    boardInMemory[row][column] = symbol

def IsWinner(row, column, symbol):
    return CheckHorizonatally(row, column, symbol) or CheckVertically(row, column, symbol) or CheckDiagonally(row, column, symbol)


def CheckDiagonally(row, column, symbol):    
        checkCount = 0
        checkCount = CheckFirstQuadrant(row, column, symbol, checkCount)
        checkCount = CheckThirdQuadrant(row, column, symbol, checkCount)

        if(checkCount == 3):
            return True
        
        checkCount = 0 
        checkCount = CheckSecondQuadrant(row, column, symbol, checkCount)
        checkCount = CheckFourthQuadrant(row, column, symbol, checkCount)

        if(checkCount == 3):
            return True

        return False


def CheckVertically(row, column, symbol):   
    checkCount = 0
    checkCount = CheckUp(row, column, symbol, checkCount)
    checkCount = CheckDown(row, column, symbol, checkCount)

    if(checkCount == 3):
        return True 
    else:
        return False

def CheckFirstQuadrant(row, column, symbol, checkCount):
    backPointer = -1
    while checkCount < 4:
        if(((row +  backPointer) < 6 or (column + backPointer < 7)) and boardInMemory[row + backPointer][column + backPointer] == symbol):
            backPointer -= 1
            checkCount += 1
        else:
            return checkCount

    return checkCount 

def CheckSecondQuadrant(row, column, symbol, checkCount):
    rowBackPointer = -1
    columnForwardPointer = 1
    while checkCount < 4:
        if(((row +  rowBackPointer) < 6 or (column + columnForwardPointer < 7)) and boardInMemory[row + rowBackPointer][column + columnForwardPointer] == symbol):
            rowBackPointer -= 1
            columnForwardPointer += 1
            checkCount += 1
        else:
            return checkCount

    return checkCount 

def CheckThirdQuadrant(row, column, symbol, checkCount):
    forwardPointer = 1
    while checkCount < 4:
        if(((row +  forwardPointer) < 6 or (column + forwardPointer < 7)) and boardInMemory[row + forwardPointer][column + forwardPointer] == symbol):
            forwardPointer += 1
            checkCount += 1
        else:
            return checkCount
   
    return checkCount

def CheckFourthQuadrant(row, column, symbol, checkCount):
    rowForwardPointer = 1
    columnBackPointer = -1
    while checkCount < 4:
        if(((row +  rowForwardPointer) < 6 or (column + columnBackPointer < 7)) and boardInMemory[row + rowForwardPointer][column + columnBackPointer] == symbol):
            rowForwardPointer += 1
            columnBackPointer -= 1
            checkCount += 1
        else:
            return checkCount

    return checkCount 

def CheckDown(row, column, symbol, checkCount):
    forwardPointer = 1
    while checkCount < 4:
        if((row +  forwardPointer) < 6 and boardInMemory[row + forwardPointer][column] == symbol):
            forwardPointer += 1
            checkCount += 1
        else:
            return checkCount

    return checkCount      

def CheckUp(row, column, symbol, checkCount):
    backPointer = -1
    while checkCount < 4:
        if((row +  backPointer) > -1 and boardInMemory[row + backPointer][column] == symbol):
            backPointer -= 1
            checkCount += 1
        else:
            return checkCount

    return checkCount

def CheckHorizonatally(row, column, symbol):
   
    checkCount = 0
    checkCount = CheckForward(row, column, symbol, checkCount)
    checkCount = CheckBackward(row, column, symbol, checkCount)
    if(checkCount == 3):
        return True 
    else:
        return False

def CheckForward(row, column, symbol, checkCount):
    forwardPointer = 1
    while checkCount < 4:
        if((column +  forwardPointer) < 7 and boardInMemory[row][column + forwardPointer] == symbol):
            forwardPointer += 1
            checkCount += 1
        else:
            return checkCount
    
    return checkCount     

def CheckBackward(row, column, symbol, checkCount):
    backPointer = -1   
    while checkCount < 4:
        if((column +  backPointer) > -1 and boardInMemory[row][column + backPointer] == symbol):
            backPointer -= 1
            checkCount += 1
        else:
            return checkCount
   
    return checkCount 
        
def SwitchThePlayer(turnof):
    if(turnof == "player 1"):
        return "player 2"
    else:
        return "player 1"

playTheGame()


