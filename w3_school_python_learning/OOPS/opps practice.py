


# class circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return (22/7) * self.radius ** 2

#     def perimerter(self):
#         return 2 * (22/7) * self.radius
    

# c1 = circle(21)
# print(c1.area())
# print(c1.perimerter())    
        


class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =" , self.role)
        print("dept =",self.dept)
        print("salary =", self.salary)

class Enginner(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Enginner", "IT", "95,000" )     

engg1 = Enginner("iron man" , 49)
engg1.showDetails()           
                