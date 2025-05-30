#Prime Number
#Create a list [10,501,22,37,100,999,87,351]
#find primenumber in the list and store it in new list
#Prime Number-->A number that can be divided exactly only by itself and 1
#2 is prime number and 1 is neither prime nor composite

List1=[10,501,22,37,100,999,87,351]
primelist=[]
complist=[]

for i in range(len(List1)):
    n=List1[i]
    if n==2:
        primelist.append(List1[i])
    j=2
    while j<n:
        if n%j!=0:
            j=j+1
            if j==n:
                primelist.append(List1[i])
        elif n%j==0:
            complist.append(List1[i])
            break

print("Given List of Numbers:",List1)
print("Prime Numbers List:",primelist)
print("Composite Numbers List:",complist)
