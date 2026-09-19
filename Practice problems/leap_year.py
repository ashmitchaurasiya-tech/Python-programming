a=int(input("Enter the year: "))
if a%4==0 and a%100==0:
    print(f"It is a leap year{a}")
else:
    print(f"It is a not leap year{a}")
