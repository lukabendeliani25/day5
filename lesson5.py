

full_name = input("enter your full_name: ")

index = 0
while index<len(full_name):
    if full_name[index] in "aeiou":
        print(str(index) + full_name[index])
    index +=1

