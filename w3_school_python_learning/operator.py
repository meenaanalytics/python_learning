'''Python Operators''' #(+, -, *,/ ,%, //, (),<, >, >=, <= , ==)

# Operators are used to perform operations on variables and values. 🚀

# math_operation = 5 + 10 + 10.15 / 2 - 10

# print(math_operation) # 5 (number(int)),  '+' operator ,  10 (number(int))

'''Arithmetic Operators'''  #(+, -, *, / ,% , ** , //)

#Arithmetic operators are used with numeric values to perform common mathematical operations:


# x = 15
# y = 4

# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x % y) 
# print(x ** y) # square ex: 2 sq 2 = 4 
# print(x // y) # remainder

# x = 10


'''assignment operator''' #operation + assign value
# x = x + 10
# or
# x += 10

# (home work)
# =
# +=
# -=
# *=
# /=
# **=
# //=
# %=

# print(x)

'''Comparison Operators'''

#Comparison operators are used to compare two values:

# x = 5
# y = 3

# print(x == y)
# print(x != y)
# print(x > y)
# print(x < y)
# print(x >= y)
# print(x <= y)

'''Chaining Comparison Operators'''

# x = 5

# print(1 < x < 10) #True

# print(1 < x and x < 10 and x < 100)
# print(not(1 < x and x < 10 and x < 100))
# print(1 < x or x > 10)

'''Logical Operators'''

# and Returns True if both statements are true	                  x < 5 and  x < 10	
# or	Returns True if one of the statements is true	          x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	  not(x < 5 and x < 10)


'''Identity Operators'''

# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is 	    Returns True if both variables are the same object	     x is y	
# is not	Returns True if both variables are not the same object	 x is not y

# x = {}
# y = x

# print( x is y )
# print( x is not y )

'''Membership Operators'''

# in 	     Returns True if a sequence with the specified value is present in the object	    x in y	
# not in	 Returns True if a sequence with the specified value is not present in the object	x not in y

# fruits = ["apple", "banana", "cherry"]

# print("banana" in  fruits)

# print("pineapple" not in fruits)
