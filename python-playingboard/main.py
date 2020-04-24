def drawPalyingBoard(row, column):   

    for drawRow in range(0, row):
        if(drawRow == 0):
            print(" _" * column)
        for drawColumn in range(0,column):           
                print("|", end = "")
                if(drawColumn < column):
                    print("_", end = "")   
                if(drawColumn == column - 1):  
                    print("|")          


drawPalyingBoard(5,3)