""""while loop"""
#trigger -> loop start kr dwe
#statment -> written inside loop
#breakpoint -> stop or exit the loop

'''basic while loop info'''

# canYouVote = False


# while canYouVote:
#     print('inside while loop body!!!')
#     canYouVote = False

# print('out side while loop!!!')


'''counter using while loop'''

# count = 0
# while count<= 5:
#     print("before > " , count )
#     count = count + 1
#     print("after > " , count)

#     print("-------------------")

#     print("loop ended")


'''gusse the number'''

# secret = 8
# gusse = 5

# while gusse != secret:
#     gusse =int(input('gusse the number : '))

#     if gusse != secret:
#         print("Sorry wrong gusse , try again")


# print(f"congrates you gusse the number {secret} ")   


'''add the number until enter 0'''

total = 0
amount = int(input("enter the products prize / 0 to exit >> "))

while amount !=0:
    total = total + amount
    amount = int(input("enter the products prize / 0 to exit >> "))
    print(f"current bill is : {total}")

print(f"your total bills is : {total}")    


