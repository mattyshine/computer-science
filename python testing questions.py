#question 8
n=int(input("Enter an integer:"))
if n>0:
    for a in range(1,n+n):
        print(a/(n/2))
else:
    print("Now quiting")

print(" ")

#question 9
#(i)
for b in range(100,0,-3):
    print(b)

print(" ")

#(ii)
num=int(input("Enter a number: "))
num_1=num
for x in range(num):
    if num_1 <0:
        break
    print(num%10)
    num=num/10

print(" ")

#(iii)
num3=int(input("Enter a number :"))
count=0
sum1=0
for z in range(num3,0,-2):
    count += 1
    sum1 += z
    if count == 10 :
        print (sum1/float(count))
        break
    
print(" ")

#question 10

num4=int(input("Enter a number: "))
min=0
l=0
sum3=0
max=num4
if num4<0:
    min=num4
    max=0
    while l<num4:
        sum3+=l
        print(sum3)
        l+=1


print(" ")

#question 11
#m
for x in range(3):
    for y in range(4):
        print(x,y,x+y)

print(" ")

#n
c=0
for x in range(10):
    for x in range(5):
        c+=1
print(c)

print(" ")

#question 12
 for i in range(4):
    for j in range(5):
        if i + 1==j or j+i==4:
            print("+",end=" ")
        else:
            print("o",end=" ")
print()

print(" ")

#question 15
a =int(input("Enter a value: "))
count=0
while a != 0:
    count=count +1
    a =int(input("Enter a value: "))
print("You entered",count,"values.")




        

    