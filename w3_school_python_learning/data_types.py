'''Example	Data Type	Try it'''

# x = "Hello World"	                            str	
# x = 20	                                    int	
# x = 20.5	                                    float	
# x = 1j	                                    complex	
# x = ["apple", "banana", "cherry"]	            list	
# x = ("apple", "banana", "cherry")	            tuple	
# x = range(6)	                                range	
# x = {"name" : "John", "age" : 36}	            dict	
# x = {"apple", "banana", "cherry"}	            set	
# x = frozenset({"apple", "banana", "cherry"})	frozenset	
# x = True	                                    bool	
# x = b"Hello"	                                bytes	
# x = bytearray(5)	                            bytearray	
# x = memoryview(bytes(5))	                    memoryview	
# x = None	                                    NoneType	

'''set'''  #similar like list, tuple but have no indexing , items index is not fixed they shuffle everytime you run it

# list , tuple, dict, 

# my_set = {'Vishal', 'Chandigarh', 'Guggu', 'holiday', 30, 7000000} #indexing is not fixed automatically decided

# print(my_set)
# my_set.add('Trip')
# print(my_set)

'''frozen_set'''

# my_set = frozenset(['Vishal', 'Chandigarh', 'Guggu'])

# print(my_set)
# my_set.add('Trip')
# print(my_set)

'''Python type Casting'''

# x = int(1)   # x will be 1
# y = int(2.8) # y will be 2
# z = int("3") # z will be 3


# x = float(1)     # x will be 1.0
# y = float(2.8)   # y will be 2.8
# z = float("3")   # z will be 3.0
# w = float("4.2") # w will be 4.2

# x = str("s1") # x will be 's1'
# y = str(2)    # y will be '2'
# z = str(3.0)  # z will be '3.0'


story = """saldfkjasdlfk asdflfkjasdflkajs asd
fasldfkj asldfkj as
fasdfkasjdf asdf
asdf
;askdjfkasjdf
asdfasjd;fkajs
df as
;dkfj asdfkj asdkjfas;kdjf 
asjdf 
asjdf ;kjsadfk jsad
fjas;kdjf 
a;skdfj; askjdf
 ;sjdf
 ;kj asdfkjsa;f jsa
 ;dfkj ;sakdjf 
 askdjf
 asdjf ;askj f"""

# print(story)


'''string'''

#name = 'vishal' # -> ['v', 'i', 's', 'h', 'a', 'l']

# print(name[3])

# for character in name:
#     print(character)

# print(len(name))

# txt = "Hey good morning , i'll go to school"

# print("shaktiman" in txt) #= True

# txt = "The best things in life are free!"
# search = input('Enter your word: ')

# while search != 'exit':
    
#     if search == 'exit':
#         break

#     if search in txt:
#         print(f"Yes, {search} is present.")
#     else:
#         print(f'No, {search} not present. ')

#     search = input('Enter your word: ')