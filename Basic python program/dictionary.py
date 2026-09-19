#Dictionary:-
"""A dictionary is a unordered collection of data type stored data in a key and value pair and are mutable"""

"""Each key in a dictionary must be unique. If you try to assign a value to an existing key,
   the old value will be replaced by the new value."""

d1 = {"Fruit":["Mango","Banana"], "Flower":["Rose", "Lotus"]}
d2 = {('India, USA'):'Countries', ('New Delhi', 'New York'):'Capitals'}
print (d1)
print (d2)

'''Python doesn't accept mutable objects such as list as key, and raises TypeError.'''
#     d1 = {["Mango","Banana"]:"Fruit", "Flower":["Rose", "Lotus"]}

#dictionary methods and functions:-
a = {
   "Name": "Sachin Tendulkar",
   "Age": 48,
   "Sport": "Cricket"
}

#1.items()
print(a.items())
#2.value()
print(a.values())
#3.keys()
print(a.keys())
#4.update()
a.update({"Sports":"Football"})
print(a)
#5.get()
print(a.get("Name"))







