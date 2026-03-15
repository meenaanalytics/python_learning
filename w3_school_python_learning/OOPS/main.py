'''
Class is like a blueprint from which we can create Objects.
'''

# class Car:
#     def __init__(self, color, variant, display):
#         self.color = color,
#         self.variant = variant,
#         self.display = display,

#     def showColor(self):
#         print('Car color is : ', self.color)

#     def showVariant(self):
#         print('Car variant is : ', self.variant)

#     def showDisplay(self):
#         print('Car display is : ', self.display)
        

# car1 = Car('Red', 'Top', 'full HD')

# # print(car1.display)

# car1.showColor()
# car1.showVariant()
# car1.showDisplay()




# class BankAccount:

#     def __init__(self, name, account_number, balance):
#         self.name = name
#         self.acc_number = account_number
#         self.balance = balance 

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposited:", amount)
#         print("New Balance:", self.balance)

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance!")
#         else:
#             self.balance -= amount
#             print("Withdrawn:", amount)
#             print("Remaining Balance:", self.balance)

#     def check_balance(self):
#         print("Account Holder:", self.name)
#         print("Current Balance:", self.balance)


# customer1 = BankAccount('Vishal', '1234567', 1000000)

# print(customer1.acc_number)

# customer1.withdraw(200000)
# customer1.deposit(2000000)
# customer1.deposit(200)

# customer2 = BankAccount('Rohan', '888888', 1000)

# customer2.withdraw(200)
# customer2.deposit(100)
# customer2.deposit(500)

# print(customer1.balance)




# class MyClass:
#     x = 5


# p1 = MyClass()
# p2 = MyClass()
# p3 = MyClass()

# # del p1

# print(p1.x)
# print(p2.x)
# print(p3.x)


# class Account:
#     pass




# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("Ram", 36)

# print(p1.name)
# print(p1.age)



# class Person:
#   pass

# p1 = Person()

# p1.name = "Tobias"
# p1.age = 25

# print(p1.name)
# print(p1.age)


# class Person:
#   def __init__(self, name, age=45):
#     self.name = name
#     self.age = age

# p1 = Person('Ram')
# p2 = Person('Sham', 50)
# p3 = Person('Sam', 60)

# print(p2.age)



'''(------------------------------------------------------------------------)'''

# warrior_name = "Thor"
# warrior_health = 100
# warrior_attack = 50

# mage_name = "shakti"
# mage_health = 80
# mage_attack = 70

# def attack_warrior():
#   print(f'warrior attacks with power', warrior_attack)

# def attack_mage():
#   print(f'mage attacks with power', mage_attack)  

# attack_warrior()
# attack_mage()





# class character:
#   def __init__(self, name , health,attack,blood):
#     self.name = name
#     self.health = health
#     self.attack = attack
#     self.blood = blood

#   def attack_enemy(self):
#     print(f'{self.name} attacks with power{self.attack} {self.blood}')


# warrior = character('Thor',100,50,'Red') 
# mage =  character('Shakti', 80,70,'Blue')


# warrior.attack_enemy()
# mage.attack_enemy()


'''(CLASS AND OBJECTS)'''

# class car:
#     def set_details(self,brand,color):
#         self.brand = brand
#         self.color = color

#     def show_details(self):
#         print(f'this is a {self.brand} {self.color}') 


# car1 = car()
# car1.set_details('BMW' , 'Blue')   

# car2 = car()
# car2.set_details('KIA' , 'Pink')


# car1.show_details()
# car2.show_details()



# class car():
#     #method
#     def start(self):
#         print("car is starting !!!")

#     def stop(self):
#         print("car is stopping !!!")


# car1 = car()
# car2 = car()

# car1.start()
# car1.stop()

# car2.start()
# car2.stop()



# class student:
#     def set_details(self,name,marks):
#         self.name = name
#         self.marks = marks


# student1 = student ()
# student1.set_details('Rimi', 95)
# print(student1.name , student1.marks)       



'''( without constructor-------(--init--))'''

# class car:
#     def set_details(self,brand,color):
#         self.brand = brand
#         self.color = color

# #creating objects
# car1 = car()
# car1.set_details('BMW', 'RED')

# print(car1.brand , car1.color)


('''WITH constructor-------(--init--()''')

# class car:
#     def __init__(self,brand,color):
#         self.brand = brand
#         self.color = color

# car1 = car('BMW', 'BLACK') # values automatically set
# print(car1.color , car1.brand)        
        

        
# class student:
#     def __init__(self, name,age,grade,rollno):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.rollno = rollno

# student1 = student('ram',25,'A',234)  
# print(student1.name,student1.age,student1.grade,student1.rollno)       




'''()'''






















      
# class Person:
#   City = 'Hyderabad'

#   def __init__(self, name, age, salary=500000):
#     self.name = name
#     self.age = age
#     self.salary = salary

#   def greet(self):
#     print("Hello, my name is " + self.name)
#     print("Hello, my age is ", self.age)
#     print("Hello, my age is ", self.City)

#   def updateAge(self):
#     print("before age: " , self.age)
#     self.age = self.age + 5
#     print("after age:  " , self.age)
#     self.greet()

# p1 = Person("Emil", 25)
# p1.updateAge()
# p1.age = p1.age + 5
# print(p1.salary)
# del p1.salary
# print(p1.City)



# class Person:
#   lastname = ""

#   def __init__(self, name):
#     self.name = name

# p1 = Person("Linus")
# p2 = Person("Emil")

# Person.lastname = "singh"
# p2.lastname = "singh"

# print(p1.name + ' ' + p1.lastname)
# print(p2.name + ' ' + p2.lastname)


# class Person:
# #   age = 34
# #   city = 'oslo'

#   def __init__(self, name):
#     self.name = name

# p1 = Person("Tobias")

# p1.age = 25
# p1.city = "Oslo"

# print(p1.name)
# print(p1.age)
# print(p1.city)



# class Playlist:
#   def __init__(self, name):
#     self.name = name
#     self.songs = []

#   def add_song(self, song):
#     self.songs.append(song)
#     print(f"Added: {song}")

#   def remove_song(self, song):
#     if song in self.songs:
#       self.songs.remove(song)
#       print(f"Removed: {song}")

#   def show_songs(self):
#     print(f"Playlist '{self.name}':")
#     for song in self.songs:
#       print(f"- {song}")

# my_playlist = Playlist("Favorites")
# my_playlist.add_song("Tum hi ho")
# my_playlist.add_song("Happy birthday to you...")
# my_playlist.add_song("Happy birthday to you...")
# my_playlist.show_songs()