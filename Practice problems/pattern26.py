"""
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
"""
#while loop
a=5
while a>=1:
    b=5
    while b>a:
        print(" ",end=" ")
        b-=1
    c=1
    while c<=a:
        print("*",end=" ")
        c+=1
    print()
    a-=1
print()
#for loop
for i in range(5,0,-1):
    for j in range(5,i,-1):
        print(" ",end=" ")
    for k in range(1,i+1,1):
        print("*",end=" ")
    print()