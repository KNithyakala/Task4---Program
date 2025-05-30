#Question --1
#Odd and Even Number
#Create a list [10,501,22,37,100,999,87,351]
#Split the list into two list, one contains odd number and another contains even number
#Number which is divisible by 2 is even number

List1=[10,501,22,37,100,999,87,351]
List2=[]
List3=[]

for i in range(len(List1)):
    if List1[i]%2==0:
        List2.append(List1[i])
    else:
        List3.append(List1[i])

print("Given List of Numbers:",List1)
print("Even Numbers List:",List2)
print("Odd Numbers List:",List3)


