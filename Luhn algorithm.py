total=0
test_1=int(input("Enter your credit card number: "))
test_5=test_1
test_1=test_1//10
while test_1 > 0:
    test_2=test_1 % 10
    test_1=test_1 // 100
    test_2=test_2*2
    if test_2>9:
        test_2=test_2-9
    else:
        test_2=test_2
    total=total+test_2
while test_5 > 0:
    test_4=test_5 % 10
    test_5=test_5 // 100
    total=total+test_4
if total % 10 ==0:
    print("Valid")
    
else:
    print("Fake card number!!! ")

    















            
    
    