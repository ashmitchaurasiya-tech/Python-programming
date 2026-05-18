#Strings:-
'''A string value is a collection of characters put in single,double and triple quotes.
With the triple quotes you extend the string to the multipe line'''

#Accessing string indexing in python:-
str="python"
print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])
print(str[5])
print(str[-1])
print(str[-2])
print(str[-3])
print(str[-4])
print(str[-5])
print(str[-6])

#Strings are immutable:-
'''Means that the contents of the variable are cannot be changed after it is created'''

#Modifying of strings or Updating of string:-
'''You can create a string that is a variation of original'''
Greeting='Hello,world!'
print(Greeting)
new_greeting='J'+Greeting[1:]
print(new_greeting)

#Traversing a string:-
'''using for loop'''
str="PYTHON"
for i in str:
    print(i)

'''using while loop'''
str="PYTHON"
i=0
while i<len(str):
    print(str[i])
    i=i+1

#program to find the length of the entered string
while True:
    str=input("")
    if str=='quit':
        break
    print(len(str))
print('done')

#program to check lenth of a string with a suitable message
while True:
     str=input("")
     if str=='quit':
         break
     if len(str)<3:
        print('Too small')
        continue
     print(" input is of sufficient length")

#String Formatting:-
'''First Format'''
num1=int(input("Enter first num"))
num2=int(input("Enter second num"))
product=num1*num2
print('The product of ',num1,'and',num2,'is',product)

'''Second Format'''
num1=int(input("Enter first num"))
num2=int(input("Enter second num"))
product=num1*num2
print('The product of {num1} and {num2} is {product}')

'''Default order'''
str1="{} {} {}".format('Work','Is','Worship')
print(str1)

'''Positional Format'''
str1="{1} {0} {2}".format('Work','Is','Worship')
print(str1)

'''Keyword Format'''
str1="{l} {f} {g}".format(g='Work',f='Is',l='Worship')
print(str1)

#SPECIAL STRING OPERATORS:-

#Concatenation (+) Operator
str1="Hello"
str2="World"
print ("String 1:",str1)
print ("String 2:",str2)
str3=str1+str2
print("String 3:",str3)

#Replication (*) Operator
str1="Hello"
str2="World"
print ("String 1:",str1)
print ("String 2:",str2)
str3=str1+str2*3
print("String 3:",str3)
str4=(str1+str2)*3
print ("String 4:", str4)

#Membership Operator(in and not in)
str="Work hard"
'W' in str
'W' not in str

#STRING SLICES:-
'''Slicing on a string'''
my_str="PORTION"
print(my_str[1:3])
print(my_str[2:])
print(my_str[1:-1])
print(my_str[:-1])
print(my_str[-7 :-1])
print(my_str[-5:-3])
print(my_str[:])
print(my_str[:2])

#String FUNCTIONS:-

#1.len()
fruit="Apple"
print(len(fruit))
#2.count()
s1="Sashi Singh"
print(s1.count("S"))
#3.capitalize()
str="this is string"
print(str.capitalize())

#5.isalnum()
str1="Work Hard"
print(str1.isalnum())
str2="Work"
print(str2.isalnum())
str3="Work1"
print(str3.isalnum())
str4="1234"
print(str4.isalnum())
#6.isalpha()
str2="Work"
print(str2.isalpha())
str3="Work1"
print(str3.isalpha())
str4="1234"
print(str4.isalpha())
#7.isdigit()
str2="Work"
print(str2.isdigit())
str3="Work1"
print(str3.isdigit())
str4="1234"
print(str4.isdogit())
#8.lower()
s1="Save Water"
print(s1.lower())
#9.islower()
str1="Work Hard"
print(str1.islower())
str2="hello"
print(str2.islower())
str3="ROHAN"
print(str3.islower())
#10.isupper()
str1="Work Hard"
print(str1.isupper())
str2="hello"
print(str2.isupper())
str3="ROHAN"
print(str3.isupper())
#11.upper?()
s1="Save Water"
print(s1.upper())
#12.lstrip()
s1="Save Water"
print(s1.lstrip())
str="ABC international"
print(str.lstrip("A"))
print(str.lstrip("n"))
#13.rstrip()
str2="Hello World"
print(str2.rstrip())
str3="Television"
print(str3.rstrip("vision"))
#14.isspace()
print(" ".isspace())
#15.istitle()
str1="This Is A Title"
str2="This is A title"
print(str1.istitle())
print(str2.istitle())
#16.replace(old,new)
str="This is just a simple string"
print(str.replace("simple","short"))
str1="This is a test"
print(str1.replace("is","eez"))
#17.split()
s1="Work is Worship"
words=s1.split()
print(words)
#18.join()
str1=('Raja','Ram','Mohan','Rai')
str=' '
print(str.join(str1))
#19.swapcase()
str='COMPUTER'
print(str.swapcase())
str1='computer'
print(str.swapcase())
#partition()
str-"The Golden Star"
print(str.partition())
print(str.partition('ne'))
print(str.partition('e'))
#20.str()
print(str(17)) 