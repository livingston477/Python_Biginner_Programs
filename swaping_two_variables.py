#swap to variables in python 

p =int(input("Enter a Number for P:"))
q=int(input("enter a number for Q:"))

tem=p
p=q
q=tem

print("value of p:",p)
print("value of q:",q)


# By using comma operator
p =int(input("Enter a Number for P:"))
q=int(input("enter a number for Q:"))

p,q=q,p

print("value of p:",p)
print("value of q:",q)

# By using the XOR method
p =int(input("Enter a Number for P:"))
q=int(input("enter a number for Q:"))

p=p^q
q=p^q
p=p^q

print("value of p:",p)
print("value of q:",q)

#By using arithemitc operations
p =int(input("Enter a Number for P:"))
q=int(input("enter a number for Q:"))

p=p+q
q=p-q
p=p-q

print("value of p:",p)
print("value of q:",q)

#By using arithemitc operations
p =int(input("Enter a Number for P:"))
q=int(input("enter a number for Q:"))

p=p*q
q=p/q
p=p/q

print("value of p:",p)
print("value of q:",q)  

