'''list'''

#Lists are used to store multiple items in a single variable.

#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

#List items are ordered, changeable, and allow duplicate values.

# ordered = indexing i.e 0 ,1 ,2 ,3, 4 .....

# mylist = ["apple", "banana", "cherry", 100, 1.2, ['a', ()]]
# mylist = ["apple", "banana", "cherry"]

# mylist[1] = 'cherry'
# mylist = []

# print(len(mylist)) # len() always start count from 1 not 0

# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]

# list1 = ["abc", 34, True, 40, "male"]

# list2 = list(["abc", 34, True, 40, "male"])

# print(type(list2))
# print(list2)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# print(thislist[2]) #access the list item using Index 
# print(thislist[-4]) # start from the last and so on...

# print(thislist[1:4])
# print(thislist[:4])

# print(thislist[2:])

# thislist = ["apple", "banana", "cherry"]

# if "Mango" in thislist:
#   print("Yes, 'apple' is in the fruits list")
# else:
#   print('Not in list!!!')


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# thislist[1:3] = ["blackcurrant"]

# thislist[1] = 'blackcurrant'
# thislist[2] = 'watermelon'

# thislist.insert(2, 'Iphone') #insert item to specific Index and push rest of the item

# thislist.append("Macbook") #insert at the last 

# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# tropical = ("mango", "pineapple", "papaya")

# thislist.extend(tropical) # extend the array (list )

# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("cherry") # remove any item with item name
# thislist.pop(1) # remove from specific index
# thislist.pop() # if you not pass anything it remove last item

# del thislist[0]  # delete the specific index 

# thislist.clear() # delete every item in list and return empty : []

# print(thislist)

fruits = ["apple", "banana", "cherry", "mango"]

# normal loop
# for fruit in fruits:
#   print(fruit)

# index loop

# length_of_fruits = len(fruits)

# print(length_of_fruits)

# print(fruits[0])
# print(fruits[1])
# print(fruits[2])

# for i in range(length_of_fruits):
#     print(fruits[i])


'''home work'''
# play with Indexes including negative(-) index and positive (+)

