# fruits = ["apple", "banana", "cherry", "Guava", "Berry", 'Mango', 'Orange']

'''iterate through while loop'''
# i = 0

# while i < len(fruits):
#   print(fruits[i])
#   i += 1  # or i = i + 1 


'''List comprehension'''

# for fruit in fruits:
#     print(fruit)

# [print(fruit) for fruit in fruits]

# new_fruit_bucket = [] #2        1                   3
# new_fruit_bucket = [fruit for fruit in fruits if "a" in fruit]
# new_fruit_bucket = [x for x in fruits if x != "apple"]
# new_fruit_bucket = [x for x in range(10)]
# new_fruit_bucket = [x for x in range(10) if x < 5]
# new_fruit_bucket = [x.upper() for x in fruits]
# new_fruit_bucket = ['hello' for x in fruits]
# new_fruit_bucket = [x if x != "banana" else "orange" for x in fruits]

# for fruit in fruits:
#     if 'a' in fruit:
#         new_fruit_bucket.append(fruit)

# print(new_fruit_bucket)


'''Sorting'''

# fruits = ["Apple", "banana", "Cherry", "Guava", "Berry", 'Mango', 'Orange', 'Avogado']

# fruits.sort()
# fruits.sort(reverse=True)

# print(fruits)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# thislist.sort(reverse=True)
# print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key= str.lower)

# thislist.reverse()

# thislist2 = thislist

# thislist2[0] = 'Vishal'

# thislist2 = thislist.copy()
# thislist2[0] = 'Vishal'


# thislist2 = list(thislist)
# thislist2[0] = 'Vishal'

# thislist2 = thislist[:] # this only return the COpy not the original one
# thislist2[0] = 'Vishal'

# print(thislist)

'''Join List'''

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

# list3 = list1 + list2 

# for x in list2:
#     list1.append(x)

# list1.extend(list2)

print(list1)