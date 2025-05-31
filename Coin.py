#Question--5
#To find all the ways to make Rs.10 using Rs.1, Rs.2, Rs.5 and Rs.10
#create a list with 1,2,5,10
#In for Loop,
#Giving higher range("10+1") to minimum of the list("1")
#Giving lower range("1+1") to maximum of the list("10")


List1=[1,2,5,10]
List1.sort()
count=0
Target = 10

print("The ways to make Rs.10:")

for i in range(List1[3]+1):
    for j in range(List1[2]+1):
        for k in range(List1[1]+1):
            for l in range(List1[0]+1):
                if i*1+j*2+k*5+l*10==Target:
                    count+=1
                    print(f"Combination {count}: 1Rs:{i}, 2Rs:{j}, 5Rs:{k}, 10Rs:{l}")


