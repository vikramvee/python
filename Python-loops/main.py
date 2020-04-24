def fizzBuzz():
    for number in range(1,101):
        if(isPrime(number)):
            print("prime")       
        elif(number % 3 == 0 and number % 5 == 0):
            print("FizzBuzz")
        elif(number % 3 == 0):
            print("Fizz")
        elif(number % 5 == 0):
            print("Buzz")
        else:
            print(number)

def isPrime(number):
    for num in range(2,number + 1):
        if(num != number and number % num == 0):           
            return False           
    return True
       

        
fizzBuzz()
            
