
num = int(input("enter a number: "))

while (num > 5):
    print("Hello world")
    num = int(input("enter a number: "))
    print("by world")


for a in range(1,11):
    print(a)

def fun():
    print("hello world")
    return "hello wprld"

fun()
print(fun())
x = fun()
y = x
z = y
print(z)

def sayMyName(fname , lname):
    return f"Hi, my name is {fname} {lname}"

print(sayMyName('vishal' , 'kumar'))


x = sayMyName
print(x(('Ram', 'Singh')))


def sayMyName(fname='vishal', lname='kumar'):
    return f"Hi, my name is {fname} {lname}"

x =sayMyName("vishal", "kumar")
x = sayMyName()
print(x)


def sayMyName(fname, lname, count):

    for i in range(count):
        print(f"{fname} {lname} {i}")

    return "function end here"

x = sayMyName('vishal' , 'kumar', 2)
print(x)




def ableToVote(age):
    if age==18 or age>18:
        print('You can vote')
    else:
        print('You can not vote')    


ableToVote(2)