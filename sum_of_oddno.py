#while loop
a=1
s=0
while a<=20:
    s+=a
    a+=2
print(f"Sum of odd numbers from 1 to 20:{s}")

#for loop
s=0
for i in range(1,21,2):
    s+=i
print(f"Sum of odd numbers from 1 to 20:{s}")
