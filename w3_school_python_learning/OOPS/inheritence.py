
'''Python Inheritance

Inheritance allows us to define a class that inherits all the methods 
and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.

'''


'''Use the super() Function
Python also has a super() function that will make the child class inherit all the methods 
and properties from its parent:

By using the super() function, you do not have to use the name of the parent element, 
it will automatically inherit the methods 
and properties from its parent.

'''




class GrandParent:
  def __init__(self, fname, lname): #method
    super().__init__()
    self.firstname = fname #properties
    self.lastname = lname #properties
    self.land = 'Delhi'

  def printname(self): #method
    print(self.firstname, self.lastname)


class Parent:
  def __init__(self, fname, lname): #method
    super().__init__(fname, lname)
    self.firstname = fname #properties
    self.lastname = lname #properties
    self.medal = 'Gold'

  def printname(self): #method
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()


# class Child(Parent):
#   def __init__(self, fname, lname):
#     pass
#   pass
  
# Child1 = Child('Guggu','Don') # Child1 = Object
# # print(Child1.firstname)
# Child1.printname()


# class Child(Parent):
#   def __init__(self, fname, lname):
#     Parent.__init__(self, fname, lname)
#     GrandParent.__init__(self, fname, lname)
#     self.specialist = 'Heart'
#     # pass
#   pass
  

# Child1 = Child('Guggu','Don') # Child1 = Object
# # print(Child1.firstname)
# Child1.printname()
# print(Child1.specialist)
# print(Child1.medal)
# print(Child1.land)



# by using super 

class Child(Parent, GrandParent):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.specialist = 'Heart'
    # pass
  pass
  
Child1 = Child('Guggu','Don') # Child1 = Object
# print(Child1.firstname)
Child1.printname()
print(Child1.specialist)
print(Child1.medal)
print(Child1.land)











