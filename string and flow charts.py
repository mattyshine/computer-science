# String amd flow chart sheet
#Question 1
string=input("Enter a string:")
for a in range(0,len(string)):
    print(string[a])

print(" ")

string_1=input("Enter a string: ")
for y in string_1:
    print(y)

print(" ")

str_1=input("Emter a string: ")
x=len(str_1)
A=0
B=0
while A<x:
    print(str_1[B])
    B+=1
    A+=1

print(" ")

#question 2
st_1=input("Enter a string:")
alpha=" "
for d in range(0,len(st_1)):
    if st_1[d].isupper():
        alpha=alpha+st_1[d].lower()
    elif st_1[d].islower():
        
        alpha=alpha+st_1[d].upper()
    else:
        alpha=alpha+st_1[d]
print(alpha)

print(" ")
st_2=input("Enter a string:")
new=" "
for m in st_2:
    if m.isupper():
        new+=m.lower()
    elif m.islower():
        new+=m.upper()
    else:
        new+=m
print(new)

print(" ")

st_3=input("Enter a string:")
empty=" "
C=0
D=0
l=len(st_3)
while C<l:
    t=st_3[D]
    if t.isupper():
        empty+=t.lower()
    elif t.islower():
        empty+=t.upper()
    else:
        empty+=t
    C+=1
    D+=1
print(empty)

print(" ")

#question 3
int_1=input("Enter a string and i will double each character: ")
empty_1=" "
for n in range(0,len(int_1)):
    z=int_1[n]
    empty_1+=(z*2)
print(empty_1)

print(" ")

int_2=input("Enter a string and i will double each character: ")
empty_2=" "
for v in int_2:
    empty_2+=(v*2)
print(empty_2)

print(" ")

int_2=input("Enter a string and i will double each character: ")


    

        