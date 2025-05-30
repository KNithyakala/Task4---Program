# Question --3
# Happy Numbers
# A happy number is a number defined by the following process:

# Create a digitsquare function for sum of square the digits in the number

# Set variable for sum of square of the digits in the number(digitsum) as O
# Find last digit of the number by (n%10) and square it
# Keep on dividing the number by 10 will give remaining digits except last digit

# Create a happynumber function
# Set unhappy list to avoid exhaustive loops and add the number in the list (eg.22)
# using digitsquare function, it will find square of digits and sum (eg.16)
# The loop will continue upto n=1.
# but the function will check whether the number in unhappy list to avoid repetitive loops
#(for eg:22 -->22, 8, 64, 52, 29, 85, 89, 145, 42, 20, 4, 16, 37, 58) when digitsquare(58)=89. It is in unhappy list.

List1=[10,501,22,37,100,999,87,351]
Unhappynumber=[]
Happynumber=[]

def digitsquare(n):
    digitsum=0
    while n!=0:
        Ldigit=n%10
        digitsum+=Ldigit**2
        n=n//10
    return digitsum

def happynumber(n):
        unhappy=[]
        while n!=1:
            if n in unhappy:
                return False
            unhappy.append(n)
            n=digitsquare(n)
        return True

for i in range(len(List1)):
    if happynumber(List1[i]):
        Happynumber.append(List1[i])
    else:
        Unhappynumber.append(List1[i])

print("Happynumber List:",Happynumber)
print("Not Happynumber List",Unhappynumber)