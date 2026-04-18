"""
5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5 
"""
#while loop
a=1
while a<=5:# this loop will print number of lines in coloumn of pattern
    b=5
    while b>=a:#this loop will print number of star to print in a row of pattern
        print(b,end=" ")
        b-=1
    print()
    a+=1
print()
#for loop
for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()