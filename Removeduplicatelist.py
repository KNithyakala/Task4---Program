#Question --6
#To find duplicates in three lists
#Create 3 lists with integers
#Create newlist and store the common values in three list using for loop

List1=[34,19,27,100,46,9,87]
List2=[12,34,50,87,100,10]
List3=[8,12,45,89,100,46,34]
newlist=[]

for i in range(len(List1)):
    for j in range(len(List2)):
        for k in range(len(List3)):
            if List3[k]==List2[j] and List3[k]==List1[i]:
                newlist.append(List3[k])

print("Duplicates in three list:",newlist)


