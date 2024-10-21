num_1=input("Enter a number: ")
num_1=int(num_1)
num_2=input("Enter a second number: ")
num_2=int(num_2)
if num_2>num_1:
    print(num_2,num_1)
else:
    print(num_1,num_2)
    
    
print(" ")
    
    
num_3=input("Enter a number under 20: ")
num_3=int(num_3)
if num_3<20:
    print("Thank you")
else:
    print("Too high")
    
    
print(" ")


num_4=input("Enter a number between 10 and 20: ")
num_4=int(num_4)
if num_4 > 9 and num_4 < 21:
    print("Thank you")
else:
    print("Incorrect answer")
    
    
print(" ")


colour_1=input("What is your favourite colour: ")
if colour_1=="red" or colour_1=="Red" or colour_1=="RED":
    print("I like red too")
else:
    print("I dont like",colour_1,",I prefer red")
    
    
print(" ")


rain_1=input("Is it raining?: ")
rain_1 = rain_1.lower()
if rain_1=="yes":
    wind_1=input("Is it windy?: ")
    wind_1 = wind_1.lower()
    if wind_1=="yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")
    

print(" ")


age_1=input("Enter your age: ")
age_1=int(age_1)
if age_1>=18:
    print("You can vote")
elif age_1==17:
    print("You can learn to drive")
elif age_1==16:
    print("You can buy a lottery ticket")
elif age_1<=15:
    print("You can go Trick-or-Treating")


print(" ")


num_5=input("Enter a number: ")
num_5=int(num_5)
if num_5<10:
    print("Too low")
elif num_5>=10 and num_5<=20:
    print("Correct")
else:
    print("Too high")
    
    
print(" ")


num_6=input("Enter one of the following numbers 1 2 or 3: ")
num_6=int(num_6)
if num_6==3:
    print("Correct")
elif num_6==2:
    print("Well done")
elif num_6==1:
    print("Thank you")
else:
    print("Error message")
    
