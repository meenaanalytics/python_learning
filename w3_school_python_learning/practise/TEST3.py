'''wrt a program to print number from 1 to 5 using a for loop'''

# for i in range(1,6):
#     print(i, end=" ")


'''wrt a program to print the squares of numbers from 1 to 5 '''

# for i in range(1,6):
#     print(i ** 2, end=" ")


'''wrt a program to print all even number from 1 to 10'''

# for i in range(1, 11):
#     if i % 2 ==0:
#         print(i)


'''wrt a program to calculate the sum of numbers from 1 to 10'''

# total = 0

# for i in range(1,11):
#     total += i

# print(f"sum is {total}")


'''(5)..wrt a program to print the world "python" in reverse using a for loop '''

# word = 'javascript'

# for i in range(len(word) -1, -1, -1):
#     print(word[i], end=" ")

'''(6)..wrt a program to count the number of vowels in the word "education" '''

# vowels = "aeiou"
# word = "education"
# count = 0

# for char in word:
#     if char in vowels:
#         count +=1

# print(f"Total vowels in {word} is {count}")      

'''(7)..wrt a program tp print the first 10 items of the fibonacci sequence'''

# a = 0
# b = 1
# print(a, b, end=" ")
# #1 1 2

# for _ in range(10):
#     next_term = a + b
#     print(next_term, end=" ")
#     a,b = b , next_term


'''(8)..wrt a program to calculate the factorial of a give number , such as 5.
output=5
'''

# n = 5
# factorial = 1

# for i in range(1, n+1):
#     factorial *=1

# print(f"factorial of {n} is {factorial}")    

'''(9)..wrt a program to check if a given number , such as 7, is a prime number'''

# num = 7
# is_prime = True
 
# for i in range(2, int(25 ** 0.5) + 1):
#     if num % i == 0:
#         is_prime = False
#         break

# if is_prime and num > 1:
#     print(num, "is a prime member") 
# else:
#     print(num, "is not a prime member")       


'''(10)..wrt a prg to occurrences of each character in the word "programming" '''

# word = "programming"
# char_count = {}

# for char in word:
#     if char in char_count:
#         char_count[char] +=1
#     else:
#         char_count[char] = 1

# for char, count in char_count.items():
#     print(char + ':' , count)            



'''--------------------------------------------------------------------------------------'''

# 7️⃣ Movie Ticket Pricing 🎬
# Ask:
# age
# show time ("morning", "evening")
# Rules:
# Children (<12): ₹100
# Adults:
# Morning → ₹150
# Evening → ₹200
# Senior citizens (≥60): 50% off

# child_ticket_price = 100
# adult_M_ticket_price = 150
# adult_E_ticket_price = 200

# senior_citizens_discount = 50 / 100 # 0.5

# showDic ={
#     'M' : 'morning',
#     'E' : 'evening'
# }

# age = int(input("Enter your age : "))

# show_time = input("Enter your show time(M for morning, E for evening)")

# if age < 12:
#     print("Your ticket price is : {child_ticket_price}")
# else:
#     if showDic[show_time] == 'morning':
#         if age >= 60:
#             print(f"your ticket price is : {adult_M_ticket_price * senior_citizens_discount}") 
#         else:
#             print(f"your ticket price is : {adult_M_ticket_price }")
    # else:
        
    #     if age >= 60:
    #         print(f'Good evening!!! Your ticket price is ₹{adult_E_ticket_price * senior_citizens_discount}')
    #     else:
    #         print(f'Good evening!! Your ticket price is ₹{adult_E_ticket_price}')
                




'''5️⃣ Gym Membership Fee 🏋️
Ask:
age
plan ("monthly" or "yearly")
Rules:
Monthly → ₹1000
Yearly → ₹10000
Age ≥ 60 → 30% discount
Print final fee'''

# showDic ={
#     'M' : 'monthly',
#     'Y' : 'yearly'
# }

# final_discount = 0

# age = int(input("Enter your age : "))

# plan = input("Enter your plan('M for monthly' or 'Y for yearly') : ")

# Monthly_base_fee = 1000
# Yearly_base_fee = 10000
# discount_fee = 30 / 100 # 0.3

# Monthly_fee_after_discount = 0
# Yearly_fee_after_discount = 0

# if age >= 60:
#     final_discount += discount_fee
#     if showDic[plan] == 'monthly':
#         Monthly_fee_after_discount = Monthly_base_fee - (Monthly_base_fee * final_discount)
#         print(f'Your fee after discount : ₹{Monthly_fee_after_discount}')
#     else:
#         Yearly_fee_after_discount = Yearly_base_fee - (Yearly_base_fee * final_discount)
#         print(f'Your fee after discount : ₹{Yearly_fee_after_discount}')
# else:
#     if showDic[plan] == 'monthly':
#         print(f'Your fee after discount : ₹{Monthly_base_fee}')
#     else:
#         print(f'Your fee after discount : ₹{Yearly_base_fee}')
    
    


'''1️⃣ Electricity Bill (Slab + Discount)
Ask:
units
Rules:
First 100 units → ₹3/unit
Above 100 units → ₹5/unit
If total bill > ₹1000 → 10% discount
Print final bill.'''


# electricity_bill = 100 * 3
# extra_units = 100 * 5
# units = int(input("Enter your bill units : "))

# electricity_discountAfter_bill = 10 / 100  #0.1

# final_bill = 0
# final_bill = electricity_bill + (extra_units * 5)

# if units <= 100:
#     final_bill = units * 3
#     print(f'your final bill is : {final_bill}')

# elif final_bill > 1000:
#     final_bill = final_bill - (final_bill * electricity_discountAfter_bill) 
#     print(f'your final bill is : ₹{final_bill}')   

# else:
#     extra_units = units - 100
#     print(f'your final bill is : {electricity_bill + (extra_units * 5)}')




units = int(input("Enter your bill units: "))

bill = 0

# Step 1: Slab calculation
if units <= 100:
    bill = units * 3
else:
    bill = (100 * 3) + ((units - 100) * 5)


# Step 2: Apply discount if bill > 1000
if bill > 1000:
    discount = bill * 0.10
    bill = bill - discount

# Step 3: Print result
print(f"Your final electricity bill is: ₹{bill}")





'''9️⃣ Phone Battery Status 🔋
Ask:
battery_percent
Rules:
≥ 80 → Full
30–79 → Medium 
< 30 → Low'''
    

# battery_percent = int(input("Enter your battery_percent : "))

# 1️⃣ Water Bill (Slab + Extra Charge)

# Ask:
# total liters used
# Rules:
# First 50 liters → ₹2 per liter
# Above 50 liters → ₹4 per liter
# If bill > ₹500 → add ₹50 service charge
# Task:
# Calculate and print the final water bill


