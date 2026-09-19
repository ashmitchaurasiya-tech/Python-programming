#SETS:-
"""A set is an unordered collection of unique elements.
Unlike lists or tuples, sets do not allow duplicate values.
each element in a set must be unique. Sets are mutable"""

my_set = {1, 2, 2, 3, 3, 4, 5, 5} 
print (my_set)

#Set Operations:-

#1.Union
'''It combine elements from both sets using the union() function or the | operator.'''
set1={1,2,3,4,5}
set2={6,7,8,9}
set3=set1|set2
print(set3)
print(set1.union(set2)) 

#Intersection
'''It is used to get common elements using the intersection() function or the & operator.'''
set1={1,7,8,4,5}
set2={6,7,8,9}
set3=set1&set2
print(set3)

#Difference
'''It is used to get elements that are in one set but not the other using the difference() function or the - operator.'''
set1={1,6,8,4,5}
set2={6,7,8,9}
set3=set1-set2
print(set3)

#Symmetric Difference
''' It is used to get elements that are in either of the sets but not in both using the symmetric_difference() method or the ^ operator.'''
set1={1,6,8,4,5}
set2={6,7,8,9}
set3=set1^set2
print(set3)

# Defining a set
langs = {"C", "C++", "Java", "Python"}

# Accessing set items using a for loop
for lang in langs:
   print (lang)

# Adding elements in set:-

# Adding elements to the set using add() method
language = set()    #empty set
language.add("C")
language.add("C++")
language.add("Java")
language.add("Python")
print("Updated Set:", language)
# Adding element to the set using update()
my_set = {1, 2, 3}
my_set.update([4])
print("Updated Set:", my_set)

#Removing elements from the set:-

#Removing elements from the set using remove()
my_set = {"Rohan", "Physics", 21, 69.75}
my_set.remove("Physics")
print ("Set after removing: ", my_set)
#Removing elements from the set using discard()
my_set = {"Rohan", "Physics", 21, 69.75}
my_set.discard("Physics")
print ("Set after removing: ", my_set)
#Removing elements from the set using pop()
my_set = {"Rohan", "Physics", 21, 69.75}
my_set.pop()
print ("Set after removing: ", my_set)
# Removing all elements from the set using clear()
my_set = {"Rohan", "Physics", 21, 69.75}
my_set.clear()
print("Updated Set:", my_set)