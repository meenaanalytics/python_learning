'''
Python Iterators
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
'''

'''
Iterator vs Iterable
Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

All these objects have a iter() method which is used to get an iterator:
'''

# student_name_list = ['Ram', 'Sham', 'Billu', 'Tiger', 'Goat', 'Cow', 'Sheep', 'Cat' , 'Chiriya']

# myIt = iter(student_name_list)

# print(next(myIt))
# print(next(myIt))
# print(next(myIt))
# print(next(myIt))
# print(next(myIt))
# print(next(myIt))
# print(next(myIt))

# for i in myIt:
#     print(i)



# mystr = "banana" #-> ['b','a', 'n',....]

# for x in mystr:
#   print(x)