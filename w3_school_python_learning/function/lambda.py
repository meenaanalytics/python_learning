'''
Python Lambda

Lambda Functions:
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.
'''

# lambda arguments : expression


# x = lambda a : a + 10
# print(x(5))


# def x(a):
#     return a + 10

# print(x(5))


'''multiple argument'''

# multiple2_number = lambda x,y : x * y

# print(multiple2_number(5,10))


# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))


'''
Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function 
inside another function.

Say you have a function definition that takes one argument, 
and that argument will be multiplied with an unknown number:

'''

# def myfunc(n):
#   return lambda a : a * n

# first_func = myfunc(5)
# print(first_func(10))

# def myfunc2(n):
#   def innerfunc(a):
#     return a * n
#   return innerfunc

# second_func = myfunc2(5)
# print(second_func(10))



'''The map() function applies a function to every item in an iterable:'''
# def doubleNumFunc(num):
#     return num * 2

# numbers = [1, 2, 3, 4, 5]
# double_num = list(map(lambda x: x * 2, numbers))
# double_num = list(map(doubleNumFunc, numbers))

# print(double_num)


'''The filter() function creates a list of items for which a function returns True:'''
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
# print(numbers)
# print(odd_numbers)



'''The sorted() function can use a lambda as a key for custom sorting:'''

# x = ("Ram", 25)
# print(x[1])

# students = [("Ram", 25), ("Sham", 2), ("Lucky", 12), ("Bruce", 18)]
# sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
# print(sorted_students)

# numbers = [10, 12, 30, 4, 45, 36, 17, 8]
# names = ['Ram', 'Sham' , 'Vishal' , 'Raghav' , 'Ajay', 'Vijay']
# print(sorted(names, reverse=True))
# print(sorted(numbers, reverse=True))




# words = ["apple", "pie", "banana", "cherry"]
# sorted_words = sorted(words, key=lambda x: len(x), reverse=True)
# print(sorted_words)

