'''
4 function add() , sub(), div(), mul()

1 main function main(Operation, *value)

'''

'''
Operation = 'ADD', 'SUB', 'DIV', 'MUL'

'''


def add(*vals):
    result = 0
    for val in vals:
        result += val
        return result
    


def sub(*vals):         #[4 , 5 , 2]
    result = vals[0]        # start with first value 
    for val in vals[1:]:    # subtract remaining 
        result -= val
        return result  



def div(*vals):
    print("Divide function runned!!")  
    return vals[0] / vals[1] 



def mul(*vals):
    result = vals[0]
    for val in vals[1]:
        result *= val
        return result
    

def main(operation, *values):
    OPERATIONS = ['ADD', 'SUB', 'DIV', 'MUL']
    try:
        if type(operation) != str or operation not in OPERATIONS:
            raise Exception("please enter a valid type from these : 'ADD', 'SUB', 'DIV', 'MUL'")
        else:
            match operation:
                case 'ADD':
                    return add(*values)
                case 'SUB':
                    return sub(*values)
                case 'DIV':
                    if len(values) >2:
                        raise Exception("only 2 number are allowed in division!!")
                    return div(*values)
                case 'MUL':
                    return mul(*values)
                case _:
                    raise Exception("invalid operation type")
    except Exception as e:
        print(e)            


output = main('ADD', 4 , 5, 2)
print('add > ', output)   # 11

output1 = main('SUB', 4 , 5, 2)
print('sub > ', output1)  # -3  (4 - 5 - 2)

output2= main('MUL', 4 , 5, 2)
print('mul > ', output2)  # 40 (4 * 5 * 2)

output3= main('DIV', 10, 5, 5)
print('div > ', output3)  

output4= main('Sandwich', 10, 5, 5)
print('div > ', output4)          