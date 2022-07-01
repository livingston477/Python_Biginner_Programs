# Function for the nth Fibonacci number

def Fibonacci(n):

    #Check if input is 0 then it will
    #print incorrect input
    if n < 0:
        print("Incorrect input")
    # check if n is 0
    # then it will return 0
    elif n==0:
        return 0
    # check if n is 1,2 
    # it will return 1
    elif n ==1 or n==2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
print(Fibonacci(6))

#Dynamic programming ## Another Method
FibArray =[0,1]

def fibonacci(n):
    if n <0:
        print("incoorect input")
    elif n < len(FibArray):
        return FibArray[n]
    else:
        FibArray.append(fibonacci(n-1)+fibonacci(n-2))
        return FibArray[n]

print(fibonacci(9))




