# (MADLIBS)

# string concatenation(aka how to put string together)
# suppose we wants to create a string that says "subscribe to ____________"
# youtuber = "vishal"  # some string variable


# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}" .format(youtuber))
# print("subscribe to {youtuber}")




# adj = input("Adjective: ")
# verb1 = input("verb: ")
# verb2 = input("verb: ")
# famous_person = input("famous person: ")

# madlibs = f"computer programming is so {adj}! it makes me so excited all the time because \
# i love to {verb1}. stay hydrated and {verb2} like you are {famous_person}!"

# print(madlibs)

'(2.. GUESS the number(computer))'

# import random

# def guess(x):
#     random_number = random.randint(1 , x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f"guess a number between 1 and {x}: "))
#         if guess < random_number:
#             print('sorry , guess again , to low.')
#         elif guess >random_number:
#             print('sorry, guess again , to high.')

#     print(f'yay , congrats. you have guessed the number {random_number} correctly!!')            

# guess(10)


'(3..(GUESS THE NUMBER  (USER) ))'

# def computer_guess(x): 
#     low = 1
#     high = x
#     feedback = ''
#     while feedback != 'c':
#         if low != high:
#             guess = random.randint(low , high)
#         else:
#             guess = low    # could also be high b/c low = high
#         feedback = input(f'Is {guess} too high (H), too low (L), or correct(c)??') .lower() 
#         if feedback == 'h':
#            high = guess - 1
#         elif feedback == 'l':
#             low = guess + 1


# print(f'yay! The computer guessed your number, {guess} ,correctly')

# computer_guess(10)



'(4..ROCK. , PAPER , SCISSORS)'

# def play():
#     user = input("'r' for rock, 'p' for paper, 's' for scissors : ")
#     computer = random.choice(['r', 'p', 's'])

#     if user == computer:
#         return 'it\'s a tie'
    
#     # r > s, s > p, p > r
#     if is_win(user , computer):
#         return 'you won!'
    

#     return ' you lost!'


# def is_win(player , opponent):
#     #return true if player wins
#     # r > s, s > p, p > r

#     if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
#          or (player == 'p' and opponent == 'r'):
#         return True
    

# print(play())    



'(FAKE NEWS HEADLINE GENERATED)'

# 1- Import the random module
import random


#2- create subject
Subjects = [
    "Shahrukh khan",
    "Virat Kholi",
    "Nirmala Sitharaman",
    "A Mumbai Cat",
    "A Group of Monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from delhi"

]


actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in mumbai Local train",
    "a plate of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL match",
    "at India gate"
]

#3- start the headline generation loop
while True:
    Subjects = random.choice(Subjects)
    actions = random.choice(actions)
    places_or_things = random.choice(places_or_things)


    headline = f"BREAKING NEWS: {Subjects} {actions} {places_or_things}"
    print("\n" + headline)

    user_input = input("\n Do you want another headline? (yes/ no)").strip()
    if user_input == "no":
        break


#print goodbye message
print("\n thanks for using the fake news headline generate.have a fun day")    






