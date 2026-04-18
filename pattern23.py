"""
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
"""
#while loop
a=1
while a<=5:#to control line 1 to 5
    b=5
    while b>=a:#to print number of spaces
        print(" ",end=" ")
        b-=1
    c=1
    while c<=a:#to print number of stars
        print("*",end=" ")
        c+=1
    print()
    a+=1
print()
#for loop
for i in range(1,6,1):
    for j in range(5,i,-1):
        print(" ",end=" ")
    for k in range(1,i+1,1):
        print("*",end=" ")
    print()