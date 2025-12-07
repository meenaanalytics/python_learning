'''
Python Decorators:

Decorators let you add extra behavior to a function, 
without changing the function's code.

A decorator is a function that takes another function as input and 
returns a new function.
'''

# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello Sally"

# @changecase
# def otherfunction():
#   return "I am speed!"

# print(myfunction())
# print(otherfunction())




# def changeCase(func):
#     function_called = func()
#     print(function_called.upper())


#     def sayHello():
#         return 'Hello world'
    
# changeCase(sayHello)   




# def changeCase(func):
#     def innerFunc(fname):
#         function_called = func (fname)
#         change_to_upper_case = function_called.upper()
#         return change_to_upper_case
#     return func('fname').upper()

#     return innerFunc

# @changeCase
# def sayHello(fname):
#     return f'Hello world {fname}'

# print(sayHello('gugu'))





def outerWrapper(x):
      def changeCase(func):
          def innerFunc(fname):
              function_called = func(fname)
              change_to_upper_case = function_called.upper()
              return change_to_upper_case
          return innerFunc  
      return changeCase

@outerWrapper('kaka')
def sayHello(fname):
    return f'Hello world {fname}'

print(sayHello('Guggu'))





# def changecase(func):
#     def myinner():
#         return func().upper()
#     return muinner


# def addgreeting(func):
#     def myinner():
#         return "Helo" + func() + "Have a good day!"
#     return myinner
    

# @changeCase
# @addgreeting
# def sayMyName():
#   return "Guggu Kaka"

# print(sayMyName())


'''
Preserving Function Metadata
Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes
'''

# def myfunction():
#     return "Have a great day!"


# print(myfunction_name_)
# #  print(myfunction._doc_)


# print(myfunction_name_)




# def changecase(func):
#     def myinner():
#         return func().upper()
#     return myinner

# @changeCase
# def myfunction():
#     return "have a great day!"

# print(myfunction._name_)





#import functools


# def changecase(func):
#     @functools.wraps(func)
#     def myinner():
#         return func().upper()
#     return myinner

# @changecase 
# def myfunction():
#     return "have a great day!"

# print(myfunction._name_)