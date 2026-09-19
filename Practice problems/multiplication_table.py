#While loop
a=1
b=int(input("Enter the number of table u want to print: "))
while a<=10:
    print(f"{b} x {a} = {b*a}")
    a+=1

#for loop
b=int(input("Enter the number of table u want to print: "))
for i in range(1,11,1):
    print(f"{b} x {i} = {b*i}")