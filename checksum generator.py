total=0
test_1=int(input("Enter a 9 digit number: "))
num_6=test_1
num_1=2
while test_1 > 0:
    test_2=test_1 % 10
    test_1=test_1 // 10
    test_2=test_2*num_1
    num_1=num_1+1
    total=total+test_2
    
num_3=total%11
num_4=11-num_3
print(num_6,num_4,sep="")
    


    