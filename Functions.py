#Function
'''
Function is a group of statement performing a special task.
'''
#program to greet the user using function:-
def func():
    print("Good Day")
    
func()

#Function with variable

def func(name):
    print("Good day!"+name)

func("Ashmit")

#Function with argument:-

def func(name):
    print("Good day!" + name)
    return None

a=func("Ashmit")
print(a)

'''
return:-
return is the function that ki ek value lekr jao function se or jo bhi variable mange use dedo.
'''

#Default parameter Value:-
'''We can have a value as a default argument in a function.'''

def func(name="Stranger"):
    print("Hello" + name)
    
func()
func("Ashmit")

#types of functions:-
"""
1. built-in function= Already present in python like print(),len()etc.

2.pre-defined function= Defined by user using the def function.

"""