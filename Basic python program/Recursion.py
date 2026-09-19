#Recursion:-
'''Recursion is a function which call itself.'''

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

n=int(input("Enter a number: "))
print(f"The factorial of given number is:{factorial(n)}")