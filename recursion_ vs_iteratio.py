# Python program to find factorial of given number

#---------Recursion---------
# method to find find factorial of given number
def recursion(n):
    if (n==0):
        return 1
    else:
        res= n * recursion(n-1) 
        return  res

print("Recurion value:",recursion(10))


#------Iteratio-----
# Method to fond the factorial of a given number
def iteration(n):
    res =1
     # using "for loop" for iteration
    for i in range(2, n+1):
        res *= i;
    return res
print("iteration value:",iteration(10))        



