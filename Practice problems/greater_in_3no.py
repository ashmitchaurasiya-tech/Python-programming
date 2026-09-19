a,b,c=map(int,input("Enter the numbers").split())
if b>a>c or b>c>a:
    print("greater= ",b)
elif a>b>c or a>c>b:
    print("greater= ",a)
elif c>a>b or c>b>a:
    print("greater= ",c)
else:
    print("They are equal")