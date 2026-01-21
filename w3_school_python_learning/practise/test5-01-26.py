'''1️⃣ Water Bill (Slab + Extra Charge)
Ask:
total liters used
Rules:
First 50 liters → ₹2 per liter
Above 50 liters → ₹4 per liter
If bill > ₹500 → add ₹50 service charge
Task:
Calculate and print the final water bill'''


 
# water_bill = 0
# water  = int(input("Enter your total liter used : ") )

# if water <= 50:
#     water_bill = water * 2

# else:
#     water_bill = (50 * 2 ) + ((water - 50) * 4) 

# if water_bill > 500:
#      water_bill = water_bill + 50       



# print(f"your final water bill : {water_bill}")    


'''3️⃣ Parking Fee System 🚗
Ask:
total hours parked
Rules:
First 2 hours → ₹30 per hour
Above 2 hours → ₹50 per hour
If parked more than 10 hours → add ₹200 fine
Task:
Calculate and print final parking fee'''

# Parking = int(input("Enter your parking hours : "))
# Parking_Fee = 0

# if Parking <= 2:
#     Parking_Fee = Parking * 30

# else:
#      Parking_Fee = (2 * 30) + ((Parking - 2) * 50)  

# if Parking > 10:
#      Parking_Fee = Parking_Fee + 200
          
# print(f"Final parking fee is : {Parking_Fee}")





# def ParkingFee_System(Parking):
     
#     # Parking = int(input("Enter parking hours: "))
     
#     Parking_Fee = 0
     

#     if  Parking <= 2:
#           Parking_Fee = Parking * 30

#     else: 
#          Parking_Fee = (2 * 30) + ((Parking - 2) * 5) 

#     if Parking > 10:
          
#          Parking_Fee = Parking_Fee + 200  

#     return Parking_Fee  

# final_fee = ParkingFee_System(1)

# print(final_fee)



'''function , if , else , elif , while loop , for loop , input , list , dict, tuple
try , match .'''



'''
How many students ? 
if user enter 5 then ask 5 times name & marks
Takes marks of students
Stores them in a list of tuple (name, marks, grade)
Calculates grade ( this should be inside function )
Uses tuple for grade rules
Run for loop print each student like : "Name: <name> | Marks: <marks> | Grade: <grade>"
'''


# students_list= []

# # marks = int(input("Enter marks of student : "))

# def MarksOfStudents(marks):
#      if marks >= 95:
#         #  print("grade A") 
#          return "A"
#      elif marks >= 80:
#         #   print("grade B") 
#           return "B" 
#      elif marks >= 50:
#         #   print("grade C") 
#           return "C"
#      else:
#           return "F"
#         #   print("your fail")


# z = int(input('How many student : '))
      
# for i in range(z):
#     x = input('Enter name : ')
#     y = int(input('enter marks : '))

#     grade = MarksOfStudents(y)
#     students_list.append((x, y , grade))

# # print(students_list)

# for i in students_list:
#      print(f"Name : {i[0]} | Marks: {i[1]} | Grade: {i[2]}")



'''
✅ PROGRAM 3: Parking Management System 🚗
(Covers: while loop, function, list, if else)
What this program does
Takes parking hours for multiple vehicles
Calculates parking fee
Stores results in a list
'''


# def Parking_fee_System(hours):
#     if hours <= 4:
#          return hours * 50
#     else:
#          parking_fee = (4 * 50) + ((hours - 4) * 70)
#     if hours > 10:
        
#         parking_fee =  parking_fee + 100 

#     return parking_fee

    
# x = Parking_fee_System(4)  
# print(x)

# parking_list = []

# while True:
#      hours = int(input("Enter your parking time(0 to stop : "))

#      if hours == 0:
#           break 
     
#      fee = Parking_fee_System(hours)
#      parking_list.append(fee)

# print(parking_list)

# for i in parking_list:
#      print(i)


'''
✅ PROGRAM 5: Bike Rental System 🚲
(Covers: while loop, function, list, if–else)
What this program does
Takes rental hours for multiple bikes
Calculates rental fee
Stores rental fees in a list
Rules
First 5 hours → ₹30 per hour
Above 5 hours → ₹50 per hour
If rental hours > 12 → add ₹150 fine
'''

# def Rental_Bike_feeSystem(hours):
#     if hours >= 5:
#         rental_fee = hours * 30
#     else:
#         rental_fee = (5 * 30) + ((hours - 5) * 50)

#     if hours > 12:
#         rental_fee = rental_fee + 150
    
#     return rental_fee

# rental_fee_list = []

# while True:
#     hours = int(input("Enter rental hours for multiple biker : "))
     
#     if hours == 0:
#         break

#     fee = Rental_Bike_feeSystem(hours) 
#     rental_fee_list.append(fee) 
#     print(fee) 


# print(rental_fee_list)

# for i in rental_fee_list:
#     print(i)

    



'''
✅ PROGRAM: Car Wash Billing System 🚗🧼
(Covers: while loop, function, dict, if–else)
What this program does
Ask user name
Takes number of cars washed per customer
Calculates wash charges
Stores all bills in a dict 
Rules
First 2 cars → ₹150 per car
Above 2 cars → ₹250 per car
If total cars > 5 → add ₹300 service charge

{
'Vishal': 3000,

}
'''


# def Car_washing_Billing(Car_wash_charge):

#     if Car_wash_charge >= 2:
#         Total_car_wash =  Car_wash_charge * 150

#     else:
#         Total_car_wash = (2 * 150) + ((Car_wash_charge - 2) * 250)


#     if  Car_wash_charge > 5:
#         Total_car_wash = Total_car_wash + 300

#     return Total_car_wash
    


# bills_in_dict = {}


# while True:
#     user_name = input("Enter the customer name (1 for stop): ")

#     if user_name == "1":
#         break

#     Car_wash_charge = int(input("Enter number of cars washed per customer : "))


#     if Car_wash_charge == 0:
#         break


#     fee = Car_washing_Billing(Car_wash_charge)
#     bills_in_dict[user_name] = fee


#     for name, bill in bills_in_dict.items():
     
#       print(f"Customer: {name} | Bill: ₹{bill}")



    

'''wrt a program that check whether numbers are even or odd

(1)Requirements:
check_even_odd (*numbers)
(2)inside the function:
use a for loop to go through each number.
use if_else to check:
if the numbers is even>==print(even)
else>===(odd)
(3)outside the function:
use while loop.
asks the user to enter  numbers stop when the user types 0.
'''

def Check_Even_Odd(*numbers):
    
    for i in numbers:

      if i % 2 == 0:
        print(f"{i} : is even")

      else:
        print(f"{i} : is odd")    


Check_Even_Odd(2,3,4,5,6,7,8,9,8,98,20,30,33,55,67,12,34,56,79,88)


'''--------------same question but answer is different------------------------'''

# def Check_Even_Odd(*numbers):
    
#     for i in numbers:

#       if i % 2 == 0:
#         print(f"{i} : is even")

#       else:
#         print(f"{i} : is odd")    

# num_list = []
# while True:
    
#     user = int(input("Enter numbers even or odd(o to stop) : "))

#     if user == 0:
#         break
#     num_list.append(user)

# Check_Even_Odd(num_list)




'''(1) Requirements:
check_positive_negative(*numbers)
(2) Inside the function:
Use a for loop to go through each number
Use if / elif / else:
If number > 0 → print "positive"
If number < 0 → print "negative"
If number == 0 → print "zero"
(3) Outside the function:
Use a while loop
Ask the user to enter numbers
Stop when the user types 999
Pass all entered numbers to the function using *args'''