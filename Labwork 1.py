r = float(input("Enter radius: "))
s = r**2*3.14
print("Area = ",s)


#Ex 2
C = float(input("Enter temperature in Celsius: "))
F = 1.8*C + 32
print("Temperature in Fahrenheit: ", F)


#Ex 3
a = 3
flag =1

if a<2:
    print(a, " is not prime")
elif a==2:
    print(a, "is prime")
else:
    for i in (2,a):
        if a%i==0:
            flag = 0
            break

if flag ==0:
    print(a," is not prime")
else:
    print(a, "is prime")


#Ex 4
x4 = 6
sumcheck=0
for i in (1,x4):
    if x4%i==0:
        print(i)
        sumcheck+=i

if sumcheck==x4:
    print(x4, " is perfect")
else:
    print(x4, " is not perfect")


#Ex 5
ColorList = ["Red", "Blue", "Yellow","White"]
Color = str(input("Type your favorite color: "))


def CheckIndexColor(n):
    found = 0
    for i in range(len(ColorList)):
        if n == ColorList[i]:
            print("Your color is at index ",i," of my list")
            found = 1
            break
    if found ==0 :
        print("Your color is not in my list")

CheckIndexColor(Color)


#Ex 6

range1 = range(0,7)
range2 = range(1,13,3)
range3 = range(5,0,-1)
range4 = range(6,-4,-2)
for i in range1:
    print(i,end= " ")
for i in range2:
    print(i,end= " ")
for i in range3:
    print(i,end= " ")
for i in range4:
    print(i,end= " ")

#Ex 7
s = str(input("Enter the string: "))

def remove_dollar_sign(n):
    newstring = ""
    for i in n:
        if i!="$":
            newstring+=i
    print(newstring)

remove_dollar_sign(s)

#Ex 8
List = [1, 4, 5, -1, 10]

def extract_even(I):
    result = [i for i in I if i % 2 == 0 and i >= 0]
    print(result)

extract_even(List)


#Ex 9
n = 0

def factorial(i):
    if i<0:
        print("must be non negative integer")
    elif i==0:
        return 0
    elif i==1:
        return 1
    else:
        return i*factorial(i-1)

fac = factorial(n)

print(fac)

#Ex 10
def extract_divisors(n):
    divisors = []
    i=1
    while i<=n:
        if n%i==0:
            divisors.append(i)
        i+=1
    print(divisors)

a=10
extract_divisors(a)



#Ex 11
a = (2,3)
b= (7,1)

distance = ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
print(distance)


#Ex 12
m = 5
n = 4

for i in range(1,m+1):
    for j in range(1,n+1):
        if i==1 or j==1 or i==m or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()