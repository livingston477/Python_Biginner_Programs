# checking the value palindrome are not
S=input("Enter the value:")
reverse =S[::-1]

if (S == reverse):
    print("yes it is palindrome")
else:
    print("no it is not palindrome")   


#Palindrome number program using while loop
Num=int(input("enter a num:"))


reverse=0
while (Num>0):
    dig =Num % 10
    reverse=reverse *10 + dig
    Num =Num // 10
if (Num ==reverse):
    print("yes it is palindrome")
else:
    print("no it is not palindrome")   




