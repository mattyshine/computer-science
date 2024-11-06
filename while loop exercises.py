user_number=input("enter an integer number: ")
running_total=0
num_num=0
if user_number != "":
    while user_number !="":
        user_number=int(user_number)
        running_total = running_total + user_number
        num_num=num_num+1
        average = running_total/num_num
        user_number=input("Enter an integer number: ")
    else:
        print("The average of the numbers entered was: ",average)
else:
    print("The average of the numbers entered was: ",average)
    

print(" ")


user_1=int(input("enter an integer number: "))
running_1=0
num_1=0
if user_1 >= 0:
    while user_1 >=0:
        running_1 = running_1 + user_1
        num_1=num_1+1
        average_1 = running_1/num_1
        user_1=int(input("Enter an integer number: "))
    else:
        print("The average of the numbers entered was: ",average_1)
else:
    print("The average of the numbers entered was: ",average_1)
    
    
print(" ")


grade_1=int(input("Enter your test grade: "))
running_2=0
num_2=0
while grade_1 > 0:
    running_2 = running_2 + grade_1
    num_2=num_2+1
    average_2 = running_2/num_2
    grade_1=int(input("Enter your test grade: "))
else:
    print("Your average of the tests is: ",average_2)

if average_2>=90:
    print("You got an A")
elif average_2>=80 and average_2<90:
    print("You got a B")
elif average_2>=70 and average_2<80:
    print("You got a C")
elif average_2>=60 and average_2<70:
    print("You got a D")
elif average_2<60:
    print("You got an F")

        
print(" ")


int_1=int(input("Enter an integer: "))
while int_1>0:
    int_1=int_1-1
    print(int_1)


print(" ")


total=0
int_2=int(input("Enter an integer and I will list out all the even numbers: "))
while total <= int_2:
    total=total+2
    print(total)


print("While loop exercises part 2")


print(" ")


total_1=0
n_1=int(input("Enter an integer and I will list out all the even numbers: "))
n_1=n_1*n_1
while total_1 <= n_1:
    total_1=total_1+1
    if total_1 % 5 !=0:
        print(total_1)

    
print(" ")


interation_1=0
total_2=0
n_2=int(input("Enter an integer: "))
n_2=n_2*n_2
while interation_1 <= 50:
    interation_1=interation_1+1
    total_2=total_2+1
    print(total_2)


print(" ")


for int_4 in range(3,29):
    if int_4 % 2==0 and int_4 % 5 !=0:
        print(int_4)


print(" ")


start_1=int(input("Enter the start value for the range: "))
end_1=int(input("Enter the end value for the range: "))
multiple_1=int(input("Enter a multiple to ignore: "))
for int_5 in range(start_1,end_1):
    if int_5 % 2==0 and int_5 % multiple_1 !=0:
        print(int_5)
        

print(" ")


for int_6 in range(50,20,-1):
    if int_6 % 2==0 and int_6 % 3 !=0:
        print(int_6)


print(" ")


for int_6 in range(12,-14,-1):
    if int_6 % 2==0 :
        print(int_6)

