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


'''set'''  #similar like list , tuple but have no indexing , item index is not fixed they shuffel everytime youn run

# list , tuple , dict

#  my_set = {'vishal' , 'chandigar' , 'gugu' , 'holiday' , 30 , 100000 , 'trip' }

# print(my_set)
# my_set.add('trip')
# print(my_set)

# '''frozen_set'''

# my_set = frozen_set(['vishal' , 'chandigar' , 'gugu' , 30 , 10000 , 'trip'])

# print(my_set)
# my_set.add('trip')
# print(my_set)

'''python type casting'''

# x = int(1)            # x will be 1.0
# y = int(2.8)          # y will be 2
# z = int("3")          # z will be 3


# w = float(1)         # w will be 1.0
# x = floar(2.8)       # x will be 2.8
# y = float("3")       # y will be 3.0
# z = float("4.2")     # z will be 4.2

# x = str("s1")       # x will be "s1"       
# y = str(2)          # y will be "2"
# z = str(3.0)        # z will be "3.0"


story = """skjdfksjfoiehdunbdnaxlskfpeijwshvmcjfiencdsdj
jsncmxncmsfjsslmkdjhfi
bxnbvczmxksjeiwuurhjbjdfiljd;
ndnfdkjfkdnjbhagiaj
sddo;wklsncjdhfurirowoewyrubcnbvjbijkdow
mncjshfisjdksjksdhfkus
ndjshfidjfollvkjc
bdjsahfkeshlsdj
sbdhaskdhvl
sbdjdsbfksdhjl
ehuriuqwheioquw
ihfweiudj
jdfoekfoek
hjdjfefl
ncdjjvofkgprpfkpsoidow 

f"""

    

      

# print(story)



'''string'''

name = (vishal) = ['v' , 'i' , 's' , 'h' , 'a' , 'l']

print([3])


for character in name:
 print(name)


 print(len(name))

 txt = "hey good morning , i' ll go to school"

 print("shaktimaan" in txt)  #= true

 txt = "the best thing in life are free!"
 search = input("enter your words:")

 while search != 'exit':
  
  if search == 'exit':
   break
  
  if search in txt:
            print(f"yes, {search} is present.")
  else:
     print(f"no, {search} not present . ")

     search = input('enter your word: ')
 
    


