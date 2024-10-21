name_1=input("What is your name: ")
for names in range(3):
    print(name_1)
    

print(" ")


name_2=input("What is your name: ")
num_1=input("Enter a number")
num_1=int(num_1)
for Names in range(num_1):
    print(name_2)


print(" ")


name=input("What is your name: ")
my_string=name
for character in my_string:
    print(character)


print(" ")


name=input("What is your name: ")
my_string1=name
num_2=input("Enter a number: ")
num_2=int(num_2)
for names_1 in range(num_2):
    for character_1 in my_string1:
        print(character_1)


print(" ")


num_3=int(input("Enter a number between 1 and 12: "))
for num_4 in range(13):
    print(num_3, "x",num_4, "=" , num_3*num_4)


print(" ")


num_5=int(input("Enter a number under 50: "))
for num_6 in range(50, num_5 ,-1):
    print(num_6)
print(num_5)


print(" ")


name_3=input("What is your name: ")
num_7=int(input("Enter a number: "))
if num_7<10:
    for num_8 in range(num_7):
        print(name_3)
else:
    for names in range(3):
        print("Too high")


print(" ")


total = 0
for totalnum in range(5):
    num_9=int(input("Enter a number: "))
    question_1=input("Do you want this number included?: ")
    question_1=question_1.upper()
    if question_1=="YES" :
        total += num_9
print(total)
 

print(" ")


input_1=input("Do you want to count up or down?: ")
input_1=input_1.lower()
if input_1=="up":
    num_10=int(input("What is the final number: "))
    for num_11 in range(0,num_10,+1):
            print(num_11)
            print(num_10)
elif input_1=="down":
    num_10=int(input("Pick a final number under 20: "))
    for num_11 in range(20,num_10,-1):
            print(num_11)
            print(num_10)
else:
    print("I do not understand")
 

print(" ")


invites_1=int(input("How many people do you want to invite to the party: "))
if invites_1<=10:
    for invites in range(invites_1):
        name_4=input("What is the guests name: ")
        print(name_4,"has been invited")
else:
    print("You dont have that number of friends!")
        
    
    








    
    
    
    