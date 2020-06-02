#The method checks the equality of the three variables passed to this method
def ParameterEquality(first, second, third):
    try:
        intFirst = int(first)
        intSecond = int(second)
        intThird = int(third)

        if intFirst == intSecond or intFirst == intThird or intThird == intFirst or intFirst == intSecond == intThird:
            return True
        else:
            return False
    except ValueError as e:
        print(str(e))
    except Exception as identifier:
        print(identifier)
    

print(ParameterEquality(1,"Hello", "#"))
print(ParameterEquality(1,"2", "3"))
print(ParameterEquality(1,"", "3"))
print(ParameterEquality(1, 2, 2))

