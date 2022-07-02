import array as arr
a=arr.array('i',[1,4,3])
print("the new created array is:",end=" ")

for i in  range(0,3):
    print(a[i],end=' ')
print()

a.append(5)

for i in a:
    print(i, end=' ')
print()

a.insert(1,4)
for i in a:
    print(i,end=' ')

# accessing elements from the array 
print("\nAccess elements is :",a[1])
print("Access elements is :",a[3])    


# Removing elements from the Array
a.remove(1)
for i in a:
  print(i,end=' ')
print() 


#Removing elements from the Array
a.remove(4 )
for i in a:
    print(i,end=' ')
print()  



# Slicing of a Array
l = [1,2,3,4,5,6,7,8]

a=arr.array('i',l)
print( "Initial Array:")
for i in a :
    print(i, end=" ")
slice_array=a[5:8]
slice_array=a[:]
# slice_array=a[3:]
print('\n',slice_array)

# searching index of  the array
print("searching",a.index(5))



