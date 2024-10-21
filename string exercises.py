name_1=input("Enter your name: ")
print(len(name_1))


print(" ")


firstname_1=input("What is your firstname: ")
secondname_1=input("What is your secondname:")
print(firstname_1 , secondname_1)
print(len(firstname_1 + secondname_1))


print(" ")


firstname_2=input("Enter your firstname in lower case: ")
secondname_2=input("Enter your secondname in lower case:")
firstname_3=firstname_2.capitalize()
secondname_3=secondname_2.capitalize()
print(firstname_3 , secondname_3)


print(" ")


rhyme_1=input("Enter the first line of a nursery rhyme: ")
print(len(rhyme_1))
num_1=int(input("Give me a starting number: "))
num_2=int(input("Give me an ending number: "))
list_1=rhyme_1[num_1:num_2+1]
print(list_1)