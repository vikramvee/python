def ParameterEquality(first, second, third):
    intFirst = int(first)
    intSecond = int(second)
    intThird = int(third)

    if intFirst == intSecond or intFirst == intThird or intThird == intFirst or intFirst == intSecond == intThird:
        return True
    else:
        return False

print(ParameterEquality(1,"1", 3))
