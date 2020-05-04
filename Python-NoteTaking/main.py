def NoteTaking():
    fileName = input("Please enter file name: ")
    try:
        with open(fileName) as file:
            if(file.__exit__):
                fileOperation = input("input your operation with file: ")
                if(fileOperation == "read"):
                    print(file.read())
                elif(fileOperation == "delete"):
                    file.truncate()
                elif(fileOperation == "append"):
                    file.append()
                else:
                    print("Invalid operation")
            else:
                inputTest = input("Please enter the input text: ")
                #file
    except IOError:
         with open(fileName, "w") as file:
             file.write("My Test")
    


NoteTaking()

