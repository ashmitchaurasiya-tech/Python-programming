"""
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
"""
#while loop
a=1
while a<=5:# this loop will print number of lines in coloumn of pattern
    b=5
    while b>=1:#this loop will print number to print in a row of pattern
        print(b,end=" ")
        b-=1
    print()
    a+=1
print()
#for loop
for i in range(1,6,1):
    for j in range(5,0,-1):
        print(j,end=" ")
    print()