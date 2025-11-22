'''
The match statement is used to perform different actions based on different conditions.

The Python Match Statement
Instead of writing many if..else statements, you can use the match statement.

The match statement selects one of many code blocks to be executed.
'''

# day = int(input('Enter the day. : '))

# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday") 
#     case 4:
#         print("Thursday") 
#     case 5:
#         print("Friday")  
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:     # just like else in if-else (only run if above all case did't match)
#         print("no day")   


# day = int(input('Enter Day number : '))

# if day == 1:
#   print("Monday")
# elif day == 2:
#   print("Tuesday")
# elif day == 3:
#   print("Wednesday")
# elif day == 4:
#   print("Thursday")
# elif day == 5:
#   print("Friday")
# elif day == 6:
#   print("Saturday")
# elif day == 7:
#   print("Sunday")
# else:
#   print("No day!!")                 



day = 7

match day:
    case 1| 2 | 3 | 4| 5 :
        print("Today is a weekend")
    case 6 | 7:
     print("I LOVE Weekends!!!") 


# Ram , Sham , Roy  -> 3rd floor   
# Alex , Bruno , Kartik  -> 1st floor

guest_name = input('Enter your name: ')

match guest_name:
    
    case 'Ram' | 'Sham' | 'Ghanshyam':
        print('3rd Floor allotted!!')

    case 'Alex' | 'Bruno' | 'Kartik':
        print('1rd Floor allotted!!')



guest_name = input('Enter your name: ')

match guest_name:

    case 'Ram':
        print('3rd Floor allotted!!')
        
    case 'Sham' :
        print('3rd Floor allotted!!')

    case 'Ghanshyam' :
        print('3rd Floor allotted!!')

    case 'Alex' | 'Bruno' | 'Kartik':
        print('1rd Floor allotted!!')


