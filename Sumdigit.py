#Question --4
#Sum of first and Last digit of the number
#Need to find the First and Last digit of the number and then add first and last digit

a=int(input("Enter an integer:"))
f=a
l=a%10

if a>10:
    while f>=10:
        f=f//10
        l=a%10
else:
    l=0

s=f+l

print("Sum of first and last digit of entered number:",s)
