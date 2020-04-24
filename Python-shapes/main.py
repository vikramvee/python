
def DrawShape():
    ToPrint = "*"
    Length = 10

    for char in range(1,Length  + 1):
        BlankSpaceLength = (Length * 2)  - (char * 2)
        Space = " " * BlankSpaceLength
        print(ToPrint * char + Space + ToPrint * char ) 
        

    for char in range(Length - 1, 0, -1):
        BlankSpaceLength = (Length * 2)  - (char * 2)
        Space = " " * BlankSpaceLength
        print(ToPrint * char + Space + ToPrint * char ) 

def DrawTriangle():
    rows = 10
    charToDraw = "*"
    for rownumber in range(rows + 1):
        print(" " * (rows - rownumber) + charToDraw * (2 * rownumber - 1))

def DrawInvertedTriangle():
    rows = 10
    charToDraw = "*"
    for rownumber in range(rows, 0 , -1):
        print(" " * (rows - rownumber) + charToDraw * (2 * rownumber - 1))
        
DrawShape()