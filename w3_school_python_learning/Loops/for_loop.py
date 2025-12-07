'''
Python For Loops:
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
'''

# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#   print(fruit)

# my_name = 'Vishal'

# my_name = ['V', 'i', 's', 'h', 'a', 'l']

# for x in my_name:
#   print(x)

# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#   print(fruit)
#   if fruit == "banana":
#     break

# fruits = ["apple", "banana", "cherry"]

# for x in fruits:
#   if x == "banana":
#     break
#   print(x)


# fruits = ["apple", "banana", "cherry"]

# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)


'''
The range() Function
To loop through a set of code a specified number of times, we can use the range() function,

The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
'''


# for x in range(2, 10, 4): # range(2, 10, 4)
#   print(x)                # range(starting , ending, steps to skip)


# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")


# for x in range(6):
#   if x == 3: break
#   print(x)
# else:
#   print("Finally finished!")

# colors = ["red", "white", "grey"]
# fruits = ["apple", "banana", "cherry"]
# cars   = ['Tata', 'Maruti', 'Ford']

# for color in colors: # color = red 
#   for fruit in fruits: #fruit = apple
#     for car in cars:
#       print(f"Color: {color}, Fruit: {fruit}, Car: {car} ")

'''
The pass Statement
for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
'''

# for x in [0, 1, 2]:
#   pass


