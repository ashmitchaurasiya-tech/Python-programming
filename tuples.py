#TUPLES:-
'''Elements can be written with or without parentheses and mixed data types'''
#DIFFERENCE BETWEEN LISTS AND TUPLES:-
'''Tuples are immutable'''
 #Creating  tuples:-
tuple1=(0,1,2,3)
tuple2=('Hello','Python')
tuple3=(tuple1,tuple2)
print(tuple3)
weekdays=("Mon","Tue","Wed","Thur","Fri")
weekends="Sat","Sun"
print(weekdays)
print(weekends)
#Accessing elements in tuples:-
tup1=("Mona","Monty",1997,2003)
print(tup1[0])
print(tup1[-1])
print(tup1[2])
print(tup1[3])
#Accessing nested tuples items:-
Tuple=((1,2,3),[4,5,6],"Hello")
print(Tuple[0][0])
print(Tuple[1][0])
print(Tuple[2][0])
print(Tuple[2][4])
#Tuple slices:-
values=(1,3,5,7,9,11,13)
print(values[1:])
print(values[:1])
print(values[2:4])

#TUPLE FUNCTIONS:-
#1.count()
a=(1,2,2,3,4,5,5,5)
print(a.count(2))
print(a.count(5))
#2.len()
tup1=(11,22,33)
print(len(tup1))
#3.max() and min()
friends=("sanjay","morris","ajay","suman")
print(max(friends))
print(min(friends))
their_earning=(1000,5000,2000,100000000)
print(max(their_earning))
print(min(their_earning))
#4.sorted()
a=(4,6,3,1,7,9,2,8,5)
print(sorted(a))
#5.tuple()
'''creating a tuple from a string'''
t=tuple("xyz")
print(t)
'''creating tuple from list'''
t=tuple([2,4,6])
print(t)
'''creating tuple from dictionary'''
t=tuple({1:"1",2:"2"})
print(t)
#6.index()
tup=(1,3,4,7,32)
print(tup.index(4))
print(tup.index(32))
#7.sum()
tup=(2,6,7,7,2,1)
print(sum(tup))

#Tuple addition:-
x=(1,2,3,4)
y=(5,6,7,8)
z=x+y
print(z)
#Tuple multiplication:-
x=(1,2,3,4)
z=x*2
print(z)
#Deleting a tuple:-
x=(1,2,3,4,5,6,7)
del x
#unpacking tuples:-
percentages=(99,95,89,90)
a,b,c,d=percentages
print(b)
print(d)
fruitlist=("apple","banana","mango","grapes")
app,man,ban,gra=fruitlist
print(app)
print(man)
print(ban)
print(gra)