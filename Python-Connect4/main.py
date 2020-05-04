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
    
    while(IsWinner()):
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
        print(boardInMemory)
        drawPalyingBoard(6, 7)
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
    CheckHorizonatally()

def CheckHorizonatally(row, column, symbol):
    while True:
        if(boardInMemory[row][column] != symbol):
            break       
        


def SwitchThePlayer(turnof):
    if(turnof == "player 1"):
        return "player 2"
    else:
        return "player 1"

playTheGame()


