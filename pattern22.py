"""
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
"""
#while loop
a=1
while a<=5:
    b=5
    while b>a:
        print(end=" ")
        b-=1
    c=1
    while c<=a:
        print("*",end=" ")
        c+=1
    print()
    a+=1
#for loop
for i in range(1,6,1):
    for j in range(5,i,-1):
        print(end=" ")
    for k in range(1,i+1,1):
        print("*",end=" ")
    print()