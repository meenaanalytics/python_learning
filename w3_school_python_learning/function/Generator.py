'''
Generators
Generators are functions that can pause and resume their execution.

When a generator function is called, it returns a generator object, which is an iterator.

The code inside the function is not executed yet, it is only compiled. The function only executes when you iterate over the generator.
'''

# def my_generator():
#   yield 'Good morning'
#   yield 'Good afternoon'
#   yield 'Good night'


# return_val = my_generator()
# print(return_val)
# print(next(return_val))
# print(next(return_val))
# print(next(return_val))


# for value in my_generator():
#   print(value)


# def fill_form():
#   yield "Enter name"
#   yield "Enter age"
#   yield "Enter address"

# form_field = fill_form()
# print(next(form_field))
# print(next(form_field))
# print(next(form_field))
# print(next(form_field))

