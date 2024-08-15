# calculator
# add
from art import logo
def add(n1,n2):
    return n1 + n2

# subtract
def sub(n1,n2):
    return n1 - n2

# mul
def mul(n1,n2):
    return n1 * n2

# div
def div(n1,n2):
    return n1 / n2

oprations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}
def calculator():
    print(logo)
    num1 = float(input("what's the first number?\n"))
    
    for symbol in oprations:
        print(symbol)
    
    
    should_cont = True
    while  should_cont:
        operation_symbol = input("pick an operation :\n")
        num2 = int(input("whats the next number\n"))
        clc = oprations[operation_symbol]
        answer = clc(num1,num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        
        jjiu= input(f"Type'y' to continue calculating with {answer}, or type 'n' to exit.")
        if jjiu == 'y':
            num1 = answer
        else:
            should_cont = False 
            calculator()   
            
calculator()              
           




