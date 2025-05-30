#Question --9
#Create a list of integers
#Forming triplet to make particular sum from List

List1=[10,20,30,9]
NList=[]
S=59
l=len(List1)
Triplet=[]

for i in range(l-2):
    S1=0
    for j in range (i+1,l-1):
        for k in range(j+1,l):
            S1=List1[i]+List1[j]+List1[k]
            if S1==S:
                NList.append(List1[i])
                NList.append(List1[j])
                NList.append(List1[k])


print("Given List",List1)
print("Triplets forming sum",S, "is",NList)


