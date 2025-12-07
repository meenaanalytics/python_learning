'''SET (Set items are unordered, unchangeable, and do not allow duplicate values.)'''

# myset = ["apple", "banana", "cherry"]
# myset = ("apple", "banana", "cherry")

# myset = {"apple", "banana", "cherry"}

# print(myset)

'''❌ No duplicate Items'''

# thisset = {"apple", "banana", "cherry", "apple", 'banana'}

# print(thisset)

'''❌ unchangeable'''

# thisset = {"apple", "banana", "cherry"}

# thisset[0] = 'Milk'

# print(thisset)


'''❌ '''
# False and 0 is considered the same value:

# thisset = {"apple", "banana", "cherry", False, True, 0}

# print(thisset)

# thisset = {"apple", "banana", "cherry"}

# print(len(thisset))

# set1 = {"apple", "banana", "cherry"}
# set2 = {1, 5, 7, 9, 3}
# set3 = {True, False, False}

# set1 = {"abc", 34, True, 40, "male"}

# print(type(set1))

# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)

# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)

# thisset = {"apple", "banana", "cherry"}

# print("Methi" in thisset)
# print("Methi" not in thisset)

# thisset = {"apple", "banana", "cherry"}

# thisset.add('SugarCane')
# thisset.remove('apple')
# thisset.clear()

# print(thisset)

# a = {"apple", "banana", "cherry"}
# b = {"pineapple", "mango", "papaya"}

# a.update(b)

# print(a)

# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
# mytuple = (1, 2, 3)

# thisset.update(mytuple)

# print(thisset)


'''
Join Sets

There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
'''

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}

# set3 = set1.union(set2) #same as update
# or
# set3 = set1 | set2 # '|' means union 
# print(set3)


'''Union allows you to join multiple sets while update only allows 2'''

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# myset = set1.union(set2, set3, set4) 
#or
# myset = set1 | set2 | set3 |set4
# print(myset)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple", "cherry"}

# set3 = set1.intersection(set2) # common in 2 sets "apple", "cherry" in this case
# or
# set3 = set1 & set2
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple", "cherry"}

# set1.intersection_update(set2)

# print(set1)


# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}

# set3 = set1.intersection(set2)

# print(set3)


# set2 = {"google", "microsoft", "apple"}
# set1 = {"apple", "banana", "cherry"}

# set3 = set2.difference(set1)
# or
# set3 = set1 - set2

# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.difference_update(set2)

# print(set1)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.symmetric_difference(set2) #drop common and return all remaining item from both set

# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 ^ set2 #  set3 = set1.symmetric_difference(set2) both works same
# print(set3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.symmetric_difference_update(set2)

# print(set1)


'''Frozen set (immutable)'''

# x = frozenset({"apple", "banana", "cherry"})
# x.add('Cheku')
# x.remove('apple')
# print(x)
# print(type(x))

