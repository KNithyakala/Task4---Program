#Question --7
#Program---> Non-repeating elements in list of integers
#create list with integers
#Check the values with another values
#if it is not repeating then print the value

List1=[45,89,67,90,12,34,45,67,-89,0]

for i in range(len(List1)):
    a=List1[i]
    c=List1.count(a)
    if c==1:
        print("First Nonrepeating elements in the list:",List1[i])
        break
    else:
        continue

