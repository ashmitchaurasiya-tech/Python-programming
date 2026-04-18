a=int(input("Enter the marks: "))
if a>=60 and a<=100:
    print("First division")
elif a>=45 and a<60:
    print("Second division")
elif a>=33 and a<45:
    print("Third division")
elif a<33:
    print("Fail")
else:
    print("Invalid")