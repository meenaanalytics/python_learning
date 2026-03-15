# # class Car:
# #   def __init__(self, brand, model):
# #     self.brand = brand
# #     self.model = model

# #   def move(self):
# #     print("Drive!")

# # class Boat:
# #   def __init__(self, brand, model):
# #     self.brand = brand
# #     self.model = model

# #   def move(self):
# #     print("Sail!")

# # class Plane:
# #   def __init__(self, brand, model):
# #     self.brand = brand
# #     self.model = model

# #   def move(self):
# #     print("Fly!")

# # car1 = Car("Ford", "Mustang")       #Create a Car object
# # boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# # plane1 = Plane("Boeing", "747")     #Create a Plane object

# # for x in (car1, boat1, plane1):
# #   x.move()





# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Move!")

# class Car(Vehicle):
#   pass

# class Boat(Vehicle):
#   def move(self):
#     print("Sail!")

# class Plane(Vehicle):
#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object

# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   x.move()
#   print('-----------')



'''Encapsulation'''


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.__age = age # Private property

#   def tellMyAge(self):
#     print(self.__age)

# p1 = Person("Emil", 25)
# # print(p1.name)
# print(p1.__age) # This will cause an error
# p1.tellMyAge()




# class Person:
#   def __init__(self, name, salary, age):
#     self.name = name
#     self.__salary = salary
#     self.__age = age  # __PERSON__AGE__ = 25

#   def get_age(self):
#     return self.__age

#   def set_age(self, age):
#     if age > 0:
#       self.__age = age
#     else:
#       print("Age must be positive")

# p1 = Person("Tobias", 30000, 25)
# p1.set_age(50)
# p1.__age = 45
# # print(p1._Person__age)
# print(p1.__dict__)



# class Student:
#   def __init__(self, name):
#     self.name = name
#     self.__grade = 0

#   def set_grade(self, grade):
#     if 0 <= grade <= 100:
#       self.__grade = grade
#     else:
#       print("Grade must be between 0 and 100")

#   def get_grade(self):
#     return self.__grade

#   def get_status(self):
#     if self.__grade >= 60:
#       return "Passed"
#     else:
#       return "Failed"

# student = Student("Emil")
# student.set_grade(85)
# print(student.get_grade())
# print(student.get_status())
# print(student.__dict__)




# class Calculator:
#   def __init__(self):
#     self.result = 0

#   def __validate(self, num):
#     if not isinstance(num, (int, float)):
#       return False
#     return True

#   def add(self, num):
#     if self.__validate(num):
#       self.result += num
#     else:
#       print("Invalid number")

# calc = Calculator()
# calc.add(10)
# calc.add(5)
# calc.add(20)
# print(calc.result)
# print(calc.__dict__)
# calc.__validate(5) # This would cause an error


class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

  def showAge(self):
    print(self.__age)

  def __addsAge(self, x):
    self.__age += x

  def setAddAge(self, x):
    self.__addsAge(x)
    print('new age ', self.__age)

p1 = Person("Ram", 25)
# print(p1.__age)
p1.showAge()
p1.setAddAge(5)