#while loop
a=1
while a<=50:
    if a%5==0:
        print(f"{a} is divisible by 5")
    else:
        print(f"{a} is not divisible by 5")
    a+=1

#for loop
for i in range(1,51,1):
    if i%5==0:
        print(f"{i} is divisible by 5")
    else:
        print(f"{i} is not divisible by 5") 