#Code predictions
# question 1
#a
print("""
1
  2
    3
""")

print(" ")

#b
text="Test.\nNext line."
print(text)

print(" ")

#c
print("One", "Two"*2)
print("One"+"Two"*2)
print(len("0123456789"))

print(" ")

#d
s="0123456789"
print(s[:3],",",s[0:3],"-",s[2:5])
print(s[:3],"-",s[3:],",",s[3:100])
print(s[20:],s[2:1],s[1:1])

print(" ")

#e
s="987654321"
print(s[-1],s[-3])
print(s[-3:],s[:-3])
print(s[-100:-3],s[-100:3])

print(" ")

#Q2
#a
y=str(123)
x="hello"*3
print(x,y)
x="hello"+"world"
y=len(x)
print(y,x)

print(" ")

#b
x="hello"+\
"to python"+\
"World"
for char in x:
    y=char
    print(y,":",end="")
    
print(" ")

#c
x="hello world"
print(x[:2],x[:-2],x[-2:])
print(x[6],x[2:4])
print(x[2:-3],x[-4:-2])

print(" ")

#question 3
thestr="this is a test"
inputstr=input("Enter an integer:")
inputint=int(inputstr)
teststr=thestr
while inputint>=0:
    teststr=teststr[1:-1]
    inputint=inputint-1
testBool="t" in teststr
print(thestr)
print(teststr)
print(inputint)
print(testBool)

print(" ")

#question 4
teststr="abcdefghi"
inputstr=input("Enter an integer:")
inputint=int(inputstr)
count=2
newstr=""
while count<=inputint:
    newstr+=teststr[0:count]
    teststr=teststr[2:]
    count+=1
print(newstr)
print(teststr)
print(count)
print(inputint)

print(" ")

#q 5
inputStr = input("Give me a string:")
biglnt = 0
littlelnt = 0
otherlnt = 0
for ele in inputStr:
    if ele >= 'a' and ele <= 'm':
        littlelnt = littlelnt + 1
    elif ele > 'm' and ele <= 'z':
        biglnt = biglnt + 1
    else:
        otherlnt = otherlnt + 1
print (biglnt)
print (littlelnt)
print (otherlnt)
print (inputStr.isdigit())

print(" ")

# q6
in1Str = input(" Enter string of digits: ")
in2Str = input(" Enter string of digits: ")
 
if len(in1Str)>len(in2Str):
    small = in2Str
    large = in1Str
else:
    small = in1Str
    large = in2Str
newStr = ''
for element in small:
    result = int(element) + int(large[0])
    newStr = newStr + str(result)
    large = large[1:]
print (len(newStr))
print (newStr)
print (large)
print (small)

print(" ")

#Q7
#a
S = input("Enter String:")
RS = " "
for ch in S:
    RS = ch + RS
print(S + RS)
 
print(" ")

#b
S = input("Enter string :")
RS = " "
for ch in S:
    RS = ch + "2" + RS
print(RS + S)

print(" ")

#Q8
#a
S = "PURA VIDA"
print(S[9] + S[9:15])
 
#b
S = "PURA VIDA"
S1 = S[: 10] + S[10:]
S2 = S[10] + S[-10]
 
#c
S = "PURA VIDA"
S1 = S* 2
S2 = S1[-19] + S1[-20]
S3 = S1[-19:]
 
#d
S = "PURA VIDA"
S1 = S[: 5]
S2 = S[5:]
S3 = S1 * 52
S4 = S2 + '3'
S5 = S1 + 3
