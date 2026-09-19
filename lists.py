#LIST MANIPULATION:-
'''A list is an ordered collection of values'''
#Creating Lists:-
list1=list(input("Enter elements in list"))
print(list1)
s='hello'
t=list(s)
print(t)
'''Creating a list of five integers'''#IMPORTANT
list_of_elements=[]
print("Enter list of five elements")
for i in range (5):
    print("Enter integer",i)

    userinput=int(input()) 
    list_of_elements.append(userinput)
print("The list is:",list_of_elements)

#Lists are Mutable:-
num=[17,12,18]
num[1]=5
print(num)
List=[1,2,3,4,5,6]
print(List)
List[2]=10;
print(List)
List[1]='anything'
print(List)

#Indexing in list:-
x=["apple","banana","peer"]
print(x[0])
print(x[1])
print(x[-1])
print(x[-2])
ch=['l','o','w','e','r']
print(ch[0])
print(ch[4])
print(ch[-2])
print(ch[-5])

#Slicing in list:-
numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers[3:6])
print(numbers[0:1])
print(numbers[7:10])
print(numbers[0:10:1])
print(numbers[0:10:2])
print(numbers[3:6:3])
print(numbers[::4])
print(numbers[8:3:-1])
print(numbers[10:0:-2])
print(numbers[5::-2])
listx=[1,2,3,4,5]
listy=listx[2:5]
print(listy)

#Traversing in lists:_
for Rainbow in ['Red','Orange','Yellow','Green','Blue','Indigo','Violet']:
    print("I like",Rainbow)

name_list=["Aman","Beena","Deepak"]
for x in name_list:
    print("Hello",x)

numbers=[1,2,3,4,5,6,7,8,9,10]
i=0
while i<10:
    print(numbers[i],end=" ")
    i=i+1

numbers=[1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    print(i,end=" ")

numbers=[1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(numbers):
     print(numbers[i],end=" ")
     i=i+1

numbers=[1,2,3,4,5,6,7,8,9,10]
i=0
while i <len(numbers):
    print(numbers[i],end=" ")
    i=i+2

ch=['l','o','w','e','r']
length=len(ch)
for i in range(length):
    print(i,(i-length))

'''Program to find the sum of the elements ona lists'''
a=[10,20,30,40]
s=0
i=0
while (i<len(a)):
    s=s+a[i]
    i=i+1
print("sum:",s)

'''Program to display total and average value of elements in the list'''
list=[93,79,73,65,59]
total=0
i=0
while i<len(list):
    total=total+list[i]
    i=i+1
average=total/len(list)
print("Total:",total)

#List operators:-
 #1.Joining lists
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)
#2.Repeating lists
a=[0]*4
print(a)
#3.Slicing lists
t=['a','b','c','d','e','f']
print(t[1:3])
print(t[:4])
print(t[3:])

#LIST FUNCTIONS AND METHODS:-

#1.len()
lst=['a','b','c','d']
print(len(lst))
q=[2,3]
p=[1,q,4]
print(len(p))
#2.count()
basket=['apple','banana','orange','apple']
print(basket.count('apple'))
a_list=[47,"47",47,4747]
print(a_list.count(47))
#3.append()
basket=['apple','banana','orange']
basket.append('apple')
print(basket)
#4.extend()
x=['apple','banana','orange']
y=['pear','mango']
x.extend(y)
print(x)
#5.insert()
num=[1,2,3,5,6,7]
num.insert(3,4)
num.insert(3,'four')
print(num)
#6.pop()
a=["red","blue","green"]
print(a)
a.pop()
print(a)
a.pop(1)
print(a)
#7.remove()
x=["to","be","or","not","to","be"]
x.remove("be")
print(x)
#8.del.statement
x=["to","be","or","not","to","be"]
del x[2]
print(x)
#9.reverse()
x=[1,2,3]
x.reverse()
print(x)
#10.sort()
x=[4,6,2,8,1,9,0,7,3,5]
x.sort()
print(x)
#11.clear()
x=[4,6,2,8,1,9,0,7,3,5]
x.clear()
print(x)
#12.max() & min()
x=[4,6,2,8,1,9,0,7,3,5]
print(max(x))
print(min(x))