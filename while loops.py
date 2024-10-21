total = 0
while total < 50:
    num_1=int(input("Enter a number: "))
    total = total + num_1
print(total)


print(" ")


num_2=int(input("Enter a number :"))
while num_2 !=5:
    num_2=int(input("Enter a number :"))
    

print(" ")


num_3=int(input("Enter a number :"))
num_4=int(input("Enter a number :"))
num_5=int(num_3+num_4)
print(num_5)
input_1 = input("Would you like to add another number :")
input_1=input_1.lower()
while input_1 =="y":
    num_6=int(input("What number would you like to add :"))
    input_1 = input("Would you like to add another number :")
    input_1 = input_1.lower()
print(num_5+num_6)
