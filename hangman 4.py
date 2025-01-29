word="appple"
length=len(word)
spares="_ "*length
print(spares)
spare="_"*length
count=7*length
question=input("Do you wnat to play Hangman: ")
while question=="yes":
    while count>0 and spare!=word:
        x=input("Enter a guess: ")
        num1=word.find(x)
        num2=word.count(x)
        word2=word[:num1]+"_"+word[num1+1:]
        num3=word2.find(x)
        if num2<=1:
            for t in word:
                if t==x:
                    spare=spare[:num1]+x+spare[num1+1:]
                    print(spare)
                else:
                    count-=1
        elif num2==2:
            for l in word:
                if l==x:
                    spare=spare[:num1]+x+spare[num1+1:num3]+x+spare[num3+1:]
                    print(spare)
                else:
                    count-=1
        elif num2==3:
            for l in word:
                if l==x:
                    word3=word[:num1]+"_"+word[num1+1:num3]+"_"+word[num3+1:]
                    num4=word3.find(x)
                    spare=spare[:num1]+x+spare[num1+1:num3]+x+spare[num3+1:num4]+x+spare[num4+1:]
                    print(spare)
                else:
                    count-=1
    question=input("Do you want to play again: ")
    count=7
    spare="_"*length


    
            
        

