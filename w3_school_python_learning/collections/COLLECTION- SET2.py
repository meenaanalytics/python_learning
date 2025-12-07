'''SET (Set items are unordered, unchangeable, and do not allow duplicate values.)'''

# myset = ["apple", "banana", "cherry", "mango"]
# myset = ("apple", "banana", "cherry", "mango")

# myset = {"apple", "banana", "cherry", "mango"}

# print(myset)

'''❌ no duplicate item'''

# thisset = {"apple", "mango", "cherry", "mango", "cherry"}

# print(thisset)

'''❌unchangeable'''

# thisset = {"apple", "mango", "cherry"}

# thisset[0] = "milk"

# print(thisset)


'''❌'''




# False and 0 is considered the same value:

# thisset = {"apple", "cherry", "mango",True , False, 0}

# print(thisset)


# thisset = {"apple", "cherry", "mango"}
# print(len(thisset))

# set1 = {"apple", "cherry", "mango"}
# set2 = {1, 4, 5, 6, 8}
# set3 = {True , False , False, True}

# set1 = {"abc", "male", 34 , True,40}

# print(type(set1))


# thisset = set(("apple", "cherry", "mango")) #note the double round-brackets
# print(thisset)


# thisset = {"apple", "cherry", "mango"}

# print("methi" in thisset)
# print("methi" not in thisset)


# thisset = {"apple", "cherry", "mango"}

# thisset.add("sugarcane")
# thisset.remove("apple")
# thisset.clear()

# print(thisset)


a = {"apple", "cherry", "mango", "orange"}
# b = {"pineapple", "kiwi", "papaya", "grapes"}

# a.update(b)

# print(a)


# thisset = {"pineapple", "kiwi", "papaya", "grapes"}
# mylist = ["cherry", "mango", "orange"]
# mytuple = (1 , 3 , 5 , 6)

# thisset.update(mytuple)
# thisset.update(mylist)

# print(thisset)


'''Join Sets

There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
'''

# set1 = {"a", "b", "c", "d"}
# set2 = {1, 2, 4, 5}

# set3 = set1.union(set2) #same as update
#or
# set3 = set1 | set2  # "|" means union  

# print(set3)


'''Union allows you to join multiple sets while update only allows 2'''


# set1 = {"a", "b", "c", "d"}
# set2 = {1, 2, 4, 5}
# set3 = {"vishal", "gugu"}
# set4 = {"cherry", "mango", "orange"}

# myset = set1.union(set2,set3, set4)
#OR
# myset = set1 | set2 | set3 | set4

# print(myset)


# set1 = {"cherry", "mango", "apple"}
# set2 = {"google", "microsoft", "apple", "cherry"}

# set3 = set1.intersection(set2)  # commom in 2 sets "apple", "cherry" in this case
#OR
# set3 = set1 & set2 
# print(set3)



# set1 = {"cherry", "mango", "apple"}😬
# set2 = {"google", "microsoft", "apple", "cherry"}

# set.intersection_update(set2)

# print(set1)


# set1 = {"apple",1, "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple",2 , True}

# set3 = set1.intersection(set2)

# print(set3)

# set2 = {"microsoft", "google", "apple"}
# set1 = {"apple", "banana", "cherry"}

# set3 = set2.difference(set1)

# print(set3)



# set2 = {"google", "microsoft", "apple"}
# set1 = {"apple", "banana", "cherry"}

# # set3 = set2.difference(set1)
# #or
# set3 = set1 - set2

# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.difference_update(set2)

# print(set1)



# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.symmetric_difference(set2)    #drop common and return all remaing item both set.

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

x = frozenset({"apple", "banana", "cherry"})
# x.add('Cheku')
# x.remove('apple')
# print(x)
print(type(x))






