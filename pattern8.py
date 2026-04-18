"""
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 
"""
#while loop
a=1
while a<=5:# this loop will print number of lines in coloumn of pattern
    b=1
    while b<=5:#this loop will print number of star to print in a row of pattern
        print(a,end=" ")
        b+=1
    print()
    a+=1
print()
#for loop
for i in range(1,6,1):
    for j in range(1,6,1):
        print(i,end=" ")
    print()