"""
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 
"""
#while loop
a=5
while a>=1:# this loop will print number of lines in coloumn of pattern
    b=1
    while b<=a:#this loop will print number of star to print in a row of pattern
        print(a,end=" ")
        b+=1
    print()
    a-=1
print()
#for loop
for i in range(5,0,-1):
    for j in range(1,i+1,1):
        print(i,end=" ")
    print()