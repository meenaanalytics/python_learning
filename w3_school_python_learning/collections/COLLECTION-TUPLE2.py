'''TUPLE'''

#thistuple = ("apple" , "cherry" , "mango", "orange")
#print(thistuple)

thistuple = ("apple")   # ✅ tuple
this_is_tuple = ("apple")   # ❌ not tuple

# print(thistuple)
# print(this_is_tuple)


'''tuple store multiple value'''

# tuple1 = ("apple" , "cherry" , "mango")
tuple2 = (1 , 8, 3, 7, 5, 6, 4 , 9)
tuple3 = (True , False , False)

# tuple1 = ("abc" , "34" , "True" , "40.977" , "male")


'''find the type'''

# mytuple = ("apple" , "cherry" , "mango", "orange")
# print(type(mytuple))

# my_tuple = tuple(("apple", "mango" , "cherry" , "guava"))
# my_tuple = ("apple" , "mango" , "cherry")

# print(tuple(my_tuple))
# print(my_tuple)

'''ACCESS TUPLE ITEM'''

# thistuple = ("apple" , "mango" , "cherry" , "kiwi" , "melon" , "orange" , "banana")

# print(thistuple[1:])
# print(thistuple[:1])
# print(thistuple[-4:-1])
# print(thistuple[1:4])
# print(thistuple[:4])
# print(thistuple[-1:-4])
# print(thistuple[-4:-3])
# print(thistuple[:-6])
# print(thistuple[2:])
# print(thistuple[1:5])
# print(thistuple[1:3])

# 
'''check if item exit'''

# if "water" in thistuple:
    # print("yes, 'apple' is in the fruits tuple")
# else:
    # print('no not in tuple')


'''update tuple'''

# x = ("apple" , "mango" , "cherry" , "kiwi" , "melon")
# x[0] = 'car'    # not allowed to change in tuple

# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)

'''add item in tuple'''

# thistuple = ("apple" , "mango" , "cherry" , "kiwi" , "melon")

# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)

# print(thistuple)


'''jion 2 tuple'''

# thistuple = ("mango" , "cherry" , "kiwi" , "melon")
# y = ("orange" ,)    # if not(,) in the end then its not equle to string
# thistuple += y      # or thistuple = thistuple + y

# print(thistuple)


'''remove itemt'''

# thistuple = ("cherry" , "kiwi" , "melon")
# y = list(thistuple)
# y.remove("kiwi")
# thistuple = tuple(y)

# print(thistuple)


'''delete tuple'''

thistuple = ("apple" , "mango" , "cherry" , "kiwi" , "melon")
del thistuple # tuple is deleted and its no longer available now onwards

print(thistuple)

'''unpack tuple item'''

# fruits = ("mango" , "cherry" , "kiwi" , "lichi")

# (x , y , *z) = fruits

# print(x)
# print(y)
# print(z)

# fruits = ("apple", "banana", "cherry", "strawerry", "raspberry")

# (x , y , *z) = fruits   #use (*) to store rest of the item🚨

# print(x)
# print(y)
# print(z)

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green , *tropic , red) = fruits

# print(green)
# print(tropic)
# print(red)

'''loop in tuple'''

# thistuple = ("mango", "cherry", "grapes", "guava")

# for v in thistuple:
    # print(v)

# thistuple = ("mango", "cherry", "grapes", "berry")

# for i in range(len(thistuple)):
#     print(thistuple[i])


# thistuple = ("cherry", "mango", "apple", "lichi")
# i = 0

# while i < len(thistuple):
#     print(thistuple[i])
#     i = i + 3


'''jion tuple'''

# tuple1 = ("a", "b", "c", "d")
# tuple2 = (1 , 2 , 3 , 4)

# tuple3 = tuple1 + tuple2
# print(tuple3)

'''multiple tuple'''

# fruits = ("apple", "mango", "cherry", "lichi")
# mytuple = fruits * 5

# print(mytuple)


'''tuple method'''

#count
fruits = ("mango", "cherry", "apple", "lichi", "apple")

# print(fruits.count('apple'))

#indexing
print(fruits.index('lichi'))
