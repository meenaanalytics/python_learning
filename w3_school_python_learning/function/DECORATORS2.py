'''
Python Decorators:

Decorators let you add extra behavior to a function, 
without changing the function's code.

A decorator is a function that takes another function as input and 
returns a new function.
'''

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())


