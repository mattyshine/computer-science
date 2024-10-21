day_1=float(input("What was the temperature on Monday: "))
day_2=float(input("What was the temperature on Tuesday: "))
day_3=float(input("What was the temperature on Wednesday: "))
day_4=float(input("What was the temperature on Thursday: "))
day_5=float(input("What was the temperature on Friday: "))
day_6=float(input("What was the temperature on Sataurday: "))
day_7=float(input("What was the temperature on Sunday: "))
num_1=(day_1+day_2+day_3+day_4+day_5+day_6+day_7)
print(num_1/7)


print(" ")


PI=3.14
x_1=int(input("Enter a value for X: "))
y_1=int(input("Enter a value for Y: "))
z_1=int(input("Enter a value for Z: "))
print(pow(x_1*4,4)+pow(y_1*3,3)+(z_1*9)+(PI*6))


print(" ")


seconds_1=int(input("Enter a time in seconds: "))
minutes_1=round(seconds_1/60)
print(minutes_1,"minutes",seconds_1 % 60,"seconds")


print(" ")


hour=int(input("Enter an hour between 1 and 12: "))
ahead=int(input("Enter how many hours ahead you want to go: "))
time=int(hour+ahead)
while time>12:
    time=time-12
print("In",ahead,"hours time it will be",time,"O'clock")


print(" ")


number=str(input("Enter a three digit number: "))
print(number[::-1])