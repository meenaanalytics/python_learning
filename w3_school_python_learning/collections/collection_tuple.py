'''Tuple'''

# thistuple = ("apple", "banana", "cherry")

# print(len(thistuple))

# thisIsTuple = ('apple',)  ✅ tuple

# this_is_tuple = ('apple')   ❌ not tuple

# print(type(thisIsTuple))
# print(type(this_is_tuple))

'''tuple store multiple value'''
# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)

# tuple1 = ("abc", 34, True, 40.977, "male")

'''find the type'''

# mytuple = ("apple", "banana", "cherry")

# print(type(mytuple))

# my_tuple = tuple(('apple', 'banana', 'Guava'))
# my_tuple = ('apple', 'banana', 'Guava')

# print(my_tuple)

'''Access tuple item'''

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# print(thistuple[:1])
# print(thistuple[-1])
# print(thistuple[1:4]) # Range of Indexes [1:4] 🚨
# print(thistuple[:4])
# print(thistuple[2:])
# print(thistuple[-4:-1])

'''check if Item exist'''

# if "water" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")
# else:
#   print('no not in tuple')

'''Update Tuple'''

# x = ("apple", "banana", "cherry")

# x[0] = 'Car' # not allowed to change in tuple 🚨

# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)

'''add item in tuple '''

# thistuple = ("apple", "banana", "cherry")

# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)

# print(thistuple)

'''join 2 tuple'''

# thistuple = ("apple", "banana", "cherry")

# y = ("orange",) #if not , in end then its equal to string

# thistuple += y # or thistuple = thistuple + y

# print(thistuple)

'''Remove item'''

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)

# print(thistuple)

'''delete tuple'''

# thistuple = ("apple", "banana", "cherry")
# del thistuple

# print(thistuple) 

'''Unpack Tuple item'''

# fruits = ("apple", "banana", "cherry")

# (x, y, z) = fruits

# print(x)
# print(y)
# print(z)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (x, y, *z) = fruits # use * to store rest of the item🚨

# print(x)
# print(y)
# print(z)

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)


'''Loop in tuple'''

# thistuple = ("apple", "banana", "cherry")

# for x in thistuple:
#   print(x)

# thistuple = ("apple", "banana", "cherry")

# for i in range(len(thistuple)):
#   print(thistuple[i])

# thistuple = ("apple", "banana", "cherry")
# i = 0

# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1

'''Join Tuple'''

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)

'''Multiple Tuple'''

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 3

# print(mytuple)

'''tuple methods'''

#count 
fruits = ( "banana", "cherry", "apple")

# print(fruits.count('apple'))

#index
print(fruits.index('apple'))